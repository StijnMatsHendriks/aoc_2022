
if __name__ == "__main__":
    cycles = {
        "noop": 1,
        "addx": 2
    }

    data = [line.strip('\n').split(' ') for line in open('input.txt').readlines()]

    register = 1
    register_history = [register]

    for line in data:
        if len(line) > 1:
            instruction, increase = line[0], int(line[1])
        else:
            instruction, increase = line[0], 0

        num_cycles = cycles[instruction]
        for i in range(0, num_cycles):
            register_history.append(register)
        register += increase

    relevant_cycles = [20 + i * 40 for i in range(6)]
    score = 0
    for cycle in relevant_cycles:
        score += register_history[cycle] * cycle
    print(score)


    drawing = [[None]*40 for i in range(6)]
    register_history = [register_history[1+40*i:1+40*(i+1)] for i in range(6)]
    for row_index, row in enumerate(register_history):
        for char_index, char in enumerate(row):
            if char_index in range(register_history[row_index][char_index]-1, register_history[row_index][char_index]+2):
                drawing[row_index][char_index] = '#'
            else:
                drawing[row_index][char_index] = '.'

    for row in drawing:
        print(row)



