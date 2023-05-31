class Country:
    def __init__(self, name):
        self.name           = name
        self.is_complete    = False
        self.completion_day = -1
        self.cities         = []


    def check_completion(self, day):
        if self.is_complete:
            return True
        for city in self.cities:
            if city.is_complete is False:
                return False
        self.is_complete = True
        self.completion_day = day
        return True
