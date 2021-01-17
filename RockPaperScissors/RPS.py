import numpy as np

class RPS:
    
    def __init__(self):
        self.scb = [0, 0, 0]
        self.cont = True

    def play(self):
        try:
            
            num = int(input("Enter 1, 2, or 3. 1 is Rock, 2 is Paper, 3 is Scissors."))
            
            if num > 3:
                self.gameOver()
                return
    
        except TypeError:
            self.gameOver()
            return
            
        self.mvs = {1: 'Rock',
                    2: 'Paper',
                    3: 'Scissors'}

        move = np.random.randint(1,4)

        if (move - num == 1) or (move - num == -2):
            print("Computer won.")
            print("You played {} against CPU's {}".format(self.mvs[move], self.mvs[num]))
            self.scoreboard(1)
            self.play()

        elif (move == num):
            print("Tie.")
            print("You and CPU played {}.".format(self.mvs[move]))
            self.scoreboard(2)
            self.play()

        else:
            print("You won!")
            print("You played {} against CPU's {}".format(self.mvs[move], self.mvs[num]))
            self.scoreboard(0)
            self.play()
        
    def scoreboard(self, id):
        self.scb[id] += 1
    
    def printSCB(self):
        print("Player's Wins: {}".format(self.scb[0]))
        print("CPU's Wins: {}".format(self.scb[1]))
        print("Ties: {}".format(self.scb[2]))
        
    def gameOver(self):
        print("The game has concluded.")
        self.printSCB()
        self.cont = False
      
def main():
  g = RPS()
  while g.cont:
    g.play()
   
if __name__ == '__main__':
    main()
