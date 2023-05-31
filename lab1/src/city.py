from .config import balance_initial

class City:
    def __init__(self, homeland, country_list, x, y):
        self.homeland          = homeland
        self.x                 = x
        self.y                 = y

        self.balance     = {}
        for country in country_list:
            self.balance[country["name"]]  = 0
        self.balance[homeland] = balance_initial

        self.neighbors         = []
        self.is_complete       = False


    def check_completion(self):
        for amount in self.balance.values():
            if amount == 0:
                return False
        self.is_complete = True
        return True
    
    
     # map print
    def __str__(self):
        return f'{self.homeland[0:4]}({"%2s" % self.x};{"%2s" % self.y})'
        

    