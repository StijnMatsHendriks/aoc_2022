def prep_data(file):
    data = [part for part in open(file).read().split('\n\n')]
    crates = [data[0].split('\n')][0]

    crates_list = [[] for i in range(9)]
    for row in crates[:-1]:
        for index, char in enumerate(row):
            if char != ' ' and index % 4 == 1:
                crates_list[(index // 4)].append(char)
    crates_list = [crate_list[::-1] for crate_list in crates_list]

    instructions = [row.split(' ') for row in data[1].split('\n')]
    return crates_list, instructions

def solve_b(crates_list, instructions):
    for instruction in instructions:
        num = int(instruction[1])
        from_row = int(instruction[3])-1 # indexing at 0
        to_row = int(instruction[5])-1 # indexing at 0

        for move_num in crates_list[from_row][-num:]:
            crates_list[to_row].append(move_num)
        for remove_num in range(num):
            crates_list[from_row].pop()
    
    ans = ""
    for crate in crates_list:
        ans += crate[-1]
    return ans

def solve_a(crates_list, instructions):
    for instruction in instructions:
        num = int(instruction[1])
        from_row = int(instruction[3])-1 # indexing at 0
        to_row = int(instruction[5])-1 # indexing at 0

        for move_num in crates_list[from_row][-num:][::-1]:
            crates_list[to_row].append(move_num)
        for remove_num in range(num):
            crates_list[from_row].pop()
    
    ans = ""
    for crate in crates_list:
        ans += crate[-1]
    return ans

if __name__ == "__main__":
    crates_list, instructions = prep_data('input.txt')
    a = solve_a(crates_list, instructions)

    crates_list, instructions = prep_data('input.txt')
    b = solve_b(crates_list, instructions)
    print(a, b)




    


    
        
