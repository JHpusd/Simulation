# import matplotlib.pyplot as plt

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
    '''
    def plot(self, point, step_size, num_steps):
        x_coords = [point[0]]
        y_coords = [point[1]]
        for _ in range(num_steps + 1):
        # +1 to show the last point on the graph more clearly
            point = self.step_forward(point, step_size)
            x_coords.append(point[0])
            y_coords.append(point[1])
        plt.style.use('bmh')
        plt.plot(x_coords, y_coords)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig('plot.png')
    '''

