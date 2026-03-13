import numpy as np

def calculate_trajectory(v0, angle_deg, dt=0.01, g=9.81, k=0.01):
    """
    Calculates the trajectory of a projectile with air resistance.
    v0: Initial velocity (m/s)
    angle_deg: Launch angle (degrees)
    k: Drag coefficient (simplified)
    """
    angle_rad = np.radians(angle_deg)
    
    # Initial conditions
    vx, vy = v0 * np.cos(angle_rad), v0 * np.sin(angle_rad)
    x, y = [0.0], [0.0]
    
    while y[-1] >= 0:
        # Physics Logic: v = v + a*dt
        # Acceleration with drag: a = -g - (k/m)*v (assuming m=1 for simplicity)
        ax = -k * vx
        ay = -g - k * vy
        
        vx += ax * dt
        vy += ay * dt
        
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)
        
    return np.array(x), np.array(y)

# Example Validation
x_vals, y_vals = calculate_trajectory(v0=50, angle_deg=45)
print(f"Simulation Complete. Max Range: {max(x_vals):.2f}m")
