import config
import helper


def convert_from_class_to_sql_table(lines=None):
    if not lines:
        lines = helper.read_lines()
    attributes = None
    if 'class' in lines[0]:
        line = helper.remove_unused_syntax(lines[0])

        line = line.replace('class', '')
        line = ''.join([i for i in line if i.isalpha()])
        print(f'CREATE TABLE [dbo].[{line}] (')
        lines.pop(0)
    else:
        print(f'CREATE TABLE [dbo].[tableName] (')
    for index in range(len(lines)):

        line = helper.remove_unused_syntax(lines[index])
        if not line:
            continue

        new_attribute = helper.is_prop_attribute(line)
        if new_attribute:
            if attributes:
                attributes = f"{attributes} {new_attribute}"
            else:
                attributes = new_attribute
            continue
        if helper.is_attribute_line(line):
            continue
        line = ''.join([i for i in line if i.isalpha()])
        line = handle_types(line, config.types_c_to_sql_type)

        if not line:
            continue
        if attributes:
            line = f"{line} {attributes},"
        else:
            line = f"{line} NULL,"
        attributes = None
        lines[index] = line
        print('\t',line)
    print(')\n\n')


def convert_from_sql_table_to_class(lines=None):
    if not lines:
        lines = helper.read_lines()
    if "CREATE" in lines[0]:
        class_name = helper.remove_unused_syntax(lines.pop(0), ["CREATE", "TABLE", "dbo", "FOREIGN", "[", "]", ".", "(", " "])
        print(f'public class {class_name}\n\t')
    for line in lines: 
        line = helper.remove_unused_syntax(line)
        line = handle_types(line, config.types_sql_to_c_type)
        print('\t',line)
        


def handle_types(line, types):
    for type in types.keys():
        if type in line:
            line = line.replace(type, '')
            line = f'[{line}] {types.get(type, type)}'
            return line
    return line

