import pdb
import lxml.html
import time
from urllib2 import urlopen
import os

class Cell:
  def __init__(self, value):
    self.value = int(value)
    self.possibilities = set([x for x in range(1,10)])

  def __repr__(self):
    return str(self.value)

class Generator:
  def __init__(self, difficulty = 2):
    self.difficulty = str(difficulty)
    self.boardarray = [] 

  def __repr__(self):
    return str(self.boardarray)

  def generate(self):
    html = urlopen("http://www.free-sudoku.com/sudoku.php?mode=%s" % (self.difficulty)).read()
    tree = lxml.html.fromstring(html)

    for i in range(81):
      i += 1
      self.boardarray.append(tree.get_element_by_id(str(i)).text_content())

    newarray = []
    for e in self.boardarray:
      if e == '':
        newarray.append('0')
      else:
        newarray.append(e)
    self.boardarray = ''.join(newarray)

class Board:
  def __init__(self):
    self.boardstring = '619030040270061008000047621486302079000014580031009060005720806320106057160400030'
    x = Generator()
    x.generate()
    self.boardstring = str(x)
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
        os.system('clear')
        x.ugly_print()
        time.sleep(0.2)

  def smart_solve(self):
    for cell in self.cells:
      if cell.value == 0:
        change = False
        for square in self.squares:
          if cell in square:
            for cell2 in square:
              if cell2.value == 0 and sorted(cell2.possibilities) == sorted(cell.possibilities) and cell2 != cell:
                change = True
            for cell3 in square:
              if cell3.value == 0 and cell3 != (cell2 or cell) and len(cell2.possibilities) == 2 and change == True:
                cell3.possibilities = list(set(cell3.possibilities) - set(cell.possibilities))
                # cell3.value = '*' + str(len(cell.possibilities))
              change=False

        for square in self.columns:
          if cell in square:
            for cell2 in square:
              if cell2.value == 0 and sorted(cell2.possibilities) == sorted(cell.possibilities) and cell2 != cell:
                change = True
            for cell3 in square:
              if cell3.value == 0 and cell3 != (cell2 or cell) and len(cell2.possibilities) == 2 and change == True:
                cell3.possibilities = list(set(cell3.possibilities) - set(cell.possibilities))
                # cell3.value = '*' + str(len(cell.possibilities))
              change=False

        for square in self.columns:
          if cell in square:
            for cell2 in square:
              if cell2.value == 0 and sorted(cell2.possibilities) == sorted(cell.possibilities) and cell2 != cell:
                change = True
            for cell3 in square:
              if cell3.value == 0 and cell3 != (cell2 or cell) and len(cell2.possibilities) == 2 and change == True:
                cell3.possibilities = list(set(cell3.possibilities) - set(cell.possibilities))
                # cell3.value = '*' + str(len(cell.possibilities))
              change=False

x = Board()


# pdb.set_trace()


while 0 in [cell.value for cell in x.cells]:
  x.simple_solve()
  x.smart_solve()

if 0 not in [cell.value for cell in x.cells]:
  print "Yatta!"

# x.ugly_print()
