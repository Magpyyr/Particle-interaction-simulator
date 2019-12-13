class Vector:           # This can be location, speed, force or acceleration

    def __init__(self, xyz):
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]

    def set(self, new_xyz):
        self.x = new_xyz[0]
        self.y = new_xyz[1]
        self.z = new_xyz[2]

    def get_coordinates(self):
        return [self.x, self.y, self.z]


