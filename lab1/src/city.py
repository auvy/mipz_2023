balance_initial        = 1000000
day_one_representative = 1000

class City:
    def __init__(self, homeland, country_list, x, y):
        self.homeland          = homeland
        self.x                 = x
        self.y                 = y

        self.balance           = { city_data["name"]: 0 for city_data in country_list }
        self.balance[homeland] = balance_initial
        
        self.received_today    = { city_data["name"]: 0 for city_data in country_list }
        
        self.neighbors         = []
        self.is_complete       = False
        
    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def add_to_motif(self, motif, amount):
        self.received_today[motif] += amount

    def diffuse_to_neighbors(self):
        for motif in self.balance:
            motif_balance = self.balance[motif]
            daily_tribute = motif_balance // day_one_representative
            
            if daily_tribute > 0:
                for neighbor in self.neighbors:
                    self.balance[motif] -= daily_tribute
                    neighbor.add_to_motif(motif, daily_tribute)

    def today_to_balance(self):
        for motif in self.received_today:
            self.balance[motif] += self.received_today[motif]
            self.received_today[motif] = 0

        if not self.is_complete:
            for motif in self.received_today:
                if self.balance[motif] == 0:
                    return
            self.is_complete = True
