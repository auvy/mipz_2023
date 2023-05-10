from .country   import Country
from .city      import City

from .config    import grid_size, representative_portion

class Map:
    def __init__(self, countries_list):
        self.countries = []
        self.cities    = []
        self.populate_map(countries_list)


    def populate_map(self, countries_list):
        for country_data in countries_list:
            self.create_country(country_data, countries_list)
        self.grid_determine_neighbors()


    def create_country(self, country_data, countries_list):
        country = Country(country_data["name"])
        
        bounds_x = [country_data["llx"], country_data["urx"] + 1]
        bounds_y = [country_data["lly"], country_data["ury"] + 1]
        
        for x in range(bounds_x[0], bounds_x[1]):
            for y in range(bounds_y[0], bounds_y[1]):
                city = City(country.name, countries_list, x, y)
                country.cities.append(city)
                self.cities.append(city)
                
        self.countries.append(country)


    def grid_determine_neighbors(self):
        for city in self.cities:
            city.neighbors = self.city_determine_neighbors(city.x, city.y)


    def city_determine_neighbors(self, x, y):
        possible_neighbors = [
            [x, y + 1],
            [x, y - 1],
            [x + 1, y],
            [x - 1, y]
        ]
        neighbors = []
        for coords in possible_neighbors:
            for city in self.cities:
                if city.x == coords[0] and city.y == coords[1]:
                    neighbors.append(city)
        
        return neighbors


    def representative_piece(self, money):
        return money // representative_portion


    def diffuse_step(self):
        # every transaction of the day
        transfer_amounts = {}
        for city in self.cities:
            motifs = {}
            for motif, amount in city.balance.items():
                motifs[motif] = self.representative_piece(amount)
            transfer_amounts[(city.x, city.y)] = motifs
        
        # all diffusions per motif
        motifs = [country.name for country in self.countries]
        for motif in motifs:
            for city in self.cities:
                transfer_amount = transfer_amounts[(city.x, city.y)][motif]
                
                for neighbor in city.neighbors:
                    city.balance[motif]     -= transfer_amount
                    neighbor.balance[motif] += transfer_amount
                
                city.check_completion()
                    
    
    def diffuse(self):
        if len(self.countries) < 2:
            country = self.countries[0]
            country.is_complete = True
            country.completion_day = 0            
            return self.countries

        complete = False
        day      = 1
        
        while not complete:
            self.diffuse_step()
            complete = self.map_check_complete(day)

            if complete: 
                break
            
            day += 1
            
        self.countries.sort(key=lambda country: (country.completion_day, country.name))
        
        return self.countries


    def map_check_complete(self, day):
        complete = True
        for country in self.countries:
            if not country.check_completion(day):
                complete = False
        return complete
    
    
    # map print
    def __str__(self):
        import numpy as np
        grid = np.full((grid_size, grid_size), None)    
        for city in self.cities:
            grid[city.x][city.y] = city
        
        result = ''
        rowstr = ''
            
        for row in reversed(np.array(grid).T):
            rowstr = ''
            for cell in row:
                if cell is None:
                    rowstr = rowstr +  " " + '...........'
                else:
                    rowstr = rowstr +  " " + str(cell)
            result = result + rowstr + '\n'
        result = result[:-1]
        
        return result