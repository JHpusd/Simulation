import matplotlib.pyplot as plt
plt.style.use('bmh')

susceptible = 1000
infected = 1
recovered = 0
s_list = []
i_list = []
r_list = []

t = []
for i in range(501):
    t.append(i)

def num_copy(num):
    copy = 0
    copy += num
    return copy

for _ in range(len(t)):
    s_list.append(susceptible)
    i_list.append(infected)
    r_list.append(recovered)

    s_copy = num_copy(susceptible)
    i_copy = num_copy(infected)
    r_copy = num_copy(recovered)

    susceptible += -0.0003*s_copy*i_copy
    infected += (0.0003*s_copy*i_copy) - (0.02*i_copy)
    recovered += 0.02*i_copy

plt.plot(t, s_list, label='susceptible')
plt.plot(t, i_list, label='infected')
plt.plot(t, r_list, label='recovered')
plt.legend(loc='center right')
plt.xlabel('time')
plt.ylabel('people')
plt.savefig('sir_model.png')
