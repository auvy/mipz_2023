def validate_case(case, grid_size):  
  check_bounds(case, grid_size)
  check_ll_ur(case)
  if len(case) > 1:
    check_intersection(case)
    check_adjacency(case)


def check_bounds(case, grid_size):
  for country in case:
    coords = list(country.values())
    coords.pop(0)
    for c in coords:
      if int(c) < 0 or int(c) >= (grid_size):
        raise Exception(f'Error: Out of Bounds: "{country["name"]}", {int(c)}, check coordinates.')


def check_ll_ur(case):
  for country in case:
    if country["llx"] > country["urx"] or country["lly"] > country["ury"]:
      raise Exception(f"Error: Invalid coordinates: '{country['name']}' has lower left point's coordinates bigger than upper right's.")


def check_intersection(case):
  # technically this error should never be called but it's here just in case
  if len(case) < 2:
    raise Exception("Error: Minimum of 2 countries needed to check intersection.")  
  indexes = range(len(case))
  pairs = [(a, b) for idx, a in enumerate(indexes) for b in indexes[idx + 1:]]
  for p in pairs:
    intersects = country_intersects(case[p[0]], case[p[1]])
    if intersects:
      raise Exception(f'Error: Intersection: {case[p[0]]["name"]} with {case[p[1]]["name"]}, check coordinates.')

def country_intersects(one, other):
  # intersecting rectangles
  return not (one["urx"] < other["llx"] or one["llx"] > other["urx"] or one["ury"] < other["lly"] or one["lly"] > other["ury"])


def check_adjacency(case):
  cities = []
  for country in case:    
    bounds_x = [country["llx"], country["urx"]]
    bounds_y = [country["lly"], country["ury"]]
      
    bounds_x.sort()
    bounds_y.sort()

    for x in range(bounds_x[0], bounds_x[1] + 1):
        for y in range(bounds_y[0], bounds_y[1] + 1):
          cities.append((x, y))

  for country in case:
    neighbors = False

    bounds_x = [country["llx"], country["urx"]]
    bounds_y = [country["lly"], country["ury"]]
        
    bounds_x.sort()
    bounds_y.sort()
    
    leftmost  = bounds_x[0]
    rightmost = bounds_x[1]
    upper     = bounds_y[1]
    lower     = bounds_y[0]
    
    for x in range(leftmost, rightmost + 1):
    # checking upper line on upper neighbors
      if (x, upper + 1) in cities:
        neighbors = True
    # checking lower line on lower neighbors
      if (x, lower - 1) in cities:
        neighbors = True
    
    for y in range(lower, upper + 1):
    # checking left  line on lefter  neighbors
      if (leftmost - 1, y) in cities:
        neighbors = True
    # checking right line on righter neighbors
      if (rightmost + 1, y) in cities:
        neighbors = True
    
    if not neighbors:
      raise Exception(f'Error: Adjacency: {country["name"]} is isolated, check coordinates')
    
  return True