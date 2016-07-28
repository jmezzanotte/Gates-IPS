# Written-by:           John Mezzanotte
# Date-last-modified:   8-11-2015
# Description:          Loops through .csv files in a directory and will convert tables into sql tables within a database.
#                       You can then manage the relational database in any sql system that will handle .db files. John Mezzanotte has chosen
#                       to use sqlite3 for his work on this project. All SQL queries that have been written by John Mezzanotte
#                       have been written for SQLite3.
#
# Notes:                This program will only parse .csv files.
#
# params:               to_sql(source_file, save_location, database_name)
#                           - source_file (required)  : Full path to the directory with your .csv files
#                           - save_location(optional) : Location where you want to save your database. If this is argument is omitted
#                                                        the program will use the users current working directory to save the file.
#                           - database_name(optional) : The name you want to use for your database. If this argument is omitted the
#                                                       program will use the default name "gates_sustainability"


import glob
import csv
import sqlite3
import os
import sys
from gates.NoCSVsFoundError import *

def to_sql(source_path, numeric_attribute_names, save_location=os.getcwd(), database_name ):

    db_location = save_location

    # returns a list we can iterate through
    files_to_parse = glob.glob(source_path + '*.csv') 

    # If we have no .csv files tell the user. If we have .csv files, process them
    if len(files_to_parse) != 0: 

        # process each file in directory 
        for name in glob.glob(source_path + '*.csv'):

            # open .csv and read first row; uses as attribute names in schema
            csv_data = csv.reader(open(name))
            attribute_names = csv_data.next()

            #grab the base name of the file
            file_name = os.path.basename(name)

            # returns a tuple with the name of the file and extention. Name of the file is the first element
            table_name = os.path.splitext(file_name)[0]
        
            # create relational schema using header values from .csv.
            # build sql query then run it below
            create_table = "CREATE TABLE {table} (".format(table = table_name)
            for i in range(0, len(attribute_names)) :
                if i == len(attribute_names) - 1 :
                    create_table += attribute_names[i] + "\tNUMBER)"
                elif attribute_names[i]in numeric_attribute_names  :
                    create_table += attribute_names[i] + "\tNUMBER,"
                else:
                    create_table += attribute_names[i] + "\tTEXT, "

            #open database connection
            try:
                con = sqlite3.connect(save_location + "\\" + database_name)
                # If you want to use 8 bit strings instead of unicode in sqlite3 set connection text_factory for str
                con.text_factory = str
                cur = con.cursor()
                cur.execute("DROP TABLE IF EXISTS {table}".format(table = table_name))
                print create_table
                cur.execute(create_table)
                print create_table
                print '%s created successfully' % table_name

                for i in csv_data:
                    data_row = i #data row will be assigned to a list
                    holders = ','.join('?' * len(data_row))
                    insert_statement = "INSERT INTO {table} VALUES({holders})".format(table=table_name, holders=holders)
                    print insert_statement
                    cur.execute(insert_statement, i)
            except sqlite3.Error as e:
                print "Error %s: " % e.args[0]
                sys.exit(1)
            finally:
                if con:
                    con.commit()
                    con.close()
    else:
        raise NoCSVsFoundException()
    

if __name__ == "__main__":
    print "run Tests here"



