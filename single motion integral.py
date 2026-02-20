import math
import matplotlib.pyplot as plt
from scipy.special import ellipj
from matplotlib.animation import FuncAnimation




l = 1.0
g = 9.81

theta0 = 1      # radians (max amplitude)
dt = 0.005
t_end = 10

k = math.sin(theta0 / 2)
m = k**2
m_bob = 1.0
times = []
thetas_exact = []
xs = []
ys = []
Es = []

t = 0.0
while t <= t_end:
    u = math.sqrt(g / l) * t
    sn, cn, dn, ph = ellipj(u, m)   # sn is what we need
    theta_t = 2 * math.asin(k * sn)
    x = l * math.sin(theta_t)
    y = -l * math.cos(theta_t)
    xs.append(x)
    ys.append(y)
    times.append(t)
    thetas_exact.append(theta_t)


    t += dt

fig, ax = plt.subplots()
ax.set_xlim(-l, l)
ax.set_ylim(-l, l)
ax.set_aspect('equal')

line, = ax.plot([], [], 'o-',lw=3, markersize=10)  # rod + bob
trace, = ax.plot([], [], '-', alpha=0.5)
def update(i):
    line.set_data([0, xs[i]], [0, ys[i]])
    trace.set_data(xs[:i], ys[:i])
    return line, trace

ax.plot(0, 0, 'ko')
anim = FuncAnimation(fig, update, frames=len(xs), interval=32, blit=False)
plt.show()



#omega_t = 2 * k * math.sqrt(g / l) * (cn * dn) / math.sqrt(1 - (k * sn) ** 2)

#    T = 0.5 * m * (l * omega_t) ** 2

#    V = m * g * l * (1 - math.cos(theta_t))

#    E = T + V