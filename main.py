import case_convert
import general
import helper
from extractor import extract_from_line_with_input
from query import insert_where
from type_script import convert_from_class_to_ts_interface
from sql import convert_from_class_to_sql_table, convert_from_sql_table_to_class

import requests

# x = requests.get('http://localhost:8009/api/Order/GetOrders?IsExcel=true')
# print(len(x.json()['content']['items']))

if __name__ == '__main__':

    functions = {
        'ts': convert_from_class_to_ts_interface,
        'class_to_sql_table': convert_from_class_to_sql_table,
        'sql_table_to_class': convert_from_sql_table_to_class,
        'snake_case_to_pascal_case':lambda: case_convert.convert(input_type),
        'snake_case_to_camel_case': lambda: case_convert.convert(input_type),
        'camel_case_to_lowercase': lambda: case_convert.convert(input_type),
        'lowercase_to_uppercase': lambda: case_convert.convert(input_type),
        'camel_case_to_uppercase': lambda: case_convert.convert(input_type),
        'from_class_to_interface': general.from_class_to_interface,
        'from_class_to_json': general.from_class_to_json,
        'auto_mapper_1': general.auto_mapper_1,
        'auto_mapper_2': general.auto_mapper_2,
        'insert_where': insert_where,
        'extract_from_line': extract_from_line_with_input,
        'exit': (lambda: None)
    }

    helper.print_array(functions.keys())

    input_type: str = input()

    if input_type.isnumeric():
        input_type = functions.keys()[int(input_type)]
    input_type = input_type.strip()

    functions[input_type]()



 #
 # GET_EXCEL_SITES_REPORT,
 # GET_PDF_SITES_REPORT,

