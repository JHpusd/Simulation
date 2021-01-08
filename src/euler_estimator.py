import matplotlib.pyplot as plt

class EulerEstimator():
    
    def __init__(self, derivative):
        self.derivative = derivative
    
    def calc_derivative_at_point(self, coords):
        result = {}
        for key in self.derivative:
            result[key] = self.derivative[key](coords[0], coords[1])
        return result
    
    def step_forward(self, point, step_size):
        t = point[0]
        x = point[1]
        point_deriv = self.calc_derivative_at_point(point)
        new_x = {}
        for key in x:
            new_x[key] = x[key] + (point_deriv[key] * step_size)
        new_point = (t + step_size, new_x)
        return new_point
    
    def calc_estimated_points(self, point, step_size, num_steps):
        point_list = []
        point_list.append(point)
        for i in range(num_steps):
            next_point = self.step_forward(point, step_size)
            point_list.append(next_point)
            point = next_point
        return point_list

    def plot(self, point, step_size, max_value):
        t_list = []
        list_dict = {}
        for key in point[1]:
            list_dict[key] = []
        while True:
            t = point[0]
            if t > max_value:
                break
            t_list.append(t)
            x = point[1]
            for key in x:
                list_dict[key].append(x[key])
            point = self.step_forward(point, step_size)
        plt.style.use('bmh')
        for key in list_dict:
            plt.plot(t_list, list_dict[key], label=key)
        plt.legend(loc="upper left")
        plt.savefig('plot.png')


