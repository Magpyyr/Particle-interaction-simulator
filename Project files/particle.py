class Particle:

    particle_count = 0

    def __init__(self, name, mass, charge, location, speed, acceleration):
        self.__name = name
        self.__mass = mass
        self.__charge = charge
        self.__location = location
        self.__speed = speed
        self.__acceleration = acceleration

    # methods to change the properties of a particle

    def set_name(self, new_name):
        self.__name = new_name

    def set_mass(self, new_mass):
        self.__mass = new_mass

    def set_charge(self, new_charge):
        self.__charge = new_charge

    def set_location(self, new_location):
        self.__location = new_location

    def set_speed(self, new_speed):
        self.__speed = new_speed

    def set_acceleration(self, new_acceleration):
        self.__acceleration = new_acceleration

    # methods to get the properties of a particle

    def get_name(self):
        return self.__name

    def get_mass(self):
        return self.__mass

    def get_charge(self):
        return self.__charge

    def get_location(self):
        return self.__location.get_coordinates()

    def get_speed(self):
        return self.__speed.get_coordinates()

    def get_acceleration(self):
        return self.__acceleration.get_coordinates()