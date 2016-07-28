# Written-by:           John Mezzanotte
# Date-last-modified:   11-19-2015
# File:                 calculate_appropriation_percentages.py
# Description:          This script will run a series of sql queries that will
#                       output the proper appropriation percentages for each
#                       spending category.
# 
#                       I have de-identified several categories used in the script. Those modifications will be found in 
#                       the in __name__ == "__main__" portion of the script where I have tested this script and demonstrate
#                       how I used it.


import sqlite3
import sys

def total_by_lever_year(year, col_label, table_name, table_in_use, category, cols, lever_nums):
    
    # build parameter as a string to feed into final query 
    add_cols_across = ""

    for i in range(0,len(cols)):
        if i == 0:
            add_cols_across += cols[i]
        elif i != len(cols):
            add_cols_across += " + " + cols[i]
        else:
            add_col_across += cols[i]

    #build parameter as a string to feed into final query 
    add_cols_downward = ""

    for i in range(0, len(cols)):
        if i == 0 :
            add_cols_downward += "SUM(" + cols[i] + ") AS " + cols[i]
        else:
            add_cols_downward += ", SUM(" + cols[i] + ") AS " + cols[i]


    # Build part of query that will handle lever choices
    lever_condition = ""

    for i in range(0, len(lever_nums)):
        if i == 0 :
            lever_condition += lever_nums[i]
        elif i != len(cols):
            lever_condition += " OR " + lever_nums[i]
        else:
            lever_condition += lever_nums[i]
        
    
    query = """
        DROP TABLE IF EXISTS {table};
        CREATE TABLE {table} AS 
        SELECT Category, Year_{funding_year}, SUM({columns_to_sum}) AS {col_name}
        FROM(
            SELECT '{funding_category}' AS Category, 'Year_{funding_year}' AS Year_{funding_year}, {downward_sum}
            FROM {from_table}
            WHERE ({levers})AND funding_year = {funding_year}
        );
    """.format(columns_to_sum = add_cols_across, table = table_name, from_table = table_in_use, downward_sum = add_cols_downward,
               levers = lever_condition, col_name = col_label, funding_year = year, funding_category = category)
    print query
    return query


def sum_tables(final_table_name,  *args):

    subquery = ""
    table_drop = ""

    for i in range(0, len(args)):
        if i == len(args) - 1:
            subquery += "SELECT * FROM " + args[i]
        else:
            subquery += "SELECT * FROM " + args[i] + " UNION "
            
    query = """
        DROP TABLE IF EXISTS {final_table};
        CREATE TABLE {final_table} AS 
        SELECT *
        FROM (
              {tables_to_stack}
             );


    """.format(final_table = final_table_name,  tables_to_stack = subquery)
    
    
    print query 
    return query

if __name__ == "__main__":


    database = "<path to database>"

    columns = ["CAT1", "CAT2", "CAT3", "CAT4", "CAT5",  "CAT6", "CAT7", "CAT8"]

    TElevers = ["flag1a = 1", "flag1b = 1", "flag1c = 1", "flag4a = 1", "flag4c = 1", "lever_number = 10"]
    STlevers = ["lever_number = 5", "lever_number = 10"]
    PDlevers = ["flag1a = 1", "flag4a = 1", "flag4b = 1", "flag6b", "lever_number = 7", "lever_number = 8", "lever_number = 10"]
    CCLlevers = ["lever_number = 2", "lever_number = 3", "lever_number = 7", "lever_number = 10", "flag6a = 1"]
    

    # Open database connection
    try:
        con = sqlite3.connect(database)
        cur = con.cursor()

    # loop through 7 years
        for i in range(1, 8):
            cur.executescript(total_by_lever_year(i, "TE", "TETotal_y" + str(i), "SITE_y1_y7" , "Teacher Evaluation", columns, TElevers))
            cur.executescript(total_by_lever_year(i, "ST", "STTotal_y" + str(i), "SITE_y1_y7" , "Staffing", columns, STlevers))
            cur.executescript(total_by_lever_year(i, "PD", "PDTotal_y" + str(i), "SITE_y1_y7" , "Professional Development", columns, PDlevers))
            cur.executescript(total_by_lever_year(i, "CCL", "CCLTotal_y" + str(i), "SITE_y1_y7" , "Career Ladders", columns, CCLlevers))
            print "query successfull.\n"

        cur.executescript(sum_tables("CCL_TOTALS", "CCLTotal_y1", "CCLTotal_y2", "CCLTotal_y3", "CCLTotal_y4",
                                     "CCLTotal_y5", "CCLTotal_y6", "CCLTotal_y7"))
        cur.executescript(sum_tables("PD_TOTALS", "PDTotal_y1", "PDTotal_y2", "PDTotal_y3", "PDTotal_y4",
                                     "PDTotal_y5", "PDTotal_y6", "PDTotal_y7"))
        cur.executescript(sum_tables("ST_TOTALS", "STTotal_y1", "STTotal_y2", "STTotal_y3", "STTotal_y4",
                                     "STTotal_y5", "STTotal_y6", "STTotal_y7"))
        cur.executescript(sum_tables("TE_TOTALS", "TETotal_y1", "TETotal_y2", "TETotal_y3", "TETotal_y4",
                                     "TETotal_y5", "TETotal_y6", "TETotal_y7"))

        for i in range(1, 8):
            cur.execute("DROP TABLE IF EXISTS CCLTotal_y{year}".format(year = i))
            cur.execute("DROP TABLE IF EXISTS PDTotal_y{year}".format(year = i))
            cur.execute("DROP TABLE IF EXISTS STTotal_y{year}".format(year = i))
            cur.execute("DROP TABLE IF EXISTS TETotal_y{year}".format(year = i))
            
    except sqlite3.Error as e:
        print "Error %s: " % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.commit()
            con.close()

            
    
    




    
