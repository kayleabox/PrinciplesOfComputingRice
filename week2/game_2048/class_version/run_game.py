from game_template import TwentyFortyEight

print "DOWN"
game = TwentyFortyEight(4, 3)
game.reset()
game.new_tile()
game.new_tile()
print game.__str__()
game.move(2)
print game.__str__()

print "UP"
game = TwentyFortyEight(4, 3)
game.reset()
game.new_tile()
game.new_tile()
print game.__str__()
print "\n"
game.move(1)
print game.__str__()

print "RIGHT"
game = TwentyFortyEight(4, 3)
game.reset()
game.new_tile()
game.new_tile()
print game.__str__()
print "\n"
game.move(4)
print game.__str__()

print "LEFT"
game = TwentyFortyEight(4, 5)
game.reset()
game.new_tile()
game.new_tile()
print game.__str__()
print "\n"
game.move(3)
print game.__str__()
