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
