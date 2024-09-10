from matplotlib import pyplot as plt
import math

# 3.5573 m/s level 2, 4.9125 m/s level 3

# Konstanter
g = 9.81 # m/s^2
v0 = 4.9125 # m/s
angle = 0 * math.pi / 180 # radianer
y0 = 1.025 # m
x0 = 0 # m
t = 0 # s
dt = 1e-2 # s

target = float(input("Target distance: ")) # m

# Visualise initial path at 0 degrees
x = x0
y = y0
x_values = [x]
y_values = [y]
while y >= 0:
    x = x0 + v0 * math.cos(angle) * t
    y = y0 + v0 * math.sin(angle) * t - 0.5 * g * t**2

    x_values.append(x)
    y_values.append(y)

    t += dt
    
plt.plot(x_values, y_values)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile motion")
plt.show()



# Calculate angle for target distance
while True:
    while y >= 0:
        x = x0 + v0 * math.cos(angle) * t
        y = y0 + v0 * math.sin(angle) * t - 0.5 * g * t**2

        t += dt
    
    if x > target:
        break
    else:
        angle += 0.01 * math.pi / 180
        print(f"Angle: {angle * 180 / math.pi} degrees")
        t = 0
        x = x0
        y = y0


print("--------------------")
print(f"Angle: {angle * 180 / math.pi} degrees")