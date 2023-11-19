import case_convert
import helper


def from_class_to_interface():
    lines = helper.read_lines_with_stop()
    for line in lines:
        line = line.strip()
        if line.startswith("public"):
            print(helper.remove_unused_syntax(line, ["public", "{", "async"]) + ";")


def from_class_to_json():
    lines = helper.read_lines_with_stop()
    if 'class' in lines[0]:
        split_line = lines.pop(0).strip().split(" ")
        print(f'"{split_line[2]}" :{{')
    else:
        print("{")
    for line in lines:
        split_line = line.strip().split(" ")
        if len(split_line) > 2:
            property_name = split_line[2]
            property_type = helper.remove_unused_syntax(split_line[1], '?')
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


def auto_mapper_1():
    print("set from:")
    from_base = input()

    print("set to:")
    to = input()

    lines = helper.read_lines()

    for line in lines:
        line = line.strip()
        if line.startswith("public") :
            split_line = line.strip().split(" ")
            property_name = split_line[2]
            print(f"{to}.{property_name}={from_base}.{case_convert.camel_case_to_lowercase(property_name)};")


def auto_mapper_2():
    print("set from:")
    from_base = input()

    lines = helper.read_lines_with_stop('123')

    for line in lines:
        line = line.strip()
        if line.startswith("public"):
            split_line = line.strip().split(" ")
            property_name = split_line[2]
            print(f"{property_name}={from_base}.{property_name},")


if __name__ == '__main__':
    auto_mapper_2()