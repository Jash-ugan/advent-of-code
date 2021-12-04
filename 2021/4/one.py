def read_and_sanitize_input(path):
  # Read and sanitize input
  f = open(path,"r")
  raw_input = f.readlines()
  input = []
  for index, value in enumerate(raw_input):
    input.append(value.replace("\n",""))
  return input

def parse_input(input):
  # Save number draw
  numbers_drawn = input[0]

  # Parse boards
  boards = []
  tmp_board = []

  for index, value in enumerate(input):

    # Skipp numbers drawn and first empty row
    if index < 2:
      continue

    # If there is an empty line this is an indicator for the next board
    if input[index] == '':
      boards.append(tmp_board)
      tmp_board = []
      continue

    line_strs = list(filter(None, value.split(" ")))
    line_ints = [int(strings) for strings in line_strs]

    tmp_board.append(line_ints)

  boards.append(tmp_board)
  return numbers_drawn, boards

def mark_number(current_number):
  global checkboards
  for board_nr, board in enumerate(boards):
    for y in range(0,number_of_lines):
      for x in range(0,number_of_numbers_in_line):
        if board[y][x] == current_number:
          checkboards[board_nr][y][x] = 1
    

input                     = read_and_sanitize_input("2021/4/input.txt")
numbers_drawn, boards     = parse_input(input)
number_of_boards          = len(boards)
number_of_lines           = len(boards[0])
number_of_numbers_in_line = len(boards[0][0])

checkboards = []
empty_line = []

for i in range(0, number_of_numbers_in_line): empty_line.append(0)
for i in range(0,number_of_boards): checkboards.append(empty_line)

mark_number(20)
print(check_board[0])

# for current_number in numbers_drawn:
#   mark_number(current_number)
#   check_winner()

#exec(open("2021/4/input.txt").read())
