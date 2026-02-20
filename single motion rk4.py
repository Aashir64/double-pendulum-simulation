import matplotlib.pyplot as plt
import numpy as np
import math

def derivatives(theta, omega):
    return omega, -(g/l)*math.sin(theta)

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
theta = (theta + math.pi) % (2 * math.pi) - math.pi
Es = []

while t < t_end:
    times.append(t)
    thetas.append(theta)
    omegas.append(omega)
    k1_theta, k1_omega = derivatives(theta, omega)
    k2_theta, k2_omega = derivatives( theta + 0.5*dt*k1_theta, omega + 0.5*dt*k1_omega)
    k3_theta, k3_omega = derivatives(theta + 0.5*dt*k2_theta, omega + 0.5*dt*k2_omega)
    k4_theta, k4_omega = derivatives( theta + dt*k3_theta, omega + dt*k3_omega)

    v = l * omega
    T = 0.5 * v**2
    V =  g * l * (1 - math.cos(theta))
    E = T + V
    Es.append(E)



    theta += (dt / 6) * (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta)
    omega += (dt / 6) * (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega)
    t += dt

plt.plot(times, thetas)
plt.xlabel("Time (s)")
plt.ylabel("angle radians")
plt.title("angle from verticle vs time")
plt.show()