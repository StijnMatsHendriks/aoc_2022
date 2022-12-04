def solve_a(data):
    overlap = 0
    for line in data:
        elf1, elf2 = line
        start1, stop1 = elf1
        start2, stop2 = elf2
        num_range1 = list(range(int(start1),int(stop1)+1))
        num_range2 = list(range(int(start2), int(stop2)+1))
        if all([num in num_range1 for num in num_range2]) or all([num in num_range2 for num in num_range1]):
            overlap += 1
    return overlap

def solve_b(data):
    overlap = 0
    for line in data:
        elf1, elf2 = line
        start1, stop1 = elf1
        start2, stop2 = elf2
        num_range1 = list(range(int(start1),int(stop1)+1))
        num_range2 = list(range(int(start2), int(stop2)+1))
        if any([num in num_range1 for num in num_range2]) or any([num in num_range2 for num in num_range1]):
            overlap += 1
    return overlap

if __name__ == "__main__":
    data = [line.strip('\n').split(',') for line in open('input.txt').readlines()]
    data = [[num_range.split('-') for num_range in line] for line in data]

    overlap_a = solve_a(data)
    overlap_b = solve_b(data)
    print(overlap_a, overlap_b)