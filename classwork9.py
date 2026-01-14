class vechile:
    def __init__(self,vechile_id,base_rate):
        self._vehicle_id= vechile_id
        self._base_rate=float(base_rate)

    def display_details(self):   
         return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate:.2f}"
    def rental_charge(self):
        return 0.0
    
    class car(vechile):
     def __init__(self, vechile_id, base_rate,num_seats):
        super().__init__(vechile_id, base_rate)   
        self.num_seats = int(num_seats)
        
