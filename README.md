# Gates-IPS
Posting scripts I used during analysis

#Written by
John Mezzanotte



#Sustainability


The python files contained here are the source versions of the final graph creation scripts for the Gates expenditure analysis 
in 2014 and 2015. The script parse_sql.py is used to parse .csv files within a directory into valid sql queries. This script 
returns a database with all 7 years of 
expenditure data. We can then run queries against that data base to create our final graph data. 


The aggregate.py file is responsible for runnning the sql queries against the data base and gives the use control over the appropriation 
percentages
that are used to create the graphs. The aggregation.py script is used as a module and imported into each of the school's 
individual aggregation 
scripts.

These files are contained here for referece. I've placed them in my python intallation root 
"C:\Python27" and created a package called gates. 


`from gates import aggregate`

