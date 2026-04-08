def transform() -> dict:
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]
    dict_from_tuples = dict()

    for tup in list_of_tuples:
        dict_from_tuples[tup[1]] = list()
    for tup in list_of_tuples:
        dict_from_tuples[tup[1]].append(tup[0])

    return dict_from_tuples

def print_result(dictionary: dict) -> None:
    for key in dictionary:
        for value in dictionary[key]:
            print(f"'{key}' : '{value}'")


if __name__ == "__main__":
    dictionary = transform()
    #print(dictionary)
    print_result(dictionary)
