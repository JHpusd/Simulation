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
    
    def calc_estimated_points(self, point, step_size, max_value):
        point_list = [point]
        counter = 0
        while counter < max_value:
            next_point = self.step_forward(point, step_size)
            point_list.append(next_point)
            point = next_point
            counter += step_size
        return point_list

    def plot(self, point, step_size, max_value):
        plt.style.use('bmh')
        points = self.calc_estimated_points(point, step_size, max_value)
        t_list = [point[0] for point in points]
        values = [point[1] for point in points]
        for key in point[1]:
            plt.plot(t_list, [vals[key] for vals in values], label=key)
        plt.legend(loc="upper left")
        plt.savefig("plot.png")


