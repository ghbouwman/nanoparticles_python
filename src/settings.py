from numpy import pi as PI
from numpy import sqrt
hex = lambda n: 3*n**2 - 3*n+ 1

# All numbers are in SI unless mentioned otherwise

# Physical constants:
ELEMENTARY_CHARGE = 1.6e-19
PLANCK_CONSTANT = 6.626e-34
HBAR = PLANCK_CONSTANT / (2*PI)
CONDUCTANCE_QUANTUM = 2*ELEMENTARY_CHARGE**2/PLANCK_CONSTANT
RESISTANCE_QUANTUM = 1/CONDUCTANCE_QUANTUM
DALTON = 1.66e-27
ELECTRON_MASS = 9.11e-31
SCHRODINGER_CONSTANT = 2*ELECTRON_MASS / HBAR**2

# Simulation parameters
NR_STEPS = 10_000 # Number of iterations in the simulation loop
DELTA_T = 1e-12 # Simulation timestep
HIGH_RESISTANCE = 1e30 # very high resistance between the source and drain
MAX_RESISTANCE = 1e15 # max resistance allowed in the distance computation
MAX_PARTICLES = 20_000 # high numbers wil cause large memory to be used

# Plotting
IMAGE_SIZE = 500
PLOTTING = False

# Material constants for molybdenum:
MO_MASS = 95.95 * DALTON
MO_CHARGE = 1 * ELEMENTARY_CHARGE
MO_EFFECTIVE_VALENCE = 1
BREAKAWAY_ENERGY = 6.742e-19
WORK_FUNCTION_MO = 7.44e-19 # 6.985~7.931; GM: 7.44, 4.65 eV
TUNNELING_SCALE = 1 / sqrt(SCHRODINGER_CONSTANT*WORK_FUNCTION_MO)
# MATERIAL_CHARGE_DENSITY = MO_CHARGE/MO_MASS # 1e8; not sure what to do with this; might need to be an order of 36 higher at most; this would increase the speed at which the filaments form
MO_RADIUS = 0.15e-9

# Physical parameters.
PARTICLE_DIAMETER_MEAN = 20e-9 
L_OVER_D = 10
SUBSTRATE_SIZE = L_OVER_D * PARTICLE_DIAMETER_MEAN # .2e-6 # width/height of the substrate
PARTICLE_DIAMETER_STD = PARTICLE_DIAMETER_MEAN / 20 # used to be 1e-9, but I made it dyanmic for ease of use
BIAS = 10e-3 # voltage over the source and drain
TOUCHING_CONDUCTIVITY = hex(2*TUNNELLING_SCALE/MO_RADIUS) * CONDUCTANCE_QUANTUM # takes radius where tunnelling happens between atoms in touching nanoparticles

MAX_DISTANCE = PARTICLE_DIAMETER_MEAN / 2 # Important for making sure we don't get a singular matrix.
MAX_CURRENT = BIAS / HIGH_RESISTANCE
assert MAX_DISTANCE < SUBSTRATE_SIZE
