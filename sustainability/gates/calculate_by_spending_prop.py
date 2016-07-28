'''
' Written-by:           John Mezzanotte
' Project:              Gates IPS Evaluation: Sustainability
' Date-last-modified    12-17-2015
' Description:          Helper methods to assist in the calculation of spending allocations
'''



def calculate_prop_by_spending(sum_cols, criteria_list, year, from_table, table_name, use_or):

    to_sum = ""
    subquery = ""
    where_clause = ""

    for i in range(0, len(sum_cols)):
        if i == len(sum_cols) - 1: 
            to_sum += sum_cols[i]
            subquery += "SUM(" + sum_cols[i] + ") AS " + sum_cols[i]
        else: 
            to_sum +=  sum_cols[i] + " + "
            subquery += "SUM(" + sum_cols[i] + ") AS " + sum_cols[i] + ", "

    for i in range(0, len(criteria_list)):
        if use_or:
            if i == len(criteria_list) - 1 : 
                where_clause += criteria_list[i]
            else:
                where_clause += criteria_list[i] + " OR "
        else:
            if i == len(criteria_list) - 1 : 
                where_clause += criteria_list 
            else:
                where_clause += criteria_list[i] + " AND " 
            

    
    query = '''
    SELECT SUM({cols}) AS {output_table}
    FROM(
        SELECT {subquery_sums}
        FROM {using_table}
        WHERE ({criteria}) AND funding_year = {funding_year})
        '''.format(cols = to_sum, using_table = from_table, output_table = table_name,  subquery_sums = subquery, criteria = where_clause, funding_year = year)


    return query


if __name__ == "__main__":

    cols = ['CAT1','CAT2','CAT3','CAT4','CAT5','CAT6','CAT7','CAT8']
    where = ['flag1b = 1','flag3a = 1','flag4b = 1','flag4c = 1','flag5a = 1', 'flag5b = 1', 'flag6a = 1', 'flag6b = 1',
                          'flag6c = 1', 'flag6d = 1','flag6e = 1', 'flag6f = 1']

    


    print calculate_prop_by_spending(cols, where, 1, "From test", "out test", True)
    
