require 'open-uri'
require 'nokogiri'
require 'pry'

class BoardGenerator

  def self.generate(difficulty = 2)

    page = fetch_page(difficulty)
    boardarray = parse_page(page)

    Board.new(boardarray)
  end

  private

  def self.fetch_page(difficulty)
    Nokogiri::HTML(open("http://www.free-sudoku.com/sudoku.php?mode=#{difficulty}"))
  end


  def self.parse_page(page)
    (1..81).each_with_object([]) do |index, values|

      cell = page.css("##{index}").text
      values << (cell == '' ?  0 : cell)

    end.join
  end

end


binding.pry
