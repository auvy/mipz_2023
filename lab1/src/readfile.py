import re

def read_lines(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
    return data.split('\n')

def parse_country(line):
    args = line.split(' ')
    
    if len(args) != 5:
        raise Exception(f"Error: Need 5 arguments for a country: {args}")
      
    name_pattern = re.compile("[A-Z][a-z]{1,24}$")
    if not name_pattern.match(args[0]):
        raise Exception(f"Error: Invalid country name: '{args[0]}'")
    
    country = {
        "name": args[0],
        "llx": int(args[1]),
        "lly": int(args[2]),
        "urx": int(args[3]),
        "ury": int(args[4])
    }
    return country

def parse_input(input_path):
    lines = read_lines(input_path)

    line_index = 0
    case = 0
    cases = []

    country_amount = 0
    countries = []
    
    while line_index < len(lines):
        line = lines[line_index]
        if line.isdigit():
            # we think it is a case
            
            country_amount = int(line)
            # we trust the input validity
            
            if country_amount == 0:
                # consider 0 an end of cases
                return cases

            countries = []
            line_index += 1

            for c in range(country_amount):
                parsed = parse_country(lines[line_index])
                countries.append(parsed)
                line_index += 1
                
            case += 1
            cases.append(countries)
            countries = []
        else:
            raise Exception("Use numbers only for cases/amount of countries.")
    return cases