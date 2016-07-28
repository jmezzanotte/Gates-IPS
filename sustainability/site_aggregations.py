'''
Written by: John Mezzanotte
Project: Gates IPS Evaluation - RESOURCES / SUSTAINABILITY
Date-last-modified: 2/11/2016
Description: This is the python script that manages the running of the SQL queries
             that perform all aggregations and analysis for a given site.
             The aggregation specifications are taken from the updated information
             supplied by each site.

Dependencies: module called gates and a script called aggreate. 
'''

from gates.aggregate import *

te_vars = {}
staffing_vars = {}
pd_vars = {}
ccl_vars = {}


def run_appropriation_queries(database, appropriation_file, item_level_appropriation):

    # We only have a need for one flag in PUC. There is only 1 item level appropriation and that
    # is in initiative(lever) 4

    flag4a = "flag4a" # for those at 25% 
    flag4b = "flag4b" # for those at 100%

    # Set constants for table names 
    te_table = "TEYear"
    te_lever_name = "Teacher Evaluation"

    st_table = "StaffingYear"
    st_lever_name = "Staffing"

    pd_table = "PDYear"
    pd_lever_name = "Professional Development"
    pd_category = "PD"

    ccl_table = "CCLYear"
    ccl_lever_name = "Compensation and Career Ladders"
    ccl_category = "CCL"

    # Set CMO name
    cmo = "org name here"

    # Read in sql queries that will be used by the function we created in the aggregate module
    appropriation_sql = open(appropriation_file, 'r')
    appropriation_query = appropriation_sql.read()
    appropriation_sql.close()


    # Item level sql query
    item_level_appr_sql = open(item_level_appropriation, 'r')
    item_level_query = item_level_appr_sql.read()
    print item_level_query
    item_level_appr_sql.close()

    # Set up teacher evaluation table queries 

    for i in range(1, 8):
        te_vars["te_lever1_year{0}".format(i)] = appropriate_lever(cmo, te_lever_name, te_table, 1, i, 0.40, appropriation_query)
        te_vars["te_lever3_year{0}".format(i)] = appropriate_lever(cmo, te_lever_name, te_table, 3, i, 0.90, appropriation_query)
        te_vars["te_lever4_flag4a_year{0}".format(i)] = aggregate_by_line_item(cmo, te_lever_name, te_table, flag4a, i, 0.25,
                                                                               item_level_query, "lever_number = 4", "flag4a = 1")
   # Set up Staffing table queries 
    for i in range(1, 8):
        staffing_vars["st_lever4_flag4a_year{0}".format(i)] = aggregate_by_line_item(cmo, st_lever_name, st_table, flag4a, i, 0.25,
                                                                                     item_level_query, "lever_number = 4", "flag4a = 1")
    # Set up PD Table queries
    for i in range(1, 8) :
        pd_vars["pd_lever1_year{0}".format(i)] = appropriate_lever(cmo, pd_lever_name, pd_table, 1, i, 0.60, appropriation_query)
        pd_vars["pd_lever2_year{0}".format(i)] = appropriate_lever(cmo, pd_lever_name, pd_table, 2, i, 1.00, appropriation_query)
        pd_vars["pd_lever4_flag4a_year{0}".format(i)] = aggregate_by_line_item(cmo, pd_lever_name, pd_table, flag4a, i, 0.25,
                                                                                item_level_query, "lever_number = 4", "flag4a = 1")
        pd_vars["pd_lever4_flag4b_year{0}".format(i)] = aggregate_by_line_item(cmo, pd_lever_name, pd_table, flag4b, i, 1.00,
                                                                               item_level_query, "lever_number = 4", "flag4b = 1")
    # Set up Career Ladders table queries
    for i in range(1, 8):
        ccl_vars["ccl_lever3_year{0}".format(i)]  = appropriate_lever(cmo, ccl_lever_name, ccl_table, 3, i, 0.10, appropriation_query)
        ccl_vars["ccl_lever4_flag4a_year{0}".format(i)] = aggregate_by_line_item(cmo, ccl_lever_name, ccl_table,flag4a, i, 0.25,
                                                                                 item_level_query, "lever_number = 4", "flag4a = 1")
        ccl_vars["ccl_lever5_year{0}".format(i)] = appropriate_lever(cmo, ccl_lever_name, ccl_table, 5, i, 1.00, appropriation_query)
        ccl_vars["ccl_lever6_year{0}".format(i)] = appropriate_lever(cmo, ccl_lever_name, ccl_table, 6, i, 1.00, appropriation_query)

       
    # place all dictionaries (associative arrays in a list)
    queries = [te_vars, staffing_vars, pd_vars, ccl_vars]
    

    # Open database connection loop through the dictionaries that hold the sql queries
    
    try:
        con = sqlite3.connect(database)
        cur = con.cursor()

        for i in queries:
            for key in i:
                cur.executescript(i[key])
                print "Query on {0} was successful".format(key)
        
    except sqlite3.Error as e:
        print "Error %s: " % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.commit()
            con.close()

    return queries
        
