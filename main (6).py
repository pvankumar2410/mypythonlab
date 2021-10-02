# Parent
class vehicle:
    def __init__(self, make, model, color, fuel_type, options, vehicle_name):
        self._make = make
        self._model = model
        self._color = color
        self._fuel_type = fuel_type
        self._options = options
        self._vehicle_name = vehicle_name

    @classmethod
    def get_make(self):
        make = input('\nWhat is the make of the vehicle?: ')
        return make

    @classmethod
    def get_model(self):
        model = input('\nWhat is the model of the vehicle?: ')
        return model

    @classmethod
    def get_color(self):
        color = input('\nWhat is the color of the vehicle?: ')
        return color

    @classmethod
    def fuel_type(self):
        fuel = input('\nWhat fuel type will the vehicle use?: ')
        return fuel

    @classmethod
    def get_options(self):
        print('\nBelow are additional options for you to add to your vehicle: ')
        options_list = {1: 'power mirrors', 2: 'power locks', 3: 'remote start', 4: 'backup camera', 5: 'bluetooth',
                        6: 'cruise control', 7: 'satellite radio', 8: 'smart drive'}
        for key, value in options_list.items():
            print(key, ':', value)

        num_options = int(input('How many of these options would you like to select?: '))
        choices = {}
        n = 0
        while n < num_options:
            choice = int(input('Please select one of the numbers that corresponds to the option you wish to add: '))
            try:
                choices[n] = options_list[choice]
                n += 1
            except:
                print('Please enter a number 1 - 8.')

        options = ", ".join(choices.values())
        return options

    @classmethod
    def vehicle_name(self):
        vehicle_name = input('\nPlease name your new vehicle. (ex: Red Lightning or Car 1): ')
        return vehicle_name


# Inheritance
class car(vehicle):
    def __init__(self, engine_size, num_doors, make, model, color, fuel_type, options, vehicle_name):
        super().__init__(make, model, color, fuel_type, options, vehicle_name)
        self.get_engine_size = engine_size
        self.get_num_doors = num_doors

    @classmethod
    def get_engine_size(self):
        engine_size = input("\nWhat will be the car's the engine size?: ")
        return engine_size

    @classmethod
    def get_num_doors(self):
        num_doors = input('\nHow many doors will the car have? ')
        return num_doors


class pickup(vehicle):
    def __init__(self, cab_style, bed_length, make, model, color, fuel_type, options, vehicle_name):
        super().__init__(make, model, color, fuel_type, options, vehicle_name)
        self.get_cab_style = cab_style
        self.get_bed_length = bed_length

    @classmethod
    def get_cab_style(self):
        cab_style = input("\nWhat will be the pickup's cab style?: ")
        return cab_style

    @classmethod
    def get_bed_length(self):
        bed_length = input("\nWhat will be the pickup's bed length?: ")
        return bed_length

# vehicle builder
def build_car():
    make = vehicle.get_make()
    model = vehicle.get_model()
    color = vehicle.get_color()
    fuel_type = vehicle.fuel_type()
    engine_size = car.get_engine_size()
    num_door = car.get_num_doors()
    options = vehicle.get_options()
    vehicle_name = vehicle.vehicle_name()

    new_vehicle = {'name': vehicle_name, 'make': make, 'model': model, 'color': color, 'fuel type': fuel_type,
               'engine size': engine_size, 'num door': num_door, 'options': options}
    return new_vehicle

def build_pickup():
    make = vehicle.get_make()
    model = vehicle.get_model()
    color = vehicle.get_color()
    fuel_type = vehicle.fuel_type()
    cab_style = pickup.get_cab_style()
    get_bed_length = pickup.get_bed_length()
    options = vehicle.get_options()
    vehicle_name = vehicle.vehicle_name()

    new_vehicle = {'name': vehicle_name, 'make': make, 'model': model, 'color': color, 'fuel type': fuel_type,
                   'cab style': cab_style, 'bed length': get_bed_length, 'options': options}
    return new_vehicle

# Main function
if __name__ == '__main__':
    garage = []
    message = ''
    while message != 'quit':
        print('''#### Welcome to the virtual garage builder! ####'
    How may we help you today?
        1) Build new vehicle
        2) Show me all my vehicles
        3) Quit''')
        value = (int(input('\nEnter menu number: ')))
        if value == 1:
            print('''Which vehicle would you like to build first?
        1) Car
        2) Pickup''')
            value = (int(input('\nEnter menu number: ')))

            if value == 1:
                new_vehicle = build_car()
                garage.append(new_vehicle)
                print('\nYour new car has been added to your virtual garage!\n')

            else:
                new_vehicle = build_pickup()
                garage.append(new_vehicle)
                print('\nYour new pickup has been added to your virtual garage!\n')

        elif value == 3:
            print('Have a nice day!')
            break

        else:
            print('\nHere are the vehicles you built:\n')
            for item in garage:
                for key, value in item.items():
                    print(key, ':', value)
                print('\n-----')