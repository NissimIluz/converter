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


def to_set():
    lines = read_lines()

    for line in lines:
        name = remove_unused_syntax(line)
        print(f"{name} = {name}")