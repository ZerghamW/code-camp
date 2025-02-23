import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        # Randomly draw balls without replacement
        drawn = random.sample(self.contents, num_balls)
        # Remove the drawn balls from contents
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful = 0
    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        new_hat = copy.deepcopy(hat)
        drawn = new_hat.draw(num_balls_drawn)
        # Count the drawn balls
        drawn_counts = {}
        for color in drawn:
            drawn_counts[color] = drawn_counts.get(color, 0) + 1
        # Check if expected_balls are met
        met = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                met = False
                break
        if met:
            successful += 1
    return successful / num_experiments