def stack_tables(database, sql_file):

    # Read in sum tables query
    sum_tables_sql = open(sql_file, 'r')
    sum_tables_query = sum_tables_sql.read()
    sum_tables_sql.close()

    te_stack = {}
    staffing_stack = {}
    pd_stack = {}
    ccl_stack = {}

    # populate the new dictionaries with the sum_tables query. 
    for i in range(1, 8):
        te_stack["te_year{0}".format(i)] = sum_tables("TEYear", i, sum_tables_query, "TEYear{0}_lever1".format(i), "TEYear{0}_lever3".format(i), "TEYear{0}_Itemflag4a".format(i)) 

        staffing_stack["st_year{0}".format(i)] = sum_tables("StaffingYear", i, sum_tables_query, "StaffingYear{0}_Itemflag4a".format(i))

        pd_stack["pd_year{0}".format(i)] = sum_tables("PDYear", i, sum_tables_query, "PDYear{0}_Lever1".format(i), "PDYear{0}_Lever2".format(i),
                                                      "PDYear{0}_Itemflag4a".format(i), "PDYear{0}_Itemflag4b".format(i))
                                                  
        ccl_stack["ccl_year{0}]".format(i)] = sum_tables("CCLYear", i, sum_tables_query, "CCLYear{0}_Lever3".format(i), "CCLYear{0}_Itemflag4a".format(i),
                                                         "CCLYear{0}_Lever5".format(i), "CCLYear{0}_Lever6".format(i))
   
    
    # one more list to make the loop code a little more concise
    queries = [te_stack, staffing_stack, pd_stack, ccl_stack]
    
    try:
        con = sqlite3.connect(database)
        cur = con.cursor()

        # run all of our sum tables queries
        for i in queries:
            for key in i:
                cur.executescript(i[key])
                print "Query on {0} was successful".format(key)
        
    except sqlite3.Error as e:
        print "Error %s: " % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.commit()
            con.close()
       
    return queries

def create_final_table(database):

    final_table = append_tables("SITE_spending_by_lever_funder_year", "TEYear1", "TEYear2", "TEYear3", "TEYear4", "TEYear5", "TEYear6", "TEYear7",
              "StaffingYear1", "StaffingYear2", "StaffingYear3", "StaffingYear4", "StaffingYear5", "StaffingYear6", "StaffingYear7",
              "PDYear1", "PDYear2", "PDYear3", "PDYear4", "PDYear5", "PDYear6", "PDYear7",
              "CCLYear1", "CCLYear2", "CCLYear3", "CCLYear4", "CCLYear5", "CCLYear6", "CCLYear7")

    
    try:
        con = sqlite3.connect(database)
        cur = con.cursor() 
        cur.executescript(final_table)
        print "Append query successfull.\n"
            
    except sqlite3.Error as e:
        print "Error %s: " % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.commit()
            con.close()

    
if __name__ == "__main__":

	
    database = "<database location>\<databasefile.db>"

    sql_dir = "<Path to sql queries>"

    # paths to sql files. 
    appropriation_file = sql_dir + "sql_appropriations.txt"
    item_level_appropriations = sql_dir + "sql_item_level_appropriations.txt"

    print item_level_appropriations
    sum_tables_query = sql_dir + "sum_tables_query.txt"


    # run all appropriation queries
    run_appropriation_queries(database, appropriation_file, item_level_appropriations)

    stack_tables(database, sum_tables_query)
   

    create_final_table(database)
