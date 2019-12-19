# This is Particle Interaction Simulator 0.1 by Pyry Vaara.
# It is a work in progress.

from particle import Particle
from vector import Vector
import math


def create_particle(particles):                # ADD A PARTICLE TO THE SIMULATION

    name = input("Start by entering a name for your particle.\n")
    mass = input("Next, enter the mass of {} (u).\n".format(name))
    charge = input("Next, enter its charge (C).\n")
    location_s = input("Finally, enter a location for the particle in the format 'x y z' (m).\n")

    location_s = location_s.rstrip()
    location = location_s.split(" ")
    location[0] = int(location[0])
    location[1] = int(location[1])
    location[2] = int(location[2])
    location = Vector(location)
    speed = Vector([0, 0, 0])
    acceleration = Vector([0, 0, 0])

    new_particle = Particle(name, mass, charge, location, speed, acceleration)
    particles.append(new_particle)
    print("New particle {} created!\n".format(name))

    return particles


def destroy_particle(particles):            # REMOVE A SPECIFIED PARTICLE FROM THE SIMULATION
    pass


def interaction(protagonist, victim):

    protagonist_mass = protagonist.get_mass() * 1.66053904 * 10**(-27)           # unit conversion to SI
    protagonist_charge = protagonist.get_charge() * 1.602176634 * 10**(-19)      # unit conversion to SI
    protagonist_xyz = protagonist.get_location()

    victim_mass = victim.get_mass() * 1.66053904 * 10**(-27)           # unit conversion to SI
    victim_charge = victim.get_charge() * 1.602176634 * 10**(-19)      # unit conversion to SI
    victim_xyz = victim.get_location()

    # CALCULATIONS FOR GRAVITATIONAL INTERACTION
    G = 6.67384 * 10**(-11)                                  # gravitational constant
    distance = math.sqrt( (protagonist_xyz[0]-victim_xyz[0])**2 + (protagonist_xyz[1]-victim_xyz[1])**2
                          + (protagonist_xyz[1]-victim_xyz[1])**2 )

    gravity = G * protagonist_mass * victim_mass / (distance**2)
    DTP = [(protagonist_xyz[0]-victim_xyz[0])/distance,
           (protagonist_xyz[1]-victim_xyz[1])/distance,
           (protagonist_xyz[1]-victim_xyz[1])/distance]     # unit vector pointing to protagonist
    DTV = [-DTP[0], -DTP[1], -DTP[2]]                       # unit vector pointing to victim

    victim_gravity = [DTP[0] * gravity, DTP[1] * gravity, DTP[2] * gravity]
    protagonist_gravity = [DTV[0] * gravity, DTV[1] * gravity, DTV[2] * gravity]

    # CALCULATIONS FOR ELECTRIC INTERACTION
    ke = 8.98755 * 10**9
    coulomb_force = ke * protagonist_charge * victim_charge / (distance**2)

    protagonist_coulomb = [DTP[0] * coulomb_force, DTP[1] * coulomb_force, DTP[2] * coulomb_force]
    victim_coulomb = [DTV[0] * coulomb_force, DTV[1] * coulomb_force, DTV[2] * coulomb_force]
    protagonist_force = [protagonist_gravity[0]+protagonist_coulomb[0], protagonist_gravity[1]+protagonist_coulomb[1],
                         protagonist_gravity[2]+protagonist_coulomb[2]]
    victim_force = [victim_gravity[0]+victim_coulomb[0], victim_gravity[1]+victim_coulomb[1],
                    victim_gravity[2]+victim_coulomb[2]]

    # CALCULATE ACCELERATIONS FOR BOTH PARTICLES
    protagonist_acc = protagonist.get_acceleration()
    protagonist_new_acc = [protagonist_acc[0] + protagonist_force[0] / protagonist_mass, 
                           protagonist_acc[1] + protagonist_force[1] / protagonist_mass,
                           protagonist_acc[2] + protagonist_force[2] / protagonist_mass]
    protagonist_new_acc = Vector(protagonist_new_acc)
    protagonist.set_acceleration(protagonist_new_acc)

    victim_acc = victim.get_acceleration()
    victim_new_acc = [victim_acc[0] + victim_force[0] / victim_mass, victim_acc[1] + victim_force[1] / victim_mass,
                      victim_acc[2] + victim_force[2] / victim_mass]
    victim_new_acc = Vector(victim_new_acc)
    victim.set_acceleration(victim_new_acc)


def move_particles(particles):

    for p in range(len(particles)):
        A = particles[p]
        A_location = A.get_location()
        A_speed = A.get_speed()
        A_acc = A.get_acceleration()

        # CHANGE THE LOCATIONS OF ALL PARTICLES ACCORDING TO THEIR SPEED
        new_x = A_location[0] + A_speed[0] * 0.001
        new_y = A_location[1] + A_speed[1] * 0.001
        new_z = A_location[2] + A_speed[2] * 0.001
        new_xyz = Vector([new_x, new_y, new_z])
        A.set_location(new_xyz)

        # CHANGE THE SPEED OF ALL PARTICLES ACCORDING TO THEIR ACCELERATION
        new_speed_x = A_speed[0] + A_acc[0] * 0.001
        new_speed_y = A_speed[1] + A_acc[1] * 0.001
        new_speed_z = A_speed[2] + A_acc[2] * 0.001
        new_speed_xyz = Vector([new_speed_x, new_speed_y, new_speed_z])
        A.set_speed(new_speed_xyz)
        
        # SET THE ACCELERATION FOR EVERY PARTICLE TO ZERO
        zero = Vector([0, 0, 0])
        A.set_acceleration(zero)


def simulation(particles):                  # time frame for the simulation

    TIME = int(input("Enter the amount of time you want to simulate in ms.\n"))

    for t in range(TIME):              # Everything is calculated once every millisecond

        totalP = len(particles)
        move_particles(particles)
        for a in range(totalP):
            protagonist = particles[a]

            for b in range(a, totalP):
                victim = particles[b]
                interaction(protagonist, victim)


def print_particles(particles):             # PRINT A LIST OF ALL THE PARTICLES IN THE SIMULATION

    print("Printing a list of all particles...\n")
    for i in range(len(particles)):
        location = particles[i].get_location()
        location_s = "[" + str(location[0]) + " " + str(location[1]) + " " + str(location[2]) + "]"

        name = particles[i].get_name()
        mass = particles[i].get_mass()
        charge = particles[i].get_charge()
        print("\tParticle number {}, name: {}, mass: {}u, charge: {}e, location: {}".format(i+1,
                                                                                     name,
                                                                                     mass,
                                                                                     charge,
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

        speed = Vector([0, 0, 0])
        acceleration = Vector([0, 0, 0])
        new_particle = Particle(name, mass, charge, location, speed, acceleration)
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