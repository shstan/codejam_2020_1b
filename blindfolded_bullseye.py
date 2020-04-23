import sys
from math import sin, cos, pi
from random import randint, randrange, uniform
class hit_guesser:
    def __init__(self, A, B):
        self.A = min(A, B)
        self.B = max(A, B)
        self.radius = self.B
        self.travel_dist = 10**9
        self.prev_response = None
        self.prev_move = None

    def rand_angle_travel(self, source, angle_range, power):
        return source[0] + round(power * cos(uniform(*angle_range))),\
               source[1] + round(power * sin(uniform(*angle_range)))

    def move(self, source, vec):
        return source[0] + vec[0],\
               source[1] + vec[1]

    def hear_and_guess(self, response):
        if self.prev_move is None:
            if response == 'MISS':
                self.prev_move = self.rand_angle_travel((0, 2 * pi), self.travel_dist)
                return move(self.prev_move,
            if response == 'HIT':
                self.travel_dist = self.radius
                self.prev_move = self.rand_angle_travel((0, 2 * pi), self.travel_dist)
                return self.prev_move
            if response == "CENTER":
                return None
        elif self.prev_move[0] <


if __name__ == "__main__":
    T, A, B = [int(x) for x in input().split()]
    for t in range(1, T+1):
        print(0, 0)
        sys.stdout.flush()
        gusser = hit_guesser(A, B)
        for i in range(300):
            gusser.

