import sys

def get_correct(expressions: str) -> list:
    list_expr = expressions.split(',')

    res_list = list()

    for word in list_expr:
        res_word = word.replace(' ', '').lower()
        res_list.append(res_word)

    return res_list

def check_dicts(corrects: list) -> None:
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    for word in corrects:
        company = word.capitalize()
        ticker = word.upper()
        if company in COMPANIES:
            print(f'{company} stock price is {STOCKS[COMPANIES[company]]}')
        elif ticker in STOCKS:
            for k, v in COMPANIES.items():
                if v == ticker:
                    name = k
                    break
            print(f'{ticker} is a ticker symbol for {name}')
        else:
            print(f'{word} is an unknown company or an unknown ticker symbol')



if __name__ == "__main__":
    if len(sys.argv) == 2:
        words = get_correct(sys.argv[1])
        if '' not in words:
            check_dicts(words)
