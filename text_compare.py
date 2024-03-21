import helper


def find_differences():
    source_class = helper.read_lines_with_stop('source_class', 'source_class')
    comparison_class = helper.read_lines_with_stop('comparison_class', 'comparison_class')
    for line in source_class:
        if line not in comparison_class:
            print(line)