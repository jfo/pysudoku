require 'open-uri'
require 'nokogiri'
require 'pry'
require 'set'



def fetch_new_puzzle(difficulty)

  tree = Nokogiri::HTML(open("http://www.free-sudoku.com/sudoku.php?mode=#{difficulty}"))
  board = new_board

  (0..8).product(0..8) do |x,y|
    id = (x * 9) + y + 1
    text_content = tree.css("##{index}").text
    value = text_content.is_a?(Integer) ? text_content.to_i : nil
    board[[x,y]] = value
  end

end


def to_square(position)
   # Convert a position array to a square number as an int,
   # 0 through 8, corresponding to the square on the
   # sudoku board.

  x, y = position
  hyper_row = x / 3
  hyper_column y / 3

  return (hyper_row * 3) + hyper_column
end



def new_board
  dict = {}

  (0..8).product(0..8).each do |x,y|
    dict[[x,y]] = nil
  end

end

def new_possible()
  # """Make a new blank possibilities dict."""

  possible_dict= {}

  (0..8).product(0..8).each do |x,y|
    possible_dict[x,y] = (1..9).to_set
  end

  return possible_dict
end


def print_board(board)
  # """Pretty-print a board."""

  (0..8).each do |row|
    (0..8).each do |col|
      tokens = board[row, col] || '.'
    end
    print tokens.join(' ')
  end
end

def deterministic_solve(board, possible)

  board = board.dup
  possible = possible.dup

  last_board = nil
  while board != last_board
    last_board = dict(board)
    print '================='
    print_board(board)

    board.keys.each do |cell|
      if board[cell]
        possible[cell] = board.cell.to_set
      end
    end
end
















