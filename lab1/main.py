from src.readfile import parse_input
from src.map import Map

input_path             = './data/input.txt'
output_path            = './data/output.txt'

def app():
  case_list = []
  try:
    case_list = parse_input(input_path)
    # for c in case_list:
    #   if not validate_case(c):
    #     print("Input error. Quitting.")
    #     return

  except Exception as e:
    print(e)
  
  try:
    with open(output_path, 'w') as f:

      for i, country_list in enumerate(case_list):
        f.write(f"Case Number {i + 1}\n")
        global_map = Map(country_list)
        
        global_map.diffuse()
        
        countries = global_map.get_countries()

        for country in countries:
          f.write(f'{country.name} {country.completion_day}\n')

  except Exception as e:
    print(e)

app()



