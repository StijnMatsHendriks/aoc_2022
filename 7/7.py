def populate_folders_dict(data):
    folders = {}
    start_line = data[0].split(' ')[2]
    curr_line = start_line

    for line in data:
        if line.startswith('$ ls'):
            continue

        previous_line = curr_line
        if '$ cd' in line:
            curr_line = folders[curr_line]['from'] if line.startswith('$ cd ..') else curr_line + line[5:] + '/'
        curr_line = start_line if curr_line == '///' else curr_line

        if curr_line not in folders:
            folders[curr_line] = {"from": previous_line, "to": [], "size": 0}
        if line[0].isdigit():
            folders[curr_line]["size"] += int(line.split(' ')[0])
    return folders
def backtrack_sizes(folders):
    Q = [key for key in folders.keys() if not folders[key]['to']]

    visited = []
    while Q:
        curr_pos = Q.pop()
        if curr_pos != "/" and curr_pos not in visited:
            previous_pos = folders[curr_pos]['from']
            Q.insert(0, previous_pos)
            folders[previous_pos]['size'] += folders[curr_pos]['size']
            visited.append(curr_pos)
    return folders

def solve_a(folders):
    total_size= 0
    for k, v in folders.items():
        if v["size"] <= 100000:
            total_size += v["size"]
    return total_size

def solve_b(folders, total_space=70000000, needed_space=30000000):
    space_in_use = folders['/']['size']
    unused_space = total_space - space_in_use
    needed_difference = needed_space - unused_space

    folder_sizes = [folders[key]['size'] for key in folders.keys() if folders[key]['size'] >= needed_difference]
    return min(folder_sizes)

if __name__ == "__main__":
    data = [line.strip('\n') for line in open('input.txt').readlines()]
    folders = populate_folders_dict(data)
    folders = backtrack_sizes(folders)
    a = solve_a(folders)
    b = solve_b(folders)
    print(a, b)