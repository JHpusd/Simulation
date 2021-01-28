import matplotlib.pyplot as plt
plt.style.use('bmh')

deer = 100
wolves = 10
d_list = []
w_list = []

t = []
counter = 0
while counter <= 100:
    t.append(counter)
    counter += 0.001

for _ in range(len(t)):
    d_list.append(deer)
    w_list.append(wolves)

    d_copy = deer
    w_copy = wolves

    deer += 0.001*((0.6*d_copy) - (0.05*d_copy*w_copy))
    wolves += 0.001*((0.02*d_copy*w_copy) - (0.9*w_copy))

plt.plot(t, d_list, label='deer')
plt.plot(t, w_list, label='wolves')
plt.legend(loc='upper right')
plt.xlabel('time (in years)')
plt.ylabel('population')
plt.savefig('predator_prey_model.png')
