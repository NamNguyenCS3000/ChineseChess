#Author: Nam Nguyen
#Chinese Chess Game

RED = "Red"
BLACK = "Black"
#Xiangqi_cardinal = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#Xiangqi_diagnal = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

class Xiangqi:
    """class for the Chinese-chess game Xiangqi"""
    def __init__(self):
        """initializes the game"""
        self.gameboard = {}
        self.place_piece()
        self.player_turn = RED
        self.main()
        self.message = "this is where prompts will go"

    def place_piece(self):
        """places red and black pieces on the board"""

        unit_dict = {RED: {Soldier: " 卒 ", Cannon: " 炮 ", Chariot: " 车 ", Horse: " 马 ", Elephant: " 相 ", Advisor: " 仕 ",
                           General: " 帅 "},
                     BLACK: {Soldier: " 兵 ", Cannon: " 砲 ", Chariot: " 車 ", Horse: " 馬 ", Elephant: " 象 ", Advisor: " 士 ",
                           General: " 将 "}}

        for i in range(0, 10):
            # red pieces
            if i == 0:
                self.gameboard[(i, 0)] = Chariot(RED, unit_dict[RED][Chariot])
                self.gameboard[(i, 1)] = Horse(RED, unit_dict[RED][Horse])
                self.gameboard[(i, 2)] = Elephant(RED, unit_dict[RED][Elephant])
                self.gameboard[(i, 3)] = Advisor(RED, unit_dict[RED][Advisor])
                self.gameboard[(i, 4)] = General(RED, unit_dict[RED][General])
                self.gameboard[(i, 5)] = Advisor(RED, unit_dict[RED][Advisor])
                self.gameboard[(i, 6)] = Elephant(RED, unit_dict[RED][Elephant])
                self.gameboard[(i, 7)] = Horse(RED, unit_dict[RED][Horse])
                self.gameboard[(i, 8)] = Chariot(RED, unit_dict[RED][Chariot])
            if i == 2:
                self.gameboard[(i, 1)] = Cannon(RED, unit_dict[RED][Cannon])
                self.gameboard[(i, 7)] = Cannon(RED, unit_dict[RED][Cannon])
            if i == 3:
                self.gameboard[(i, 0)] = Soldier(RED, unit_dict[RED][Soldier])
                self.gameboard[(i, 2)] = Soldier(RED, unit_dict[RED][Soldier])
                self.gameboard[(i, 4)] = Soldier(RED, unit_dict[RED][Soldier])
                self.gameboard[(i, 6)] = Soldier(RED, unit_dict[RED][Soldier])
                self.gameboard[(i, 8)] = Soldier(RED, unit_dict[RED][Soldier])
            # black pieces
            if i == 6:
                self.gameboard[(i, 0)] = Soldier(BLACK, unit_dict[BLACK][Soldier])
                self.gameboard[(i, 2)] = Soldier(BLACK, unit_dict[BLACK][Soldier])
                self.gameboard[(i, 4)] = Soldier(BLACK, unit_dict[BLACK][Soldier])
                self.gameboard[(i, 6)] = Soldier(BLACK, unit_dict[BLACK][Soldier])
                self.gameboard[(i, 8)] = Soldier(BLACK, unit_dict[BLACK][Soldier])
            if i == 7:
                self.gameboard[(i, 1)] = Cannon(BLACK, unit_dict[BLACK][Cannon])
                self.gameboard[(i, 7)] = Cannon(BLACK, unit_dict[BLACK][Cannon])
            if i == 9:
                self.gameboard[(i, 0)] = Chariot(BLACK, unit_dict[BLACK][Chariot])
                self.gameboard[(i, 1)] = Horse(BLACK, unit_dict[BLACK][Horse])
                self.gameboard[(i, 2)] = Elephant(BLACK, unit_dict[BLACK][Elephant])
                self.gameboard[(i, 3)] = Advisor(BLACK, unit_dict[BLACK][Advisor])
                self.gameboard[(i, 4)] = General(BLACK, unit_dict[BLACK][General])
                self.gameboard[(i, 5)] = Advisor(BLACK, unit_dict[BLACK][Advisor])
                self.gameboard[(i, 6)] = Elephant(BLACK, unit_dict[BLACK][Elephant])
                self.gameboard[(i, 7)] = Horse(BLACK, unit_dict[BLACK][Horse])
                self.gameboard[(i, 8)] = Chariot(BLACK, unit_dict[BLACK][Chariot])


    def main(self):
        """runs Xiangqi game"""
        self.print_board()

    def is_in_check(self, color):
        """checks for if general is in check"""
        general = General
        general_dict = {}
        piece_loc = {RED: [], BLACK: []}
        piece_unit = {RED: [], BLACK: []}
        for position, piece in self.gameboard.items():
            if type(piece):
                piece_loc[piece.Color].append(position)
                piece_unit[piece.Color].append(piece)
            if type(piece) == general:
                general_dict[piece.Color] = position
        if color == 'black':
            return self.can_see_general(piece_loc[BLACK], piece_loc[RED], piece_unit[BLACK], piece_unit[RED], general_dict[BLACK])
        if color == 'red':
            return self.can_see_general(piece_loc[RED], piece_loc[BLACK], piece_unit[RED], piece_unit[BLACK], general_dict[RED])

    def can_see_general(self, c_player_loc,  o_player_loc, c_player_unit, o_player_unit, general_pos):
        """"""
        for o_unit in o_player_unit:
            for c_unit in c_player_unit:
                for c_position in c_player_loc:
                    for o_position in o_player_loc:
                        for x_position in range(9):
                            for y_position in range(10):
                                if c_unit.is_valid(c_position, [x_position, y_position], self.player_turn, self.gameboard) and not\
                                        o_unit.is_valid(o_position, general_pos, self.player_turn, self.gameboard):
                                    #print(o_unit, " o_unit", o_position, " ", general_pos)
                                    return False

    def make_move(self, spos, epos):
        """function moves pieces on the board"""
        #print(self.gameboard)
        try:
            start = (int(spos[1:]) - 1, (ord(spos[0]) - 97))
            end = (int(epos[1:]) - 1, (ord(epos[0]) - 97))
            #print(start[0], start[1])
        except:
            print("error decoding input. please try again")
            return ((-1, -1), (-1, -1))
        try:
            target = self.gameboard[start[0], start[1]]
        except:
            print("could not find piece")
            target = None
        if target:
            #print("found " + str(target))
            if target.Color != self.player_turn:
                self.message = "you aren't allowed to move that piece this turn"
            if target.is_valid([start[0], start[1]], [end[0], end[1]], target.Color, self.gameboard):
                if self.is_in_check('red'):
                    print("checkmate")
                print("that is a valid move")
                self.gameboard[end[0], end[1]] = self.gameboard[start[0], start[1]]
                print(self.gameboard[end[0], end[1]], " gb ep")
                del self.gameboard[start[0], start[1]]
                self.print_board()  # Print the board
                if self.player_turn == RED:
                    self.player_turn = BLACK
                else:
                    self.player_turn = RED
            else:
                print("nope")
        else:
            self.message = "there is no piece in that space"



    def print_board(self):
        """prints board"""
        print("       A  |   B  |  C   |  D   |  E  |  F   |   G  |   H  |   I ")
        # loop is responsible for rows
        for i in range(0, 10):
            print("_" * 70)
            if i < 9:
                print(chr(i+1 + 48), end="  | ")
            elif i ==9:
                print("10", end="  | ")
            # loop is responsible for columns
            for j in range(0, 9):
                divider = self.gameboard.get((i, j), "    ")
                print(str(divider) + ' | ', end="")
            print()
        print("_" * 70)

