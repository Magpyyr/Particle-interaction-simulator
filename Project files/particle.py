class Particle:

    particle_count = 0

    def __init__(self, name, mass, charge, location):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.location = location
        self.speed = 0
        self.acceleration = 0

    # methods to change the properties of a particle

    def set_name(self, new_name):
        self.name = new_name

    def set_mass(self, new_mass):
        self.mass = new_mass

    def set_charge(self, new_charge):
        self.charge = new_charge

    def set_location(self, new_location):
        self.location = new_location

    # methods to get the properties of a particle

    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def get_charge(self):
        return self.charge

    def get_location(self):
        return self.location

    def get_speed(self):
        return self.speed

