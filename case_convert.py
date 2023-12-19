def convert(type_func):
    print('insert word:')
    word = input()

    result = 'not found'
    if type_func == 'snake_case_to_pascal_case':
        result = snake_case_to_pascal_case(word)
    elif type_func == 'snake_case_to_camel_case':
        result = snake_case_to_camel_case(word)

    elif type_func == 'lowercase_to_uppercase':
        result = lowercase_to_uppercase(word)

    elif type_func == 'camel_case_to_lowercase':
        result = camel_case_to_lowercase(word)

    elif type_func == 'camel_case_to_uppercase':
        result = camel_case_to_lowercase(word).upper()


    print(result)


def snake_case_to_pascal_case(old_property_name):
    return snake_case_to_pascal_or_camel_case(old_property_name, True)


def snake_case_to_camel_case(old_property_name):
    return snake_case_to_pascal_or_camel_case(old_property_name, False)


def lowercase_to_uppercase(old_property_name :str):
    return old_property_name.replace(" ", "_").upper()


def snake_case_to_pascal_or_camel_case(old_property_name, next_is_big=True):
    property_name = ''
    for letter in old_property_name:
        if letter in ['_']:
            next_is_big = True
        elif letter not in []:
            if next_is_big:
                next_is_big = False
                property_name += letter.upper()
            else:
                property_name += letter.lower()
    return property_name


def camel_case_to_lowercase(old_property_name: str):
    property_name = old_property_name[0].lower()
    for letter in old_property_name[1:]:
        if letter.isupper():
            property_name += ('_' + letter.lower())
        else:
            property_name += letter
    return property_name
