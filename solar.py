
# from vpython import sphere, vector, color, rate, mag, norm

# # Constants
# AU = 1.496e11  # Astronomical Unit in meters
# G = 6.67430e-11  # Gravitational constant
# dt = 60 * 60 * 6  # 6 hours per time step
# SUN_MASS = 1.989e30  # in kg

# # Planet data: name: [mass, distance from sun, orbital speed, radius (viz), color]
# planets_data = {
#     "Mercury": [3.3e23, 0.39 * AU, 47.9e3, 0.02, color.gray(0.5)],
#     "Venus":   [4.87e24, 0.72 * AU, 35.0e3, 0.03, color.orange],
#     "Earth":   [5.97e24, 1.00 * AU, 29.8e3, 0.035, color.blue],
#     "Mars":    [6.42e23, 1.52 * AU, 24.1e3, 0.025, color.red],
# }

# # Create the Sun
# sun = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.yellow, emissive=True)

# # Create planets
# planets = []

# for name, data in planets_data.items():
#     mass, dist, vel, radius, clr = data
#     planet = sphere(
#         pos=vector(dist / AU, 0, 0),  # Scale position in AU
#         radius=radius,
#         color=clr,
#         make_trail=True,
#         retain=200
#     )
#     planet.mass = mass
#     planet.velocity = vector(0, vel, 0)  # Tangential velocity
#     planets.append(planet)

# # Simulation loop
# while True:
#     rate(200)

#     for planet in planets:
#         r_vec = planet.pos - sun.pos
#         r_mag = mag(r_vec)

#         # Calculate gravitational force
#         force_mag = G * planet.mass * SUN_MASS / (r_mag * AU)**2  # back to meters
#         force_dir = -norm(r_vec)
#         force = force_mag * force_dir

#         # Update velocity and position
#         acceleration = force / planet.mass
#         planet.velocity += acceleration * dt
#         planet.pos += planet.velocity * dt / AU  # scale back to AU



