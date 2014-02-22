import pdb

class Cell:
  def __init__(self, value):
    self.value = int(value)
    self.possibilities = set([x for x in range(1,10)])

  def __repr__(self):
    return str(self.value)


class Board:
  def __init__(self, boardstring='000000000111111111222222222333333333444444444555555555666666666777777777888888888'):
    self.boardstring = boardstring
    self.boardstring = '619030040270061008000047621486302079000014580031009060005720806320106057160400030'
    self.setup()

  def setup(self):
    self.cells = list(self.boardstring)
    self.cells = [Cell(slot) for slot in self.cells]

    self.rows= [self.cells[i:i+9] for i in range(0,len(self.cells),9)]

    self.columns = [[],[],[],[],[],[],[],[],[]]

    for column in range(9):
      self.columns[column] = self.cells[column::9]

    self.squares = [[],[],[],[],[],[],[],[],[]]

    for i in range(0, 9, 3):
      for row in self.rows[i:i+3]:
        for cell in row[:3]:
          self.squares[i].append(cell)

      for row in self.rows[i:i+3]:
        for cell in row[3:6]:
          self.squares[i + 1].append(cell)

      for row in self.rows[i:i+3]:
        for cell in row[6:]:
          self.squares[i + 2].append(cell)


  def ugly_print(self):
    line = "---------------------------------------------------"

    print line
    for i in range(3):
      print ' '.join([str(x) for x in self.rows[i]])
    print line
    for i in range(3):
      print ' '.join([str(x) for x in self.rows[i + 3]])
    print line
    for i in range(3):
      print ' '.join([str(x) for x in self.rows[i + 6]])
    print line




  def simple_solve(self):
    for cell in self.cells:
      if cell.value == 0:

        for row in self.rows:
          if cell in row:
            for cell2 in row:
              if cell2.value in cell.possibilities: 
                cell.possibilities.remove(cell2.value)

        for column in self.columns:
          if cell in column: 
            for cell2 in column:
              if cell2.value in cell.possibilities:
                cell.possibilities.remove(cell2.value)

        for square in self.squares:
          if cell in square: 
            for cell2 in square:
              if cell2.value in cell.possibilities:
                cell.possibilities.remove(cell2.value)

      if len(cell.possibilities) == 1:
        cell.value =  cell.possibilities.pop()


x = Board()
x.simple_solve()
pdb.set_trace()
