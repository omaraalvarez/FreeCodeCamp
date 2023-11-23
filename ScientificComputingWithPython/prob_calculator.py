import random


class Hat:

    def __init__(self, **kwargs):

        self.contents = []
        self.n = 0

        for color, amount in kwargs.items():

            for _ in range(amount):
                self.contents.append(color)

    def draw(self, n):

        self.n = n

        if self.n >= len(self.contents):

            return self.contents

        else:

            drawn = random.choices(self.contents, k = self.n)

            return drawn

    def __len__(self):

        return len(self.contents) - self.n


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success = 0

    for _ in range(num_experiments):

        result = dict()

        drawn = hat.draw(num_balls_drawn)

        for d in drawn:

            if d in result:

                result[d] += 1

            else:

                result[d] = 1

        colors = [c for c in result.keys()]
        s = []

        for color in colors:

            if color in expected_balls and result[color] >= expected_balls[color]:

                s.append(True)

        if sum(s) == len(expected_balls):

            success += True

    return success / num_experiments
