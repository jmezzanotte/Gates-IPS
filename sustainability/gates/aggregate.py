# Written-by:           John Mezzanotte
# Date-last-modified:   9-24-2015
# File:                 aggregate data 
# Description:          perform aggregations used for graphing expenditure data
#                       for districts and CMOs


import sqlite3
import sys


def appropriate_lever(site_name, lever_name, table_name, lever_number, year, proportion, sql_query ):

    """ This function will apply a propotion to the total lever value. This is custom for Hillsborougho """

    query = sql_query.format(name_of_lever = lever_name, number_of_lever = lever_number, table = table_name, lever_prop = proportion, funding_year = year,
              site=site_name)

	
    print query
		
    return query




def lever_no_prop(site_name,lever_name, table, lever_number, year, sql_query):

        query = sql_query.format(table_name = table, name_of_lever = lever_name, number_of_lever = lever_number, funding_year = year,
                   site=site_name)
	
	print query
	
        return query

def aggregate_by_line_item(site_name, lever_name,  table, lever_number, item_catagory, year, prop, sql_query,  *args):
    
        query = sql_query.format(table_name = table, funding_year = year, name_of_lever = lever_name,
                                 number_of_lever = lever_number, lever_prop = prop, site=site_name, item = item_catagory)

        for i in range(0, len(args)):
            if i == len(args) - 1:
                query +=  args[i] + ";"
            else:
                query += args[i] + " AND "

	print query 
        return query
       

def sum_tables(final_table_name, year, sql_query, *args):

    subquery = ""
    table_drop = ""

    for i in range(0, len(args)):
        if i == len(args) - 1:
            subquery += "SELECT * FROM " + args[i]
        else:
            subquery += "SELECT * FROM " + args[i] + " UNION "
            
    #Clean up the database. Create the drop table query
    
    #for i in range(0, len(args)):
    #    table_drop += "DROP TABLE IF EXISTS " + args[i] + ";"
   
    query = sql_query.format(final_table = final_table_name, funding_year = year, tables_to_stack = subquery)
    
    print query 
    return query

def append_tables(final_table_name, *args):

    query = "DROP TABLE IF EXISTS {final_table}; CREATE TABLE {final_table} AS ".format(final_table = final_table_name)

    for i in range(0, len(args)):
        if i == len(args) - 1:
            query += "SELECT * FROM " + args[i] 
        else:
            query += "SELECT * FROM " + args[i] + " UNION "

    query += " ORDER BY Name DESC"

    print query 
    return query



   
    
