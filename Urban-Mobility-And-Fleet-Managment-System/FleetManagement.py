from vehical import ElectricCar, ElectricScooter

v1 = ElectricCar("CAR001", "Tesla", 80, 5)
v2 = ElectricScooter("SCOOTER001", "OLA", 70, 75)
v3 = ElectricCar("CAR002", "BMW", 80, 5)
v4 = ElectricScooter("SCOOTER002", "Hero", 70, 75)

all_vehicles={"Scooter":[v2,v4],"Car":[v1,v3]}

hubs={"Downtown":[v1,v2],"Airport":[v3,v4]}

def add_hub():
    hub_name = input("Enter hub name: ")
    hubs[hub_name] = []

def add_vehicle():
    vehicle_type = int(input("Enter vehicle type (1-car/2-scooter): "))
    vehicle_id = input("Enter vehicle ID: ")
    for vehi in all_vehicles["Car"]+all_vehicles["Scooter"]:
        if vehi.vehicle_id == vehicle_id:
            print("Vehicle ID already exists")
            return
    model = input("Enter vehicle model: ")
    battery_percentage = int(input("Enter battery percentage: "))
    if vehicle_type == 1:
        seating_capacity = int(input("Enter seating capacity: "))
        all_vehicles["Car"].append(ElectricCar(vehicle_id, model, battery_percentage, seating_capacity))
    elif vehicle_type == 2:
        max_speed_limit = int(input("Enter max speed limit: "))
        all_vehicles["Scooter"].append(ElectricScooter(vehicle_id, model, battery_percentage, max_speed_limit))

def search_vehicle_by_hub():
    hub_name = input("Enter hub name: ")
    if hub_name not in hubs:
        print("Hub not found")
        return
    print(f"Vehicles in {hubs[hub_name]}")

def search_by_battery_status():
    battery_specific_vehicals=filter(lambda v:v.battery_percentage>=80,all_vehicles["Car"]+all_vehicles["Scooter"])
    for vehicle in battery_specific_vehicals:
        print(vehicle)

