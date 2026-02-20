import matplotlib.pyplot as plt

import math
l = 1.0
g = 9.81
theta = 1 #rad
omega = 0.0
dt = 0.01
t_end = 10
t= 0.0
times = []
thetas = []
omegas = []
Es = []
theta = (theta + math.pi) % (2 * math.pi) - math.pi
while t < t_end:
    times.append(t)
    thetas.append(theta)
    omegas.append(omega)
    alpha = -(g/l) * math.sin(theta)
    omega += alpha * dt
    theta += omega * dt
    theta = (theta + math.pi) % (2 * math.pi) - math.pi
    t += dt

    v = l * omega
    T = 0.5 * v ** 2
    V = g * l * (1 - math.cos(theta))
    E = T + V
    Es.append(E)


plt.plot(times, thetas)
plt.xlabel("Time (s)")
plt.ylabel("angle radians")
plt.title("angle from vertical vs time")
plt.show()
