import numpy as np
from copy import deepcopy
import math

"""
My original BFS solution (Gets WA for unknown reason!)
"""
def get_route(X, Y):
    if (X + Y) % 2 == 0:
        return get_moves(None)
    start = (0, 0)
    queue = [[start]]
    visited = set()
    res_path = None
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex == (X, Y):
            res_path = path
            break
        elif vertex not in visited:
            for cur_neighbor in get_children(vertex[0], vertex[1], 2 ** (len(path) - 1)):
                new_path = path[:]
                new_path.append(cur_neighbor)
                queue.append(new_path)
            visited.add(vertex)
    # print(res_path)
    return get_moves(res_path)

def get_moves(path):
    if path is None:
        return 'IMPOSSIBLE'
    moves = []
    for i in range(len(path) - 1):
        if path[i][0] > path[i + 1][0]:
            moves.append('W')
        elif path[i][0] < path[i + 1][0]:
            moves.append('E')
        elif path[i][1] > path[i + 1][1]:
            moves.append('S')
        else:
            moves.append('N')
    return ''.join(moves)

def get_children(X, Y, jump_dist):
    children = []
    if X - jump_dist >= -10**9:
        children.append((X - jump_dist, Y))
    if X + jump_dist <= 10**9:
        children.append((X + jump_dist, Y))
    if Y - jump_dist >= -10**9:
        children.append((X, Y - jump_dist))
    if Y + jump_dist <= 10**9:
        children.append((X, Y + jump_dist))
    return children

"""
Solution #2
"""
def bin_array(num, m):
    """Convert a positive integer num into an m-bit bit vector"""
    return np.array(list(np.binary_repr(num).zfill(m))).astype(np.int8)

def validate_moves(k, N, S, W, E, X, Y):
    if N < 0 or S < 0 or W < 0 or E < 0:
        return None
    start = np.array((0, 0))
    moves = np.array([[0, 1], [0, -1], [-1, 0], [1, 0]])
    move_dirs = ['N', 'S', "W", 'E']
    dirs = []
    bitarr = np.zeros((4, k))
    for i, dir in enumerate((N, S, W, E)):
        bitarr[i] = bin_array(dir, k)[::-1]
    for i in range(k):
        gi = np.argmax(bitarr[:, i])
        start += moves[gi] * (2**i)
        dirs.append(move_dirs[gi])
    # print(start)
    if start[0] == X and start[1] == Y:
        return dirs
    return None



def bizzaire_trick(X, Y):
    """
    algorithm by @hitman623 from https://codeforces.com/blog/entry/76281
    E - W = X
    N - S = Y
    N + S + E + W = 2**K - 1
    a = N + E
    b = S + W
    c = N + W
    You know per each step in k steps, only one of N, S, W, E can have 1 as bit.
    N = a & c (What bits do N + E and N + W share? That's North movement!)
    E = a - N (clearing N's bits from a leaves us with E. Same logic for W and S)
    :param X:
    :param Y:
    :return:
    """
    mandist = X + Y
    for k in range(math.floor(math.log2(abs(X) + abs(Y))), 32):
        sum_o_moves = 2**k - 1
        a = (sum_o_moves + X + Y)//2
        b = (sum_o_moves - X - Y)//2
        c = (sum_o_moves - X + Y)//2
        N = a & c
        E = a - N
        W = c - N
        S = b - W
        # print(k, N, W, S, E)
        res = validate_moves(k, N, S, W, E, X, Y)
        if res is not None:
            return ''.join(res)
    return 'IMPOSSIBLE'




if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        X, Y = [int(x) for x in input().split()]
        print("Case #{}: {}".format(t, bizzaire_trick(X, Y)))
