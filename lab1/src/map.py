from .country import Country
from .city import City

grid_size = 10

class Map:
    def __init__(self, countries_list):
        self.countries = []
        self.grid      = [ [None] * (grid_size + 2) for i in range((grid_size + 2)) ]
        
        validate_case(countries_list)
        
        self.__grid_init(countries_list)
        self.__check_neighbors_countries()

    # class-private
    def __grid_init(self, countries_list):
        # go through every country and put it's cities on the grid
        for country_data in countries_list:
            
            country = Country(country_data["name"])
            
            for x in range(country_data["llx"], country_data["urx"] + 1):
               # we iterate by columns downwards and right basically. 
                for y in range(country_data["lly"], country_data["ury"] + 1):
                    if self.grid[x][y] is not None:
                        raise Exception(f"{self.grid[x][y].country_name} intersects with {country.name} in [{x}, {y}]")
                    
                    # city defines each coin denom
                    city = City(country.name, countries_list, x, y)
                    self.grid[x][y] = city
                    # add this city to country
                    country.append_city(city)
            self.countries.append(country)

        # set neighbors for each city
        for row in self.grid:
            for city in row:
                if city is not None:
                    neighbors_list = self.__get_neighbors(city.x, city.y)
                    city.set_neighbors(neighbors_list)

    def diffuse(self):
        if len(self.countries) == 1:
            country = self.countries[0]
            country.toggle_complete()
            return

        full = False
        day = 1
        while not full:
            for x in range(grid_size + 1):
                for y in range(grid_size + 1):
                    if self.grid[x][y] is not None:
                        city = self.grid[x][y]
                        city.diffuse_to_neighbors()

            for x in range(grid_size + 1):
                for y in range(grid_size + 1):
                    if self.grid[x][y] is not None:
                        city = self.grid[x][y]
                        city.today_to_balance()

            full = True
            for country in self.countries:
                country.check_completion(day)
                if country.is_complete is False:
                    full = False

            # if not full:
            day += 1

        # self.countries.sort()
        self.countries.sort(key=lambda x: x.completion_day, reverse=False)

    def get_countries(self):
        return self.countries

    # class-private
    def __get_neighbors(self, x, y):
        neighbors = []
        if self.grid[x][y + 1] is not None:
            neighbors.append(self.grid[x][y + 1])
        if self.grid[x][y - 1] is not None:
            neighbors.append(self.grid[x][y - 1])
        if self.grid[x + 1][y] is not None:
            neighbors.append(self.grid[x + 1][y])
        if self.grid[x - 1][y] is not None:
            neighbors.append(self.grid[x - 1][y])
        return neighbors

    # class-private
    def __check_neighbors_countries(self):
        if len(self.countries) < 2:
            return
        for country in self.countries:
            if not country.has_foreign_neighbors():
                raise Exception(f"{country.name} has no connection with other countries")


# not class methods but needed to check validity only
def country_intersects(self, other):
    return not (self["urx"] < other["llx"] or self["llx"] > other["urx"] or self["ury"] < other["lly"] or self["lly"] > other["ury"])

def check_bounds(case):
  if len(case) < 2:
    raise Exception("Error: Minimum of 2 countries needed to check intersection.")
  indexes = range(len(case))
  pairs = [(a, b) for idx, a in enumerate(indexes) for b in indexes[idx + 1:]]
  
  for p in pairs:
    intersect = country_intersects(case[p[0]], case[p[1]])
    if intersect:
      raise Exception(f'Error: {case[p[0]]["name"]} and {case[p[1]]["name"]} intersect.')

def validate_case(case):  
  for country in case:
    coords = list(country.values())
    coords.pop(0)
    for c in coords:
      if int(c) <= 0 or int(c) >= (grid_size + 1):
        raise Exception(f'Error: Country "{country["name"]}" coordinates out of bounds.')
  
  if len(case) > 1:
    check_bounds(case)
  
