def solve(data, length):
    for index, char in enumerate(data):
        slice = data[index:index+length]
        if len(list(set(list(slice)))) == length:
            return index + length
           

if __name__ == "__main__":
    data = open('input.txt').read()
    a = solve(data, 4)
    b = solve(data, 14)
    print(a, b)