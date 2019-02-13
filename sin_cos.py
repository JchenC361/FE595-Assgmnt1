import numpy as np
import matplotlib.pyplot as plt

# Make lines more accurate while approaching x = 1
time = np.arange(0,2*np.pi,0.01)
sin = np.sin(time)
cos = np.cos(time)
tan = np.tan(time)

# Limit the range of y axis between -1 to 1.
plt.ylim((-1, 1))

plt.plot(time, sin, time, cos)
plt.axhline(y=0, color = 'black')
# Plot tangent line.
plt.plot(time, tan, color='grey')

# Generate figure before plt.show in order to avoid outputting blank image.
fig = plt.gcf()

# Save the created image in your local directory.
fig.savefig('D:/SinCosTan.png')

plt.show()
