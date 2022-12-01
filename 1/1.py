

def solve_a(data):
    big_carrier = max([sum(rations) for rations in data])
    return big_carrier


def solve_b(data):
    carriers_sorted = sorted([sum(rations) for rations in data])
    return sum(carriers_sorted[-3:])

if __name__ == "__main__":
    data = open('input.txt', 'r').read().split('\n\n')
    data = [rations.split('\n') for rations in data[:-1]]
    data = [[int(cals) for cals in rations] for rations in data]
    
    a = solve_a(data)

    b = solve_b(data)
    print(a, b)