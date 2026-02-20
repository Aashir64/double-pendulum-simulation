import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation

def derivatives(state):
    t1, w1, t2, w2 = state
    delta = t1 - t2
    den =  (2* m1) + m2 - (m2*math.cos(2*delta))

    if abs(den) < 1e-9:
        den = 1e-9 if den >= 0 else -1e-9


    a1 = (-g*(2*m1 + m2)*math.sin(t1) - m2*g*math.sin(t1 - 2*t2) - 2*math.sin(delta)*m2*(w2**2 * l2 + w1**2 * l1 * math.cos(delta))) / (l1*den)

    a2 = (2*math.sin(delta)*(w1**2 * l1 * (m1 + m2) + g*(m1 + m2)*math.cos(t1) + w2**2 * l2 * m2 * math.cos(delta))) / (l2*den)

    return (w1, a1, w2, a2)


def vadd(state, k, c):

    t1, w1, t2, w2 = state
    dt1, dw1, dt2, dw2 = k
    return t1 + c*dt1 , w1 + c*dw1 , t2 + c*dt2 , w2 + c*dw2



def rk4_step(state):
    k1 = derivatives(state)
    k2 = derivatives(vadd(state, k1, dt/2))
    k3 = derivatives(vadd(state, k2, dt/2))
    k4 = derivatives(vadd(state, k3, dt))

    t1, w1, t2, w2 = state
    dt1_1, dw1_1, dt2_1, dw2_1 = k1
    dt1_2, dw1_2, dt2_2, dw2_2 = k2
    dt1_3, dw1_3, dt2_3, dw2_3 = k3
    dt1_4, dw1_4, dt2_4, dw2_4 = k4

    t1_new = t1 + (dt/6) * (dt1_1 + 2*dt1_2 + 2*dt1_3 + dt1_4)
    w1_new = w1 + (dt/6) * (dw1_1 + 2*dw1_2 + 2*dw1_3 + dw1_4)
    t2_new = t2 + (dt/6) * (dt2_1 + 2*dt2_2 + 2*dt2_3 + dt2_4)
    w2_new = w2 + (dt/6) * (dw2_1 + 2*dw2_2 + 2*dw2_3 + dw2_4)

    return (t1_new, w1_new, t2_new, w2_new)






m1 = 1.1

m2 = 1

l1 = 0.01
l2 = 0.01
g = 9.81
t1 = 2.01   #rad
t2 = 1.0
x1s = []
y1s = []
x2s = []
y2s = []

w1 = 0.0
w2 = 0.0
dt = 0.01
t_end = 10
t= 0.0
state = (t1, w1, t2, w2)
times = []
t1s, w1s, t2s, w2s = [], [], [], []


while t < t_end:
    times.append(t)
    t1s.append(state[0])
    w1s.append(state[1])
    t2s.append(state[2])
    w2s.append(state[3])

    # 2) step
    state = rk4_step(state)

    # 3) time update
    t += dt





for a1, a2 in zip(t1s, t2s):
    x1 = l1 * math.sin(a1)
    y1 = -l1 * math.cos(a1)
    x2 = x1 + l2 * math.sin(a2)
    y2 = y1 - l2 * math.cos(a2)

    x1s.append(x1); y1s.append(y1)
    x2s.append(x2); y2s.append(y2)



fig, ax = plt.subplots()
ax.set_xlim(-(l1+l2), l1+l2)
ax.set_ylim(-(l1+l2), l1+l2)
ax.set_aspect('equal')

line, = ax.plot([], [], 'o-',lw=3, markersize=10)  # rod + bob
trace, = ax.plot([], [], '-', alpha=0.5)
def update(i):
    line.set_data([0, x1s[i], x2s[i]], [0, y1s[i], y2s[i]])
    trace.set_data(x2s[:i], y2s[:i])
    return line, trace



ax.plot(0, 0, 'ko')
anim = FuncAnimation(fig, update, frames=len(x1s), interval=32, blit=False)
plt.show()
