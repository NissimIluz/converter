import case_convert
import general
import helper
from type_script import convert_from_class_to_ts_interface
from sql import convert_from_class_to_sql_table, convert_from_sql_table_to_class

if __name__ == '__main__':
    types: [] = ['ts', 'sql', 'sql_to_class', 'lowercase_to_pascal_case',
                 'lowercase_to_camel_case', 'lowercase_to_uppercase',
                 'camel_case_to_lowercase',
                 'from_class_to_interface', 'from_class_to_json', 'auto_mapper_1',
                 'auto_mapper_2']
    helper.print_array(types)

    type = input()

    if type == types[0]:
        convert_from_class_to_ts_interface()
    elif type == types[1]:
        convert_from_class_to_sql_table()
    elif type == types[2]:
        convert_from_sql_table_to_class()
    elif type == types[3]:
        case_convert.convert(type)
    elif type == types[4]:
        case_convert.convert(type)
    elif type == types[5]:
        case_convert.convert(type)
    elif type == types[6]:
        case_convert.convert(type)
    elif type == types[7]:
        general.from_class_to_interface()
    elif type == types[8]:
        general.from_class_to_json()
    elif type == types[9]:
        general.auto_mapper_1()
    elif type == types[10]:
        general.auto_mapper_2()