class Piece:
    """class for pieces"""
    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.Color = color
        self.valid_location = []

    def __repr__(self):
        """"""
        return self.name

    def __str__(self):
        """function subs in the dictionary string"""
        return self.name

    def is_valid(self, start_pos, end_pos, Color, gameboard):
        """"""
        if self.available_moves(start_pos[0], start_pos[1], end_pos[0], end_pos[1], gameboard):
            return True
        return False

    def open_space(self, x1, x2, y1, y2, gameboard, m_dir, can_kill):
        """"""
        space = 0
        # Orthogonally Movement
        if m_dir == "right":
            space = y1 + 1
            while space <= y2:
                try:
                    gameboard[(x1, space)]
                except:
                    space += 1
                else:
                    if space != y2 and not can_kill and self.name == " 炮 " or self.name == " 砲 ":
                        return self.open_space(x1, x2, space + 1, y2, gameboard, "right", True)
                    if space == y2 and gameboard[(x1, space)].Color != self.Color:
                        return can_kill
                    return False
            return True
        if m_dir == "left":
            space = y1 - 1
            while space >= y2:
                try:
                    gameboard[(x1, space)]
                except:
                    space -= 1
                else:
                    if space != y2 and not can_kill and self.name == " 炮 " or self.name == " 砲 ":
                        return self.open_space(x1, x2, space - 1, y2, gameboard, "left", True)
                    if space == y2 and gameboard[(x1, space)].Color != self.Color:
                        return can_kill
                    return False
            return True
        if m_dir == "down":
            space = x1 + 1
            while space <= x2:
                try:
                    gameboard[space, y1]
                except:
                    space += 1
                else:
                    if space != x2 and not can_kill and self.name == " 炮 " or self.name == " 砲 ":
                        return self.open_space(space + 1, x2, y1, y2, gameboard, "down", True)
                    if space == x2 and gameboard[space, y1].Color != self.Color:
                        return can_kill
                    return False
            return True
        if m_dir == "up":
            space = x1 - 1
            while space >= x2:
                try:
                    gameboard[space, y1]
                except:
                    space -= 1
                else:
                    if space != x2 and not can_kill and self.name == " 炮 " or self.name == " 砲 ":
                        return self.open_space(space - 1, x2, y1, y2, gameboard, "up", True)
                    if space == x2 and gameboard[space, y1].Color != self.Color:
                        return can_kill
                    return False
            return True
        # Diagonally Movement
        if m_dir == "rightup":
            space = y1 + 1
            x1 -= 1
            while space <= y2:
                try:
                    gameboard[(x1, space)]
                except:
                    space += 1
                    x1 -= 1
                else:
                    if space == y2 and gameboard[(x1, space)].Color != self.Color:
                        return can_kill
                    return False
            return True
        if m_dir == "rightdown":
            space = y1 + 1
            x1 += 1
            while space <= y2:
                try:
                    gameboard[(x1, space)]
                except:
                    space += 1
                    x1 += 1
                else:
                    if space == y2 and gameboard[(x1, space)].Color != self.Color:
                        return can_kill
                    return False
            return True
        if m_dir == "leftup":
            space = x1 - 1
            y1 -= 1
            while space >= x2:
                try:
                    gameboard[space, y1]
                except:
                    space -= 1
                    y1 -= 1
                else:
                    if space == x2 and gameboard[space, y1].Color != self.Color:
                        return can_kill
                    return False
            return True
        if m_dir == "leftdown":
            space = x1 + 1
            y1 -= 1
            while space <= x2:
                try:
                    gameboard[space, y1]
                except:
                    space += 1
                    y1 -= 1
                else:
                    if space == x2 and gameboard[space, y1].Color != self.Color:
                        return can_kill
                    return False
            return True

    def boundary_checker(self, x, y):
        """checks if placement is within the board's boundary"""
        if x >= 0 and x < 10 and y >= 0 and y < 9:
            return True
        return False

    def no_conflict(self, gameboard, intial_color, x, y):
        if self.boundary_checker(x, y) and (((x, y)not in gameboard) or gameboard[(x, y)].Color != initial_color):  
            return True
        return False

    def ad_nauseum(self, x, y, gameboard, Color, intervals):
        answers = []
        for x_int, y_int in intervals:
            x_temp, y_temp = x + x_int, y + y_int
            while self.boundary_checker(x_temp, y_temp):
                target = gameboard.get((x_temp, y_temp), None)
                if target is None:
                    answers.append((x_temp, y_temp))
                elif target.Color != Color:
                    answers.append((x_temp, y_temp))
                    break
                else:
                    break
                x_temp = x_temp = x_int
                y_temp = y_temp + y_int
        return answers


