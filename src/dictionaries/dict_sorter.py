def transform() -> dict:
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '23920'),
        ('The Netherlands', '28'),
        ('The US', '61'),
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
        dict_from_tuples[tup[0]] = int(tup[1])

    return dict_from_tuples

def sort_dict(dictionary: dict) -> dict:
    sorted_by_country = dict(sorted(dictionary.items()))
    sorted_by_num = dict(sorted(sorted_by_country.items(), key=lambda item: item[1], reverse=True))
    return sorted_by_num

def print_result(dictionary: dict) -> None:
    for key in dictionary:
        print(key)


if __name__ == "__main__":
    dictionary = transform()
    sorted_dict = sort_dict(dictionary)
    print_result(sorted_dict)
