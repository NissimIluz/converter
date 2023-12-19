from helper import read_lines_with_stop


def extract_from_line_with_input():
    from_str = input("from: ")
    to_str = input("to: ")
    print("rows: \n")
    lines = read_lines_with_stop()
    extract_from_line(lines, from_str, to_str)


def extract_from_line(lines, from_str, to_str):
    for line in lines:
        line = line.strip()
        if from_str in line:
            from_index = line.index(from_str)
            to_index = line[from_index:].index(to_str) + len(to_str)

            print(line[from_index:to_index])

