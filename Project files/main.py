# This is Particle Interaction Simulator 0.1 by Pyry Vaara.
# It is a work in progress.

def create_particle(particles):

    name = input("Start by entering a name for your particle.\n")
    mass = input("Next, enter the mass of {}.\n".format(name))
    charge = input("Next, enter its charge.\n".)
    location_s = input("Finally, enter a location for the particle.\n")


def destroy_particle(particles):
    pass

def simulation(particles):
    pass


def main():

    choice = -1
    particles = []


    print("Hello and welcome to Particle Interaction Simulation 0.1.")


    while choice != 4:      # The simulation program within this while loop

        if choice == -1:

            print("What would you like to do? Enter your choice as, for example, "1".\n")
            print("  1. Create a new particle")
            print("  2. Destroy a particle")
            print("  3. Simulate the interaction of existing particles")
            print("  4. Exit simulation\n")
            choice = int(input())

        elif choice == 1:
            create_particle(particles)
            choice = -1

        elif choice == 2:
            destroy_particle(particles)
            choice = -1

        elif choice == 3:
            simulation(particles)
            choice = -1






main()