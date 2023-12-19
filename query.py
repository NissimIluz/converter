from helper import read_lines, print_array, remove_unused_syntax


def insert_where():
    query_lines = read_lines()
    index = 0
    while query_lines[index].strip().startswith('-- @'):
        # print(query_lines[index])
        [key, value] = query_lines[index].strip().split('=')[:2]
        key = remove_unused_syntax(key, '--').strip()
        value = remove_unused_syntax(value, [' (DbType']).strip()
        index += 1
        for j in range(index, len(query_lines)):
            query_lines[j] = query_lines[j].replace(key, value)

    print_array(query_lines)

