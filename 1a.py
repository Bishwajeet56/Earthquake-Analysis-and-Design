import os
import numpy as np
import matplotlib.pyplot as plt

# File details
file_name = 'RSN813_LOMAP_YBI090.AT2'
#add your file path and uncomment the line below
#file_path = <file path>
full_file_path = os.path.join(file_path, file_name)

# Parse the file
with open(full_file_path, 'r') as file:
    # Skip first 3 lines and read the header
    for _ in range(3):
        next(file)
    header_line = file.readline()  # Read the line containing NPTS and DT

    # Extract NPTS and DT
    npts = int(header_line.split('=')[1].split(',')[0].strip())  # Extract NPTS
    dt = float(header_line.split('=')[2].split('SEC')[0].strip())  # Extract DT

    # Read the acceleration data
    data = []
    for line in file:
        data.extend([float(value) for value in line.split()])

# Convert acceleration to m/s²
acceleration = np.array(data) * 9.81

# Generate time vector
time = np.linspace(0, (npts - 1) * dt, npts)

# Find maximum and minimum acceleration
max_accel = np.max(acceleration)
min_accel = np.min(acceleration)
max_time = time[np.argmax(acceleration)]
min_time = time[np.argmin(acceleration)]

# Plotting acceleration response
plt.figure(figsize=(10, 6))
plt.plot(time, acceleration, 'b-', linewidth=1.5, label='Acceleration')

# Highlight maximum and minimum points
plt.scatter(max_time, max_accel, color='red', label=f'Max: {max_accel:.2f} m/s²', zorder=5)
plt.scatter(min_time, min_accel, color='green', label=f'Min: {min_accel:.2f} m/s²', zorder=5)

plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Acceleration (m/s²)', fontsize=12)
plt.title('Acceleration Response Over Time', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True)
plt.show()
