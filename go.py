B = "black"
W = "white"

class Go:
  def __init__(self, height, width=0):
    if width==0:
      width = height
    self.size = {"height":height,"width":width}
    self.turn = B
    self.board = []
    self.moves = []
    for i in range(height):
      self.board.append([])
      for j in range(width):
        self.board[i].append(".")

  def get_position(self, pos):
    return pos

  def handicap_stones(self, num):
    if len(self.moves[]) !=0:
      raise Exception("InvalidHandicapException: game has already started")
    else:
      if self.size["height"] == 9 and self.size["width"] == 9:
        if num>=1 and num <=5:
          for i in range(num):
            self.place_stone("B", )
        else:
          raise Exception("InvalidHandicapException: invalid number of handicap stones")
      elif self.size["height"] == 13 and self.size["width"] == 13:
        if num>=1 and num <=9:
        else:
          raise Exception("InvalidHandicapException: invalid number of handicap stones")
      elif self.size["height"] == 19 and self.size["width"] == 19:
        if num>=1 and num <=9:
        else:
          raise Exception("InvalidHandicapException: invalid number of handicap stones")
      else:
        raise Exception("InvalidHandicapException: wrong board size")

  def move(self, coords):
    pass

  def pass_turn(self):
    pass

  def printBoard(self):
    if self.size["height"] < 10:
      cols=[32]
    else:
      cols=[32,32]
    for i in range(self.size["width"]):
      cols.append(ord("A")+i)
    cols=[chr(x) for x in cols]
    print("".join(cols))
    for row in range(self.size["height"]):
      if self.size["height"] < 10:
        print(self.size["height"]-row,end="")
      else:
        if self.size["height"]-row > 9:
          print(self.size["height"]-row,end="")
        else:
          print(" ",self.size["height"]-row,sep="",end="")
      for col in range(self.size["width"]):
        print(self.board[row][col],end="")
      print()
  def rollback(self, num):
    pass

game = Go(9)
game.printBoard()
