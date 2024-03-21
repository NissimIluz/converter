import case_convert
import general
import ts
from extractor import extract_from_line_with_input
from query import insert_where
from sql import convert_from_class_to_sql_table, convert_from_sql_table_to_class
from text_compare import find_differences
from type_script import convert_from_class_to_ts_interface

functions = {
        'ts': convert_from_class_to_ts_interface,
        'class_to_sql_table': convert_from_class_to_sql_table,
        'sql_table_to_class': convert_from_sql_table_to_class,
        'snake_case_to_pascal_case':lambda: case_convert.convert('snake_case_to_pascal_case'),
        'snake_case_to_camel_case': lambda: case_convert.convert('snake_case_to_camel_case'),
        'camel_case_to_lowercase': lambda: case_convert.convert('camel_case_to_lowercase'),
        'lowercase_to_uppercase': lambda: case_convert.convert('lowercase_to_uppercase'),
        'pascal_case_or_camel_case_to_uppercase': lambda: case_convert.convert('pascal_case_or_camel_case_to_uppercase'),
        'word_to_camel_case': lambda: case_convert.convert('word_to_camel_case'),
        'word_to_kebab_case': lambda: case_convert.convert('word_to_kebab_case'),
        'from_class_to_interface': general.from_class_to_interface,
        'from_class_to_json': general.from_class_to_json,
        'auto_mapper_1': general.auto_mapper_1,
        'auto_mapper_2': general.auto_mapper_2,
        'insert_where': insert_where,
        'extract_from_line': extract_from_line_with_input,
        'find_differences': find_differences,
        'to_url': ts.to_url,
        'to_url_function': ts.to_url_function,
        'exit': (lambda: None)
    }