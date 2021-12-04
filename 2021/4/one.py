def read_and_sanitize_input(path):
  # Read and sanitize input
  f = open(path,"r")
  raw_input = f.readlines()
  input = []
  for index, value in enumerate(raw_input):
    input.append(value.replace("\n",""))
  return input

def parse_input(input):
  numbers_drawn = input[0]
  boards = []
  tmp_board = []
  for index, value in enumerate(input):
    if index < 2:
      continue
    if input[index] == '':
      boards.append(tmp_board)
      tmp_board = []
      continue
    tmp_board.append(input[index])
  boards.append(tmp_board)
  return numbers_drawn, boards

def test():
  return parse_input(read_and_sanitize_input("2021/4/input.txt"))

#exec(open("2021/4/input.txt").read())
