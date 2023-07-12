from TypeScript import convert_from_class_to_ts_interface
from sql import convert_from_class_to_sql_table, convert_from_sql_table_to_class

if __name__ == '__main__':
    types: [] = ['ts', 'sql', 'sql_to_class']
    print(", ".join(types))

    #type = input()
    type = 'sql_to_class'

    if type == types[0]:
        convert_from_class_to_ts_interface()
    elif type == types[1]:
        convert_from_class_to_sql_table()
    elif type == types[2]:
        convert_from_sql_table_to_class()
