from case_convert import camel_case_to_lowercase, word_to_camel_case


def to_url():
    print('insert word:')
    word = input()
    word = word.replace('_', '-')
    word = word.lower()
    print(word)


def to_url_function():
    print('insert word:')

    name = input()
    name = word_to_camel_case(name)
    print(f'get {name}Url() {{\n\t'
          f'return getFullUrl(EDUCATION_PLACES.BASE, EDUCATION_PLACES.{camel_case_to_lowercase(name).upper()});'
          f" // {camel_case_to_lowercase(name).upper()}: \'{name}\',"
          f'\n}}')


if __name__ == '__main__':
    to_url_function()