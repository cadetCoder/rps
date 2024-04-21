##########
# TASK 2 #
##########

# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = "22087552"

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"
#
# Please leave the next line unchanged
task = 'task2'
# ----------------------------------------------------------------------------------------------------------------------------
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of each
# method below that currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# DO NOT CHANGE the names or parameters of any of these methods
# DO NOT CHANGE the names of the four fields
# Make sure you read the method descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
#
# The script contains a class definition and a program that can
# be used to test its behaviour
#
# To run the program type  play_game()  at the command line in the
# Python shell
#
# ----------------------------------------------------------------------------------------------------------------------------

class peg_game () :
    # A class of objects that capture the state of a game that involves
    # inserting pegs into rows of holes in a board until all holes are full
    # The winner is the person who inserts the last peg(s)
    # At each turn the next player chooses how many pegs to insert into
    # the board. The pegs will always be put into the row that has the largest
    # number of empty holes
    # The maximum number of pegs that can be inserted at each turn is the
    # lower of maxplay and the number of empty holes in the most empty row
    # (see maxplay and max_pegs_this_turn below)
    #
    # Each peg_game object, P, has four fields:
    #  P.holes_per_row
    #             the number of holes per row
    #             P.holes_per_row is an int greater than 1
    #
    #  P.rows     the current number of empty holes in each row
    #             P.rows is a non-empty list of non-negative ints
    #
    #  P.maxplay  the absolute maximum number of pegs that a
    #             player is allowed to insert in one move
    #             P.maxplay is a positive int
    #
    #  P.next     the identity of the next player to play
    #             P.next is either 1 or 2

    def __init__ (self,row_count,holes) :
        # Creates a new peg_game object, using the parameters row_count
        # and holes, and sets the identity of the next player to 1
        # This method already works correctly. DO NOT CHANGE IT
        self.holes_per_row = holes      # Remains constant throughout the game
        self.rows = [holes] * row_count # The number of rows remains constant
                                        # The number of unfilled holes in each row
                                        # changes as the game is played
        self.maxplay = self.holes_per_row - 1 # Remains constant throughout the game
        self.next = 1   # Changes on each turn
        


    ####################
    # Method 1: 1 mark
    ####################
        # Returns the identity of the player whose turn
        # it is to play next (either 1 or 2)
    def next_player_ID (self) :
        # Insert function body to replace code stub

        return self.next


    ####################
    # Method 2: 2 marks
    ####################
        # Returns the identity of the player who played
        # the last turn (either 1 or 2)
    def previous_player_ID (self) :
        # Insert function body to replace code stub
        return self.next % 2 + 1
 


    ####################
    # Method 3: 3 marks
    ####################
        # Once the game has started there may not be enough empty holes
        # in any row to insert the maximum number of pegs that can
        # be played on any turn (self.maxplay)
        # This function returns the limit on the number of pegs that
        # can be inserted on the next turn. This is the
        # minimum of maxplay and the number of empty holes
        # in the most-empty row
        # Examples
        # if self.rows is [3,5,5,6] and self.maxplay is 5 the function returns 5
        # if self.rows is [3,3,4,4] and self.maxplay is 5 the function returns 4
        # if self.rows is [1,2,3] and self.maxplay is 4 the function returns 3
    def max_pegs_this_turn (self) :
        # Insert function body to replace code stub
          # Returns the limit on the number of pegs that can be inserted on the next turn
          # This is the minimum of maxplay and the number of empty holes in the most-empty row
          return min(self.maxplay, min(self.rows))


    ####################
    # Method 4: 1 mark
    ####################
        # Returns the total number of empty holes on the board
        # When this number is zero the game is over
    def empty_holes (self) :
        # Insert function body to replace code stub

        return sum(self.rows)


    ####################
    # Method 5: 3 marks 
    ####################
        # Inserts the number of pegs specified by the parameter
        # pegs_to_add and switches to the next player
        # Pegs are inserted in one row only, and that is always the
        # row with the largest number of empty holes
    def insert_pegs (self,pegs_to_add) :

        max_row = max(range(len(self.rows)), key=lambda i: self.rows[i])
        self.rows[max_row] -= pegs_to_add
        self.next = 2 if self.next == 1 else 1

        pass



# ----------------------------------------------------------------------------------------------------------------------------
# DO NOT CHANGE any part of this script between here and
# the end of the file
# ----------------------------------------------------------------------------------------------------------------------------

    def __str__ (self) :
        # Returns a string-based representation of the playing board
        # in a peg_game object so that it can be displayed using Python's
        # built-in print function
        # This method already works correctly
        board_as_string = ""
        for holes_in_row in self.rows :
            row_as_string = (self.holes_per_row - holes_in_row) * "T "
            row_as_string += holes_in_row * "o " + "\n"
            board_as_string += row_as_string
        return board_as_string

#################################################################################
# GAME PLAY

def play_game() :
    # Sets up and runs a peg game
    # Once you have got the peg_game class working you should
    # test it by setting up games with different sizes / numbers of rows
    # on the board
    # For example    game = peg_game(10,3)
    print ("Welcome to the peg game")
    while True :
        row_count = input("What is the number of rows? ")
        if row_count.isdigit() :
            row_count = int(row_count)
            if row_count >= 1 :
                break
            else :
                print ("Minimum number of rows is 1")
    while True :
        hole_count = input("What is the number of holes per row? ")
        if hole_count.isdigit() :
            hole_count = int(hole_count)
            if hole_count > 1 :
                break
            else :
                print ("Minimum number of holes per row is 2")
    game = peg_game(row_count,hole_count)
    print ("\nPlayers take it in turns to insert pegs into holes")
    print ("until all " + str(game.empty_holes()) + " holes are full\n")
    print ("You may insert between 1 and " + str(game.max_pegs_this_turn()) + " pegs into the board")
    print ("They will be put into the row with the largest number of empty holes")
    print ("The player who fills up the board is the winner\n")
    print ("Each empty hole is shown as an o")
    print ("Each hole containing a peg is shown as a T\n")
    playing = True
    while playing :
        print (game)
        next_player = game.next_player_ID()
        print ("It's player",next_player,"to play next")
        if input ("Quit the game (y/n)? ") in ['y','Y'] :
            break
        while True :
            prompt = "\nHow many pegs do you want to insert?\n"
            prompt += "(minimum is 1, maximum on this turn is " + str(game.max_pegs_this_turn()) + "): "
            n = input(prompt)
            if n.isdigit() :
                n = int(n)
            else :
                continue
            if n >= 1 and n <= game.max_pegs_this_turn() :
                print ()
                break
        game.insert_pegs(n)
        if game.empty_holes() == 0 :
            print ("Congratulations player",game.previous_player_ID(),"you win")
            playing = False
    print ("\nThank you for playing\nTo play again enter  play_game()  at the >>> prompt\n")


if input ("Play game (y/n)? ") in ["y","Y"] :
    print ()
    play_game ()
