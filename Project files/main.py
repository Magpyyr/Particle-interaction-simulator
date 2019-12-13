# This is Particle Interaction Simulator 0.1 by Pyry Vaara.
# It is a work in progress.

from particle import Particle
from vector import Vector

def create_particle(particles):

    name = input("Start by entering a name for your particle.\n")
    mass = input("Next, enter the mass of {} (kg).\n".format(name))
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
        location_s = "[" + location[0] + " " + location[1] + " " + location[2] + "]"
        print("\tParticle number {:d}, name: {:s}, mass: {:f}, charge: {.f}, location: {".format(i+1,
                                                                                particles[i].get_name,
                                                                                particles[i].get_mass,
                                                                                particles[i].get_charge,
                                                                                location_s))


def main():

    choice = -1
    particles = []


    print("Hello and welcome to Particle Interaction Simulation 0.1.")


    while choice != 5:      # The program operates within this while loop

        if choice == -1:

            print("What would you like to do? Enter your choice as, for example, '1'.\n")
            print("  1. Create a new particle")
            print("  2. Destroy a particle")
            print("  3. Simulate the interaction of existing particles")
            print("  4. Print all particles")
            print("  5. Exit simulation\n")
            choice = int(input())

        elif choice == 1:
            particles = create_particle(particles)
            choice = -1

        elif choice == 2:
            destroy_particle(particles)
            choice = -1

        elif choice == 3:
            simulation(particles)
            choice = -1

        elif choice == 4:
            print_particles(particles)
            choice = -1

        else:
            print("Invalid command, try again!")

    print("\nSimulation terminating...")



main()