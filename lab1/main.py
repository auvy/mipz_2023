from src.readfile import parse_input
from src.validity import validate_case

from src.config   import grid_size, input_path, output_path

from src.map      import Map


def app():
  case_list = []
  try:
    case_list = parse_input(input_path)
    for i, case in enumerate(case_list):
      print(f"Checking case {i}")
      validate_case(case, grid_size)
    print("Cases are valid")
  except Exception as e:
    print(e)
    return
    
  try:
    with open(output_path, 'w') as f:

      for i, country_list in enumerate(case_list):
        f.write(f"Case Number {i + 1}\n")
        print(f'\ncase {i}')
        
        global_map = Map(country_list)
        print(global_map)
                
        countries = global_map.diffuse()

        for country in countries:
          f.write(f'{country.name} {country.completion_day}\n')
          print(f'{country.name} {country.completion_day}')
          
  except Exception as e:
    print(e)
    return


app()