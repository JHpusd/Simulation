import matplotlib.pyplot as plt

class EulerEstimator():
    
    def __init__(self, derivative):
        self.derivative = derivative
    
    def calc_derivative_at_point(self, coordinates):
        x = coordinates[0]
        return self.derivative(x)
    
    def step_forward(self, point, step_size):
        x = point[0]
        y = point[1]
        new_point = (x + step_size, y + self.calc_derivative_at_point(point)*step_size)
        return new_point
    
    def calc_estimated_points(self, point, step_size, num_steps):
        print(point)
        for i in range(num_steps):
            print(self.step_forward(point, step_size))
            point = self.step_forward(point, step_size)
        return
    
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
