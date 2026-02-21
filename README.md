Double Pendulum Motion Simulation 

in this project i used rk4 numerical apporximation to create a simulation of a double pendulum. Rk4 takes a weighted average of 4 different slope estimates across an interval in order to estimate the nature of the graph. Due to the number of varables affecting the movement of the pendulam, a exact solusion cannot be used. in this code the user can change the intial angles, the length of the rod,
gravitational acceleration, and the mass of the ball and observe how the path of the pendulum can change.

## Features
- RK4 solver for the double pendulum ODE system
- Matplotlib animation of the two-link pendulum
- Parameters you can tweak: initial angles, rod lengths, masses, gravity, time-step
- **Chaos demonstration:** small changes in initial conditions (e.g. 0.01 rad) can produce drastically different trajectories



## How it works (high-level)
State vector:
\[
y = [\theta_1,\ \omega_1,\ \theta_2,\ \omega_2]
\]
The model computes:
\[
y' = [\omega_1,\ \alpha_1,\ \omega_2,\ \alpha_2]
\]
and RK4 advances the state by taking a weighted average of four slope estimates across each timestep.

### Requirements
- Python 3.x  
- numpy, matplotlib (and scipy only if you’re also running the single-pendulum exact solution)

Install:
```bash
pip install -r requirements.txt
