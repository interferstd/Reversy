import numpy as np

empty = 0
first = 1
second = 2
draw = 3

def read_step(a, b):
    x, y = map(int, input('your step: ').split(" "))
    return (x, y)

class Blackboard:
    def __init__(self):
        self.desk = np.zeros((8,8), dtype=np.int8)
        self.desk[3][3] = first
        self.desk[4][4] = first
        self.desk[3][4] = second
        self.desk[4][3] = second
        self.current_plr = first
        self.other_plr = second

    # takes one argument
    # which is a function returning a coordinates of move
    def make_step(self, coord_function):
        x, y = coord_function(self.desk, self.possible_steps())
        # assuming that (x, y) is legal move
        x1, y1 = x, y
        # changing horisontals and verticals
        self.desk[x][y] = self.current_plr
        while x1 >= 0:
            x1 -= 1
            if x1 < 0:
                break
            if self.desk[x1][y] == empty:
                break
            if self.desk[x1][y] == self.current_plr:
                if self.desk[x1+1][y] == self.other_plr:
                    while x1 < x:
                        self.desk[x1][y] = self.current_plr
                        x1 += 1
                break
            #x1 -= 1
        x1 = x
        while x1 < 8:
            x1 += 1
            if x1 > 7:
                break
            if self.desk[x1][y] == empty:
                break
            if self.desk[x1][y] == self.current_plr:
                if self.desk[x1-1][y] == self.other_plr:
                    while x1 > x:
                        self.desk[x1][y] = self.current_plr
                        x1 -= 1
                break
        x1, y1 = x, y
        while y1 >= 0:
            y1 -= 1
            if y1 < 0:
                break
            if self.desk[x][y1] == empty:
                break
            if self.desk[x][y1] == self.current_plr:
                if self.desk[x][y1+1] == self.other_plr:
                    while y1 < y:
                        self.desk[x][y1] = self.current_plr
                        y1 += 1
                break
        y1 = y
        while y1 < 8:
            y1 += 1
            if y1 > 7:
                break
            if self.desk[x][y1] == empty:
                break
            if self.desk[x][y1] == self.current_plr:
                if self.desk[x][y1-1] == self.other_plr:
                    while y1 > y:
                        self.desk[x][y1] = self.current_plr
                        y1 -= 1
                break
        x1, y1 = x, y
        while x1 < 7 and y1 < 7:
            x1 += 1
            y1 += 1
            if self.desk[x1][y1] == empty:
                break
            if self.desk[x1][y1] == self.current_plr:
                if self.desk[x1-1][y1-1] == self.other_plr:
                    while x1 > x and y1 > y:
                        self.desk[x1][y1] = self.current_plr
                        y1 -= 1
                        x1 -= 1
                break
        x1, y1 = x, y
        while x1 > 0 and y1 < 7:
            x1 -= 1
            y1 += 1
            if self.desk[x1][y1] == empty:
                break
            if self.desk[x1][y1] == self.current_plr:
                if self.desk[x1 + 1][y1 - 1] == self.other_plr:
                    while x1 < x and y1 > y:
                        self.desk[x1][y1] = self.current_plr
                        y1 -= 1
                        x1 += 1
                break
        x1, y1 = x, y
        while x1 > 0 and y1 > 0:
            x1 -= 1
            y1 -= 1
            if self.desk[x1][y1] == empty:
                break
            if self.desk[x1][y1] == self.current_plr:
                if self.desk[x1 + 1][y1 + 1] == self.other_plr:
                    while x1 < x and y1 < y:
                        self.desk[x1][y1] = self.current_plr
                        y1 += 1
                        x1 += 1
                break
        x1, y1 = x, y
        while x1 < 7 and y > 0:
            x1 += 1
            y1 -= 1
            if self.desk[x1][y1] == empty:
                break
            if self.desk[x1][y1] == self.current_plr:
                if self.desk[x1 - 1][y1 + 1] == self.other_plr:
                    while x1 > x and y1 < y:
                        self.desk[x1][y1] = self.current_plr
                        y1 += 1
                        x1 -= 1
                break
        self.current_plr, self.other_plr = self.other_plr, self.current_plr
        if len(self.possible_steps()) == 0:
            self.current_plr, self.other_plr = self.other_plr, self.current_plr
        unique, counts = np.unique(self.desk, return_counts=True)
        occurance = dict(zip(unique, counts))
        # print(occurance)
        # print(occurance[second])
        if empty not in occurance:
            if occurance[first] > occurance[second]:
                return first
            elif occurance[first] < occurance[second]:
                return second
            else:
                return draw
        elif first not in occurance:
            return second
        elif second not in occurance:
            return first
        else:
            return empty

    # return a list of pairs of possible steps for current player
    def possible_steps(self):
        # print(self.desk)
        possible = []
        for i in range(8):
            for j in range(8):
               # print(i, j)
                if self.desk[i][j] == self.current_plr:
                    x, y = i, j
                    # checking verticals and horisontals
                    while x < 8:
                        if self.desk[x][j] == empty:
                            break
                        if self.desk[x][j] == self.other_plr:
                            if x < 7:
                                if self.desk[x+1][j] == empty:
                                    possible.append((x+1, y))
                                    break
                            if not(x < 7 and self.desk[x+1][j] == self.other_plr):
                                break
                        x += 1
                    x = i
                    while x >= 0:
                        if self.desk[x][j] == empty:
                            break
                        if self.desk[x][j] == self.other_plr:
                            if x > 0:
                                if self.desk[x-1][j] == empty:
                                    possible.append((x-1, y))
                                    break
                            if not(x > 0 and self.desk[x-1][j] == self.other_plr):
                                break
                        x -= 1
                    x = i
                    while y < 8:
                        if self.desk[i][y] == empty:
                            break
                        if self.desk[i][y] == self.other_plr:
                            if y < 7:
                                if self.desk[i][y+1] == empty:
                                    possible.append((x, y+1))
                                    break
                            if not(y < 7 and self.desk[x][y+1] == self.other_plr):
                                break
                        y += 1
                    y = j
                    while y >= 0:
                        if self.desk[i][y] == empty:
                            break
                        if self.desk[i][y] == self.other_plr:
                            if y > 0:
                                if self.desk[i][y-1] == empty:
                                    possible.append((x, y-1))
                                    break
                            if not(y > 0 and self.desk[x][y-1] == self.other_plr):
                                break
                        y -= 1
                    x, y = i, j
                    # checking diagonals
                    while x >= 0 and y < 8:
                        if self.desk[x][y] == empty:
                            break
                        if self.desk[x][y] == self.other_plr:
                            if x > 0 and y < 7:
                                if self.desk[x-1][y+1] == empty:
                                    possible.append((x-1, y+1))
                                    break
                            if not(x > 0 and y < 7 and self.desk[x-1][y+1] == self.other_plr):
                                break
                        x -= 1
                        y += 1
                    x, y = i, j
                    while x < 8 and y < 8:
                        if self.desk[x][y] == empty:
                            break
                        if self.desk[x][y] == self.other_plr:
                            if x < 7 and y < 7:
                                if self.desk[x+1][y+1] == empty:
                                    possible.append((x+1, y+1))
                                    break
                            if not(x < 7 and y < 7 and self.desk[x+1][y+1] == self.other_plr):
                                break
                        x += 1
                        y += 1
                    x, y = i, j
                    while x < 8 and y >= 0:
                        if self.desk[x][y] == empty:
                            break
                        if self.desk[x][y] == self.other_plr:
                            if x < 7 and y > 0:
                                if self.desk[x+1][y-1] == empty:
                                    possible.append((x+1, y-1))
                                    break
                            if not(x < 7 and y > 0 and self.desk[x+1][y-1] == self.other_plr):
                                break
                        x += 1
                        y -= 1
                    x, y = i, j
                    while x >= 0 and y >= 0:
                        if self.desk[x][y] == empty:
                            break
                        if self.desk[x][y] == self.other_plr:
                            if x > 0 and y > 0:
                                if self.desk[x-1][y-1] == empty:
                                    possible.append((x-1, y-1))
                                    break
                            if not(x > 0 and y > 0 and self.desk[x-1][y-1] == self.other_plr):
                                break
                        x -= 1
                        y -= 1

        return list(dict.fromkeys(possible))

# можно попробовать поиграть самому с собой - на каждом ходе выводятся все возможные ходы для текущего игрока
if __name__ == "__main__":
    board = Blackboard()
    #board.desk[3][2] = first
    #board.desk[5][3] = second
    #board.desk[2][4] = second
    #board.desk[5][4] = first
    #board.desk[6][4] = first
    #board.desk[2][5] = first
    #board.desk[2][3] = first
    print(board.desk)
    while True:
        print('current plr: ', board.current_plr)
        print(board.possible_steps())
        state = board.make_step(read_step)
        print(board.desk)
        if state != empty:
            if state == first:
                print('first player wins')
            elif state == second:
                print('second player wins')
            else:
                print('draw!')
            break
