from vehical import ElectricCar, ElectricScooter

all_vehicles={"Scooter":[],"Car":[]}

hubs={"Downtown":[],"Airport":[]}

def add_hub():
    hub_name = input("Enter hub name: ")
    hubs[hub_name] = []

def add_vehicle():
    vehicle_type = int(input("Enter vehicle type (1-car/2-scooter): "))
    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        return
    vehicle_id = input("Enter vehicle ID: ")
    for vehi in all_vehicles["Car"]+all_vehicles["Scooter"]:
        if vehi.vehicle_id == vehicle_id:
            print("Vehicle ID already exists")
            return
    model = input("Enter vehicle model: ")
    hub_name = input("Enter hub name: ")
    battery_percentage = int(input("Enter battery percentage: "))
    if vehicle_type == 1:
        seating_capacity = int(input("Enter seating capacity: "))
        new_v = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity)
        all_vehicles["Car"].append(new_v)
    elif vehicle_type == 2:
        max_speed_limit = int(input("Enter max speed limit: "))
        new_v = ElectricScooter(vehicle_id, model, battery_percentage, max_speed_limit)
        all_vehicles["Scooter"].append(new_v)
    if hub_name in hubs:
        hubs[hub_name].append(new_v)
    else:
        print("Hub not found")
        return

    # with open(r"C:\Users\ADMIN\Downloads\BridgeLab\bridgeLabz\Urban-Mobility-And-Fleet-Managment-System\data.csv","a") as f:
    #     f.write(f"{vehicle_id},{model},{battery_percentage},{seating_capacity if vehicle_type == 1 else max_speed_limit},{vehicle_type},{hub_name}\n")

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

def sort_by_name():
    sorted_vehicles_by_name=sorted(all_vehicles["Car"]+all_vehicles["Scooter"],key=lambda v:v.vehicle_id)
    for vehicle in sorted_vehicles_by_name:
        print(vehicle)

def advance_sorting():
    sorted_vehicles_by_battery=sorted(all_vehicles["Car"]+all_vehicles["Scooter"],key=lambda v:v.battery_percentage)
    for vehicle in sorted_vehicles_by_battery:
        print(vehicle)

import csv

def save_to_csv(filenameCSV):

    with open(filenameCSV, "w", newline="") as file:


        writer = csv.writer(file)
        writer.writerow(["vehicle_type", "vehicle_id", "model", "battery_percentage", "extra", "status"])
        for vehicle in all_vehicles["Car"]:
            writer.writerow(["Car",
                vehicle.vehicle_id,
                vehicle.model,vehicle.battery_percentage,
                vehicle.seating_capacity,
                vehicle.get_maintenance_status()])

        for vehicle in all_vehicles["Scooter"]:

            writer.writerow(["Scooter",
                vehicle.vehicle_id,
                vehicle.model,
                vehicle.battery_percentage,
                vehicle.max_speed_limit,
                vehicle.get_maintenance_status()
            ])


def load_from_csv(filenameCSV):

    with open(filenameCSV, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["vehicle_type"] == "Car":

                car = ElectricCar(
                    row["vehicle_id"],
                    row["model"],
                    int(row["battery_percentage"]),
                    int(row["extra"])
                )

                car.set_maintenance_status(row["status"])

                all_vehicles["Car"].append(car)

            else:

                scooter = ElectricScooter(
                    row["vehicle_id"],
                    row["model"],
                    int(row["battery_percentage"]),
                    int(row["extra"])
                )

                scooter.set_maintenance_status(row["status"])

                all_vehicles["Scooter"].append(scooter)


import json

def save_to_json(filenameJSON):

    data = {}

    for hub_name, vehicles in hubs.items():

        data[hub_name] = []

        for vehicle in vehicles:

            if isinstance(vehicle, ElectricCar):

                data[hub_name].append({
                    "type": "Car",
                    "vehicle_id": vehicle.vehicle_id,
                    "model": vehicle.model,
                    "battery": vehicle.battery_percentage,
                    "seating_capacity": vehicle.seating_capacity,
                    "status": vehicle.get_maintenance_status()
                })

            else:

                data[hub_name].append({
                    "type": "Scooter",
                    "vehicle_id": vehicle.vehicle_id,
                    "model": vehicle.model,
                    "battery": vehicle.battery_percentage,
                    "max_speed_limit": vehicle.max_speed_limit,
                    "status": vehicle.get_maintenance_status()
                })

    with open(filenameJSON  , "w") as file:
        json.dump(data, file, indent=4)

import json

def load_from_json(filenameJSON):

    with open(filenameJSON  , "r") as file:

        data = json.load(file)

    hubs.clear()

    for hub_name, vehicles in data.items():

        hubs[hub_name] = []

        for v in vehicles:

            if v["type"] == "Car":

                vehicle = ElectricCar(
                    v["vehicle_id"],
                    v["model"],
                    v["battery"],
                    v["seating_capacity"]
                )

            else:

                vehicle = ElectricScooter(
                    v["vehicle_id"],
                    v["model"],
                    v["battery"],
                    v["max_speed_limit"]
                )

            vehicle.set_maintenance_status(v["status"])

            hubs[hub_name].append(vehicle)


# add_vehicle()
# add_vehicle()

filenameJSON = "data.json" 
load_from_json(filenameJSON)
save_to_json(filenameJSON)

filenameCSV = "data.csv"
load_from_csv(filenameCSV)
save_to_csv(filenameCSV)
print(hubs)