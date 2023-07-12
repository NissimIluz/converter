import config
import helper



def convert_from_array():
    text = input("enter:")
    text_array = text.split(',')
    for index in range(len(text_array)):
        text_array[index] = ''.join([i for i in text_array[index] if i.isalpha()])
        text_array[index] = convert_first_latter_to_lower(text_array[index])
    print(text_array)


def convert_from_class():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    for index in range(len(lines)):
        line = helper.remove_unused_syntax(lines[index])
        line = handle_types(line, config.types_c_to_ts)

        line = ''.join([i for i in line if i.isalpha()])
        lines[index] = convert_first_latter_to_lower(line)
    print(lines)


def convert_from_class_to_ts_interface(lines=None):
    if not lines:
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break

    if 'class' in lines[0]:
        line = helper.remove_unused_syntax(lines[0])
        line = line.replace('class', '')
        line = ''.join([i for i in line if i.isalpha()])
        print(f'export interface {line} ' + '{')
        lines.pop(0)
    else:
        print('export interface name{')

    for index in range(len(lines)):
        line = helper.remove_unused_syntax(lines[index])
        if helper.is_attribute_line(line):
            continue
        line = ''.join([i for i in line if i.isalpha()])
        line = handle_types(line, config.types_c_to_ts, True)
        if not line : continue
        line = convert_first_latter_to_lower(line)
        lines[index] = line
        print('\t', line)
    print('}\n\n')
    print(lines)


def convert_from_class_to_string_array(lines=None):
    if not lines:
        lines = helper.read_lines()
    for index in range(len(lines)):
        line = helper.remove_unused_syntax(lines[index])
        line = ''.join([i for i in line if i.isalpha()])
        line = handle_types(line, config.types_c_to_ts)
        line = convert_first_latter_to_lower(line)
        lines[index] = line
        print(line)
    print(lines)


def convert_first_latter_to_lower(name):
    name = name[0].lower() + name[1:]
    return name


def handle_types(line, types, insert_new_ts_type=False):
    for type in types.keys():
        if type in line:
            line = line.replace(type, '')
            if insert_new_ts_type:
                line = line + ': ' + types.get(type, type) + ";"
            return line
    return line


def temp():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
        line = line.replace(',', '').replace(' ', '')
        print('a1.' + line.replace(' ', '') + '!=' + 'a2.' + line + ' or')


