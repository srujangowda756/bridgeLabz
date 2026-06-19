from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        self.__maintenance_status = "Available"
    
    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def set_maintenance_status(self,status):
        self.__maintenance_status = status
    
    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}, Model: {self.model}, Battery: {self.battery_percentage}%"
    
    def __eq__(self,other):
        return self.vehicle_id == other.vehicle_id
    
    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass

class ElectricCar(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity):
        super().__init__(vehicle_id,model,battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        cost=5+(distance*0.5)
        return f"Cost for {distance} km: ${cost}"


class ElectricScooter(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,max_speed_limit):
        super().__init__(vehicle_id,model,battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, distance):
        cost=1+(0.15*distance)
        return f"Cost for {distance} km: ${cost}"

