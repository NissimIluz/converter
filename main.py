import helper
from functions import functions

if __name__ == '__main__':
    helper.print_array(functions.keys())

    input_type: str = input()

    if input_type.isnumeric():
        input_type = functions.keys()[int(input_type)]
    input_type = input_type.strip()

    functions[input_type]()