def horse_list(x, y, int1, int2):
    """sepcifically for the horse, permutes the values needed around a position for noConflict tests"""
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]


def general_list(x, y):
    return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1),
            (x - 1, y - 1)]

class Chariot(Piece):
    """class for the chariot piece"""
    def available_moves(self, x1, y1, x2, y2, gameboard, Color=None):
        #print(x2, y2, " chariot")
        if Color is None: Color = self.Color
        if x1 == x2:  # horizontal
            if y1 < y2:  # move right
                return self.open_space(x1, x2, y1, y2, gameboard, "right", True)
            if y2 < y1:  # move left
                return self.open_space(x1, x2, y1, y2, gameboard, "left", True)
        if y1 == y2:  # Vertical
            if x1 < x2:  # move down
                return self.open_space(x1, x2, y1, y2, gameboard, "down", True)
            if x2 < x1:  # move Up
                return self.open_space(x1, x2, y1, y2, gameboard, "up", True)

class Horse(Piece):
    """class for the horse piece"""
    def available_moves(self, x1, y1, x2, y2, gameboard, Color=None):
        #print(x2, y2, " horse")
        valid_location = [(x1 - 2, y1 + 1), (x1 - 1, y1 + 2), (x1 + 1, y1 + 2), (x1 + 2, y1 + 1), (x1 + 2, y1 - 1),
                          (x1 + 1, y1 - 2), (x1 - 1, y1 - 2), (x1 - 2, y1 - 1), (x1 - 2, y1 + 1)]
        if Color is None: Color = self.Color
        if (x2, y2) in valid_location:
            if x1 + 2 == x2:  # move Down
                if self.open_space(x1, x1 + 1, y1, y1, gameboard, "down", False):
                    if y1 < y2:
                        return self.open_space(x1, x2, y1, y2, gameboard, "rightdown", True)
                    else:
                        return self.open_space(x1, x2, y1, y2, gameboard, "leftdown", True)
            if x1 - 2 == x2:  # move Up
                if self.open_space(x1, x1 - 1, y1, y1, gameboard, "up", False):
                    if y1 < y2:
                        return self.open_space(x1, x2, y1, y2, gameboard, "rightup", True)
                    else:
                        return self.open_space(x1, x2, y1, y2, gameboard, "leftup", True)
            if y1 - 2 == y2:  # move left
                if self.open_space(x1, x1, y1, y1 - 1, gameboard, "left", False):
                    if x1 < x2:
                        return self.open_space(x1, x2, y1, y2, gameboard, "leftup", True)
                    else:
                        return self.open_space(x1, x2, y1, y2, gameboard, "leftdown", True)
            if y1 + 2 == y2:  # move right
                if self.open_space(x1, x1, y1, y1 + 1, gameboard, "right", False):
                    if x1 < x2:
                        return self.open_space(x1, x2, y1, y2, gameboard, "rightup", True)
                    else:
                        return self.open_space(x1, x2, y1, y2, gameboard, "rightdown", True)

    def get_valid_location(self, x, y):
        return self.valid_location

