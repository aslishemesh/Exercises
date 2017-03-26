# Exercise3 - training.

player1_pick = ""
player2_pick = ""

# get the players answers
while player1_pick not in ['r', 'p', 's']:
    player1_pick = raw_input("Player 1 - please enter (r)ock, (p)aper or (s)cissors: ")
while player2_pick not in ['r', 'p', 's']:
    player2_pick = raw_input("Player 2 - please enter (r)ock, (p)aper or (s)cissors: ")

# create a tuple for decision
pair = (player1_pick, player2_pick)
# calc decision
if pair == ('r','r') or pair == ('p','p') or pair == ('s','s'): result = "    Draw !"
elif pair == ('p','r') or pair == ('s','p') or pair == ('r','s'): result = "    Player 1 wins !"
elif pair == ('r','p') or pair == ('p','s') or pair == ('s','r'): result = "    Player 2 wins !"

print "result ",result


print "Player 1 chose: ", player1_pick, " Player 2 chose: ", player2_pick

print result


