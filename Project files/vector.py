class Vector:

    def __init__(self, xyz):
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]

    def set(self, new_xyz):
        self.x = new_xyz[0]
        self.y = new_xyz[1]
        self.z = new_xyz[2]