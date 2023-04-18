from .country import Country
from .city import City
from .validity import validate_case

grid_size = 10

class Map:
    def __init__(self, countries_list):
        self.countries = []
        self.grid      = [ [None] * (grid_size + 2) for i in range((grid_size + 2)) ]
        
        validate_case(countries_list, grid_size)
        
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
        self.countries.sort(key=lambda x: (x.completion_day, x.name))

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