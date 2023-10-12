# Define tha base class player

class player:
  def play(self):
    print("tha player is a playing cricket.")

# Defint the derived class Batsman

class Batsman (player):
  def play(self):
    print ("The batsman is batting.")

# Define the derived class Bow

class Bowler(player):
 def play(self):
   print ("The bowler is bowing.")
   
# creating objects of batsman and bowler classes

batsman = Batsman()
bowler = Bowler()
  
# call the play() method for each object

batsman.play()
bowler.play()
