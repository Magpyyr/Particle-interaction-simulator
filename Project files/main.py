# This is Particle Interaction Simulator 0.1 by Pyry Vaara.
# It is a work in progress.

from particle import Particle
from vector import Vector

def create_particle(particles):

    name = input("Start by entering a name for your particle.\n")
    mass = input("Next, enter the mass of {} (u).\n".format(name))
    charge = input("Next, enter its charge (C).\n")
    location_s = input("Finally, enter a location for the particle in the format 'x y z' (m).\n")

    location_s = location_s.rstrip()
    location = location_s.split( )
    location[0] = int(location[0])
    location[1] = int(location[1])
    location[2] = int(location[2])
    location = Vector(location)

    new_particle = Particle(name, mass, charge, location)
    particles.append(new_particle)
    print("New particle {} created!\n".format(name))

    return particles


def destroy_particle(particles):
    pass

def simulation(particles):
    pass

def print_particles(particles):

    print("Printing a list of all particles...\n")
    for i in range(len(particles)):
        location = particles[i].get_location
        location = location.get_coordinates
        location_s = "[" + str(location[0]) + " " + str(location[1]) + " " + str(location[2]) + "]"
        print("\tParticle number {:d}, name: {:s}, mass: {:f}, charge: {.f}, location: {".format(i+1,
                                                                                particles[i].get_name,
                                                                                particles[i].get_mass,
                                                                                particles[i].get_charge,
                                                                                location_s))
        print("\nList complete, the simulation contains {:d} particles.\n".format(i+1))


def load_particles(particles):

    file = open("test_particles.txt", "r")
    counter = 0

    for line in file:
        sline = line.rstrip()
        sline = sline.split(" ")

        if len(sline) != 6:
            pass

        name = sline[0]
        mass = sline[1]
        charge = sline[2]

        location = []
        location.append(int(sline[3]))
        location.append(int(sline[4]))
        location.append(int(sline[5]))


        location = Vector(location)
        new_particle = Particle(name, mass, charge, location)
        particles.append(new_particle)
        counter += 1

    print("{:d} particles loaded.\n".format(counter))

    file.close()
    return particles

def main():

    choice = -1
    particles = []


    print("Hello and welcome to Particle Interaction Simulation 0.1.")


    while choice != 6:      # The program operates within this while loop

        if choice == -1:

            print("What would you like to do? Enter your choice as, for example, '1'.\n")
            print("  1. Create a new particle")
            print("  2. Load particles from a file")
            print("  3. Destroy a particle")
            print("  4. Simulate the interaction of existing particles")
            print("  5. Print all particles")
            print("  6. Exit simulation\n")
            choice = int(input())

        elif choice == 1:
            particles = create_particle(particles)
            choice = -1

        elif choice == 2:
            particles = load_particles(particles)
            choice = -1

        elif choice == 3:
            destroy_particle(particles)
            choice = -1

        elif choice == 4:
            simulation(particles)
            choice = -1

        elif choice == 5:
            print_particles(particles)
            choice = -1

        else:
            print("Invalid command, try again!")

    print("\nSimulation terminating...")



main()