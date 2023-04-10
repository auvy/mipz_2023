class Country:
    def __init__(self, name):
        self.name           = name
        self.is_complete    = False
        self.completion_day = -1
        self.cities         = []

    def append_city(self, city):
        self.cities.append(city)

    def check_completion(self, day):
        if self.is_complete:
            return
        for city in self.cities:
            if city.is_complete is False:
                return
        self.is_complete = True
        self.completion_day = day

    def has_foreign_neighbors(self):
        for city in self.cities:
            for neighbor in city.neighbors:
                if neighbor.homeland != self.name:
                    return True
    
    def toggle_complete(self):
        self.is_complete = True
        self.completion_day = 0
