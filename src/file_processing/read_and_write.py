def csv_to_tsv(filename: str) -> None:
    with open(f'{filename}.csv', 'r', encoding='utf-8') as csv:
        text = csv.read()
    
    with open(f'{filename}.tsv', 'w', encoding='utf-8') as tsv:

        inside = False
        result = []
        for char in text: 
            if char == '"':
                inside = not inside
            elif char == ',':
                if not inside:
                    char = '\t'
            result.append(char)

        
        tsv.write(''.join(result)) 

if __name__ == '__main__':
    csv_to_tsv('ds')
        