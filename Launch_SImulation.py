import math
import matplotlib.pyplot as plt

# Simulation constants
initial_pressure_psi = 90  # psi
initial_pressure = initial_pressure_psi * 6894.757  # pa
tube_radius = 0.0381  # m
tube_length = 1  # m
system_mass = 2  # kg
reservoir_length = 0.1  # m
tube_area = math.pi * tube_radius ** 2
initial_reservoir_volume = tube_area * reservoir_length
reservoir_moles_of_air = initial_pressure * initial_reservoir_volume / (8.31446261815324 * 273.15)

# Simulation variables
dt = 0.0001
time = [0]
force = [initial_pressure * tube_area]
acceleration = [force[-1]/system_mass]
velocity = [0]
position = [0]
pressure = [initial_pressure]
volume = [initial_reservoir_volume]

# Simulation loop
while position[-1] < tube_length:
    # t = t0 + dt
    time.append(time[-1] + dt)

    # V = pi * r^2 * l
    volume.append(tube_area * reservoir_length + tube_area * position[-1])

    # PV = nRT
    pressure.append(reservoir_moles_of_air * 8.31446261815324 * 273.15 / volume[-1])

    # F = P * A
    force.append(pressure[-1] * tube_area)

    # a = F / m
    acceleration.append(force[-1] / system_mass)

    # v = a * dt + v0
    velocity.append(acceleration[-1] * dt + velocity[-1])

    # x = v * dt + x0
    position.append(velocity[-1] * dt + position[-1])


print(f'Final Iteration\na = {acceleration[-1]} m/s2\nv = {2.236936 * velocity[-1]} mph\np = {position[-1]} m')

plt.plot(position, velocity)
plt.ylabel('velocity')
plt.xlabel('position')

plt.show()
