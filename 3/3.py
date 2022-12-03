import string

def check_overlap(data):
    data = [list(set(item[0]).intersection(item[1]))[0] for item in data]
    return data

def check_overlap_groups_3(data):
    new_data = []
    letters = string.ascii_letters
    for group in data:
        elf1, elf2, elf3 = group
        overlap_elf12 = set(elf1).intersection(elf2)
        overlap_all = overlap_elf12.intersection(elf3)
        prio = letters.index(list(overlap_all)[0])+1
        new_data.append(prio)
    return new_data

def split_pack_in_comps(data):
    data = [[rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]] for rucksack in data]
    return data

def get_groups(data):
    data = [data[index:index+3] for index, rucksack in enumerate(data) if index % 3 == 0]
    return data

def solve_a(data):
    data = split_pack_in_comps(data)
    data = check_overlap(data)
    letters = string.ascii_letters
    data = [letters.index(item[0])+1 for item in data]
    return sum(data)

def solve_b(data):
    data = get_groups(data)
    data = check_overlap_groups_3(data)
    return sum(data)





if __name__ == "__main__":
    data = [rucksack.strip('\n') for rucksack in open('input.txt').readlines()]
  
    a = solve_a(data)
    b = solve_b(data)
    print(a, b)
