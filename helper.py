import config


def remove_unused_syntax(line, unused_syntax=config.g_unused_syntax):
    for s in unused_syntax:
        line = line.replace(s, '')
    return line


def is_attribute_line(line):
    line_without_space = line.replace(" ", "")
    return line_without_space and (line_without_space[0] == '[' or line_without_space[-1] == ']')


def read_lines():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines


def read_lines_with_stop(stop='123!@#'):
    print("To stop enter " + stop)
    lines = []
    while True:
        line = input()
        if line.strip() != stop:
            lines.append(line)
        else:
            break
    return lines


def is_prop_attribute(line):
    for annotation_key in config.annotations.keys():
        if f"[{annotation_key}]" in line:
            return config.annotations[annotation_key]
    return None


def print_array(array):
    for line in array:
        print(line)


def lowercase_to_pascal_case(old_property_name):
    return lowercase_to_pascal_or_camel_case(old_property_name, True)


def lowercase_to_camel_case(old_property_name):
    return lowercase_to_pascal_or_camel_case(old_property_name, False)


def lowercase_to_uppercase(old_property_name:str):
    return old_property_name.replace(" ", "_").upper()


def lowercase_to_pascal_or_camel_case(old_property_name, next_is_big=True):
    property_name = ''
    for letter in old_property_name:
        if letter in ['_']:
            next_is_big = True
        elif letter not in []:
            if next_is_big:
                next_is_big = False
                property_name += letter.upper()
            else:
                property_name += letter
    return property_name


def camel_case_to_lowercase(old_property_name: str):
    property_name = old_property_name[0].lower()
    for letter in old_property_name[1:]:
        if letter.isupper():
            property_name += ('_' + letter.lower())
        else:
            property_name += letter
    return property_name


def convert_name():
    while True:
        name = input()
        print(lowercase_to_pascal_case(name.replace(" ", "").lower()))


def from_class_to_interface():
    lines = read_lines_with_stop()
    for line in lines:
        line = line.strip()
        if line.startswith("public"):
            print(remove_unused_syntax(line, ["public", "{", "async"]) + ";")


def from_class_to_json():
    lines = read_lines_with_stop()
    if 'class' in lines[0]:
        split_line = lines.pop(0).strip().split(" ")
        print(f'"{split_line[2]}" :{{')
    else:
        print("{")
    for line in lines:
        split_line = line.strip().split(" ")
        if len(split_line) > 2:
            property_name = split_line[2]
            property_type = remove_unused_syntax(split_line[1], '?')
            if property_type.startswith('int') or \
                    property_type in ['double', 'bit', 'bool', 'boolean', 'double'] or \
                    property_type.endswith('Enum'):
                default_value = property_type
            elif property_type.startswith('str'):
                default_value = f'"{property_type}"'
            else:
                default_value = '"object"'
            print(f'\t"{property_name}": {default_value},')
    print("}")


def auto_mapper():
    base = "v"
    lines = read_lines()

    for line in lines:
        line = line.strip()
        if line.startswith("public") :
            split_line = line.strip().split(" ")
            property_name = split_line[2]
            print(f"temp.{property_name}={base}.{camel_case_to_lowercase(property_name)}.Value;")



if __name__ == '__main__':
    auto_mapper()