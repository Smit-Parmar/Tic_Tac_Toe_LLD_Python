class Player:
    def __init__(self,name):
        self.name=name

class Grid(Player): #Class to check grid is full or not , player move validation

    def __init__(self):
        # self.grid=[["-" for x in range(3)] for _ in range(3)]
        self.grid=[[1,2,3],[4,5,6],[7,8,9]]
        
    def showGrid(self): #To print grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j],end=" ")
            print()
        
    def checkWinner(self):

        #check horizontally
        for i in range(len(self.grid)):
            flag=True
            syb=self.grid[i][0]
            for j in range(len(self.grid)):
                if self.grid[i][j]!=syb:
                    flag=False
                    continue
            if flag:
                return True

        #check vertically
        for i in range(len(self.grid)):
            flag=True
            syb=self.grid[0][i]
            for j in range(len(self.grid)):
                if self.grid[j][i]!=syb:
                    flag=False
                    continue
            if flag:
                return True

        #Check diagonally
        start=self.grid[0][0]
        if self.grid[1][1] == start and self.grid[2][2]==start:
            return True
        start=self.grid[2][0]
        if self.grid[1][1] == start and self.grid[0][2]==start:
            return True
        return False

class Game(Grid):
    def __init__(self,player1,player2):
        self.turn=True #If true then player1 turn
        self.winner=False
        self.player1=player1
        self.player2=player2
        Grid.__init__(self)
        self.grid_size=len(self.grid) * len(self.grid)
        self.move_count=self.grid_size
        
    def makeMove(self,position,symbol): #Insert player symbol into grid
        if position > self.grid_size:
            print("Invalid position please enter again")
            return False
        row=position//len(self.grid)
        col=position%len(self.grid)
        if col==0:
            col=len(self.grid)
            row-=1
        if str(self.grid[row][col-1]).isdigit():
            self.grid[row][col-1]=symbol
            return True
        else:
            self.showGrid()
            print("Position already filled")
            return False

    def startGame(self): #To play game until winner is not decided or draw
        while self.winner or self.move_count!=0:
            if self.turn : #player 1 turn 
                position=int(input(f"{self.player1.name} turn! Where you want to insert X :"))
                if not self.makeMove(position,"X"): #if player has entered invalid position or position already filled 
                    continue
                if self.checkWinner():
                    self.winner=True
                    self.showGrid()
                    print(f"Winner is {self.player1.name}")
                    break

                self.turn =False
            else:
                position=int(input(f"{self.player2.name} turn!. Where you want to insert O :"))
                if not self.makeMove(position,"O"): #if player has entered invalid position or position already filled 
                    continue
                if self.checkWinner():
                    self.winner=True
                    self.showGrid()
                    print(f"Winner is {self.player2.name}")
                    break

                self.turn =True
            self.move_count-=1
            self.showGrid()

        if not self.winner:
            print("==========")
            self.showGrid()
            print("Match is tied")


if __name__ =="__main__":
    player1=Player(input("Please enter player1 name: "))
    player2=Player(input("Please enter player1 name: "))
    newgame=Game(player1,player2)
    newgame.showGrid()
    newgame.startGame()


