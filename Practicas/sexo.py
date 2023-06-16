import numpy as np
import matplotlib.pyplot as plt

number_of_people = np.random.rand(100)
interests = np.random.rand(100)

# ------

fig, ax = plt.subplots()
ax = plt.scatter(number_of_people, interests)
plt.grid()
plt.show()
