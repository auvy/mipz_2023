def country_intersects(one, other):
    return not (one["urx"] < other["llx"] or one["llx"] > other["urx"] or one["ury"] < other["lly"] or one["lly"] > other["ury"])

def check_bounds(case):
  if len(case) < 2:
    raise Exception("Error: Minimum of 2 countries needed to check intersection.")
  indexes = range(len(case))
  pairs = [(a, b) for idx, a in enumerate(indexes) for b in indexes[idx + 1:]]
  
  for p in pairs:
    intersect = country_intersects(case[p[0]], case[p[1]])
    if intersect:
      raise Exception(f'Error: {case[p[0]]["name"]} and {case[p[1]]["name"]} intersect.')

def validate_case(case, grid_size):  
  for country in case:
    coords = list(country.values())
    coords.pop(0)
    for c in coords:
      if int(c) <= 0 or int(c) >= (grid_size + 1):
        raise Exception(f'Error: Country "{country["name"]}" coordinates out of bounds.')
  
  if len(case) > 1:
    check_bounds(case)
  