class Elephant(Piece):
    """class for the elephant piece"""
    def available_moves(self, x1, y1, x2, y2, gameboard, Color=None):
        #print(x2, y2, " elephants")
        if Color is None: Color = self.Color
        # crossing river
        if Color == RED:
            if x2 >=6:
                return False
        else:
            if x2 <= 5:
                return False
        # digonal movement
        if x2 == x1 - 2 and y2 == y1 + 2:
            return self.open_space(x1, x2, y1, y2, gameboard, "rightup", True)
        if x2 == x1 + 2 and y2 == y1 + 2:
            return self.open_space(x1, x2, y1, y2, gameboard, "rightdown", True)
        if x2 == x1 - 2 and y2 == y1 - 2:
            return self.open_space(x1, x2, y1, y2, gameboard, "leftup", True)
        if x2 == x1 + 2 and y2 == y1 - 2:
            return self.open_space(x1, x2, y1, y2, gameboard, "leftdown", True)

class Advisor(Piece):
    """class for the advisor piece"""
    def available_moves(self, x1, y1, x2, y2, gameboard, Color=None):
        #print(x2, y2, " advisor")
        if Color is None: Color = self.Color
        #palace
        #red hori d-f (3, 5) and 2 vert
        # black hori 3, 5 and 8 vert
        if Color == RED:
            if y2 <= 2 or y2 >= 6 or x2 >= 3:
                return False
        if Color == BLACK:
            if y2 <= 2 or y2 >= 6 or x2 <= 6:
                return False
        if x2 == x1 - 1 and y2 == y1 + 1:
            return self.open_space(x1, x2, y1, y2, gameboard, "rightup", True)
        if x2 == x1 + 1 and y2 == y1 + 1:
            return self.open_space(x1, x2, y1, y2, gameboard, "rightdown", True)
        if x2 == x1 - 1 and y2 == y1 - 1:
            return self.open_space(x1, x2, y1, y2, gameboard, "leftup", True)
        if x2 == x1 + 1 and y2 == y1 - 1:
            return self.open_space(x1, x2, y1, y2, gameboard, "leftdown", True)

