def parse_country(line):
    tokens = line.split()

    if len(tokens) != 5:
        raise Exception(f"Error: Need 5 arguments for a country: {tokens}")

    country = {
        "name": tokens[0],
        "llx" : int(tokens[1]),
        "lly" : int(tokens[2]),
        "urx" : int(tokens[3]),
        "ury" : int(tokens[4])
    }

    return country


def read_lines(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
    return data.split('\n')


def parse_input(input_path):
    lines = read_lines(input_path)

    cases = []
    current_case = []

    countries_n = -1
    
    for l in lines:
        tokens = l.strip().split()
                
        if len(tokens) > 0:
                
            # case number line
            if  len(tokens) < 2 and \
                tokens[0].isdigit() :
                    
                # number of countries
                countries_n = int(tokens[0])
                
                # append accumulated countries in case
                # and move on
                if len(current_case) > 0:
                    cases.append(current_case)
                    current_case = []
                
                # line '0' that ends reading
                if int(tokens[0]) == 0:
                    break
                
            # country line      
            elif len(tokens) == 5 and            \
                 len(current_case) < countries_n :
                # implicitly ignore country
                # if case array has enough
                country = parse_country(l)
                current_case.append(country)
            
            else:
                continue
    
    return cases
