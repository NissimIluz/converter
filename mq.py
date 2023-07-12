import helper

def run():
    print('table_name:')
    table_name = input()
    print('data:')
    lines = helper.read_lines()
    new_data = []
    property_names = []

    for line in lines:

        line = helper.remove_unused_syntax(line, " ")

        property_name = helper.lowercase_to_pascal_case(line)

        new_line = f',{table_name}.{line.replace(",","")} AS {property_name}'
        property_names.append(property_name)
        new_data.append(new_line)

    print(f'-- {table_name}\n')
    helper.print_array(new_data[1:])
    print('\n\n')
    for property_namae in property_names:
        to_print = f'public string {property_namae}' + '{ get; set; }'
        print(to_print)

if __name__ == '__main__':
    run()