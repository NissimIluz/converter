from helper import read_lines


class Config:
    type = int
    start_with = "('"
    end_with = "')"
    separator = "','"


class SqlIntConfig(Config):
    type = int
    start_with = "("
    end_with = ")"
    separator = ","


if __name__ == '__main__':
    config: Config = SqlIntConfig()
    lines = read_lines()
    result = config.start_with
    for line in lines:
        if line:
            result += (line + config.separator)
    result = result[:-len(config.separator)]
    result += config.end_with
    print(result)
