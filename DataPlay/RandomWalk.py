from random import choice

class RandomWalk(object):
    """Generates random walks"""
    
    def __init__(self,num_points=5000):
        self.num_points = num_points

        #all walks start at 0
        self.x_vals = [0]
        self.y_vals = [0]

    def fill_walk(self):
        """calculate all the points on walk"""

        while len(self.x_vals) < self.num_points:

            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 or y_step == 0:
                continue

            self.x_vals.append(self.x_vals[-1] + x_step)
            self.y_vals.append(self.y_vals[-1] + y_step)