class General(Piece):
    """class for the general piece"""
    def available_moves(self, x1, y1, x2, y2, gameboard, Color=None):
        #print(x2, y2, " general")
        if Color is None: Color = self.Color
        if Color == RED:
            if y2 <= 2 or y2 >= 6 or x2 >= 3:
                return False
        if Color == BLACK:
            if y2 <= 2 or y2 >= 6 or x2 <= 6:
                return False
        if y1 + 1 == y2:
            return self.open_space(x1, x2, y1, y2, gameboard, "right", True)
        if y1 - 1 == y2:
            return self.open_space(x1, x2, y1, y2, gameboard, "left", True)
        if x1 + 1 == x2:
            return self.open_space(x1, x2, y1, y2, gameboard, "down", True)
        if x1 - 1 == x2:
            return self.open_space(x1, x2, y1, y2, gameboard, "up", True)
        #if in check, test all possible position of general (and units)
        #if still in check, checkmate
        #if player moves, -> in check,
        #test all possible movements of your own units against enemy that putting you in check
        #if all possible movements leads to check -> stalemate

class Cannon(Piece):
    """class for the cannon piece"""
    def available_moves(self, x1, y1, x2, y2, gameboard, Color=None):
        #print(x2, y2, " cannon")
        if Color is None: Color = self.Color
        if x1 == x2:  # horizontal
            if y1 < y2:  # move right
                return self.open_space(x1, x2, y1, y2, gameboard, "right", False)
            if y2 < y1:  # move left
                return self.open_space(x1, x2, y1, y2, gameboard, "left", False)
        if y1 == y2:  # Vertical
            if x1 < x2:  # move down
                return self.open_space(x1, x2, y1, y2, gameboard, "down", False)
            if x2 < x1:  # move Up
                return self.open_space(x1, x2, y1, y2, gameboard, "up", False)

class Soldier(Piece):
    """class for the soldier piece"""
    def available_moves(self, x1, y1, x2, y2, gameboard, Color=None):
        #print(x2, y2, " soldier")
        if Color is None: Color = self.Color
        # if not over river
        if Color == RED:
            if x1 + 1 == x2:
                return self.open_space(x1, x2, y1, y2, gameboard, "down", True)
            if x2 >=6:
                if y1 + 1 == y2:
                    return self.open_space(x1, x2, y1, y2, gameboard, "right", True)
                if y1 - 1 == y2:
                    return self.open_space(x1, x2, y1, y2, gameboard, "left", True)
        if Color == BLACK:
            if x1 - 1 == x2:
                return self.open_space(x1, x2, y1, y2, gameboard, "up", True)
            if x2 <= 5:
                if y1 + 1 == y2:
                    return self.open_space(x1, x2, y1, y2, gameboard, "right", True)
                if y1 - 1 == y2:
                    return self.open_space(x1, x2, y1, y2, gameboard, "left", True)
        return False



def main():

    game = Xiangqi()
    game.make_move('c1', 'e3')
    game.make_move('e7', 'e6')
    game.make_move('b1', 'd2')
    game.make_move('h10', 'g8')
    game.make_move('h1', 'i3')
    game.make_move('g10', 'e8')
    game.make_move('h3', 'g3')
    game.make_move('i7', 'i6')
    game.make_move('i1', 'h1')
    game.make_move('g7', 'g6')
    game.make_move('d2', 'f3')
    game.make_move('h8', 'i8')
    game.make_move('d1', 'e2')
    game.make_move('b8', 'd8')
    game.make_move('a1', 'd1')
    game.make_move('b10', 'c8')
    game.make_move('g4', 'g5')
    game.make_move('d10', 'e9')
    game.make_move('g5', 'g6')
    game.make_move('g8', 'f6')
    game.make_move('g3', 'g2')
    game.make_move('f6', 'e4')
    game.make_move('d1', 'd4')
    game.make_move('a10', 'b10')
    game.make_move('d4', 'e4')
    game.make_move('i8', 'i4')
    game.make_move('e1', 'd1')
    game.make_move('b10', 'b3')
    game.make_move('f3', 'e5')
    game.make_move('i10', 'i7')
    game.make_move('h1', 'h10')
    game.make_move('e6', 'e5')
    game.make_move('h10', 'f10')
    game.make_move('e10', 'f10')
    game.make_move('e4', 'i4')
    game.make_move('d1', 'e1')
    game.make_move('i7', 'd7')
    game.make_move('c4','c5')
    game.make_move('b3', 'b1')
    game.make_move('e2', 'd1')
    game.make_move('b1', 'd1')
    game.make_move('e1', 'e2')
    game.make_move('d7', 'd2')

if __name__ == '__main__':
    main()