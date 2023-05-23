import random
import copy


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += value * [key]

    def draw(self, num_balls_drawn):
        N = len(self.contents)
        if N <= num_balls_drawn:
            return self.contents
        else:
            remaining_balls = random.choices(self.contents, k=N - num_balls_drawn)
            for ball in remaining_balls:
                self.contents.remove(ball)
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    s = set(expected_balls)
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)  # created a copy for each iteration
        drawn_balls = another_hat.draw(num_balls_drawn)  # making changes with copy in each iteration
        check = []
        for item in s:
            check += [drawn_balls.count(item) >= expected_balls.count(item)]
        if all(check):
            M += 1
    return M / num_experiments
