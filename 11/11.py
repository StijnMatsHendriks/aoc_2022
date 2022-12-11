import re
from functools import partial
from tqdm import tqdm
import gc
import math

def decrease_worry_level(worry_number, method):
    if method == 'lcm':
        worry_number = worry_number % lcm
        return worry_number
    else:
        return int(worry_number/3)

def parse_text(text):

    monkey = text.split('\n')
    starting_items = [int(char) for char in monkey[1].split(': ')[1].split(', ')]
    div_num = int(monkey[3].split(' ')[-1])
    div_true = int(monkey[4].split(' ')[-1])
    div_false = int(monkey[5].split(' ')[-1])

    if '*' in monkey[2]:
        x, y = monkey[2].split('= ')[-1].split(' * ')
        func = partial(mul_constant, int(y)) if y.isdigit() else square
    else:
        x, y = monkey[2].split('= ')[-1].split(' + ')
        func = partial(add_constant, int(y)) if y.isdigit() else double
    return starting_items, div_num, div_true, div_false, func

def add_constant(constant, old_val):
    return old_val + constant

def mul_constant(constant, old_val):
    return old_val * constant

def square(val):
    return val * val

def double(val):
    return val+val

class Monkey:
    def __init__(self, starting_items, div_num, div_true, div_false, operation, method):
        self.starting_items = starting_items
        self.div_num = div_num
        self.div_true = div_true
        self.div_false = div_false
        self.operation = operation
        self.inspected_items = 0
        self.method = method

    def list_items(self):
        return self.starting_items

    def exchange_item(self, item, monkey):
        self.throw_item()
        monkeys[monkey].catch_item(item)

    def throw_item(self):
        self.starting_items.pop(0)

    def catch_item(self, item):
        self.starting_items.append(item)

    def inspect_item(self, item):
        item = self.operation(item)
        item = decrease_worry_level(item, self.method)
        monkey = self.test(item)
        self.exchange_item(item, monkey)
        self.inspected_items += 1

        del monkey # cleanup

    def inspect_items(self):
        while self.starting_items:
            item = self.starting_items[0]
            self.inspect_item(item)

            del item # cleanup
            gc.collect()

    def test(self, num):
        if num % self.div_num == 0:
            return self.div_true
        else:
            return self.div_false

if __name__ == "__main__":
    data = open('input.txt').read().split('\n\n')
    monkeys = {index: Monkey(*parse_text(text), method='lcm') for index, text in enumerate(data)}

    global lcm
    lcm = math.lcm(*[monkey.div_num for monkey in monkeys.values()])
    num_rounds = 10000
    num_monkeys = len(data)

    for round in tqdm(range(num_rounds)):
        for monkey in range(num_monkeys):
            monkeys[monkey].inspect_items()

    inspected_items = sorted([(monkeys[monkey].inspected_items, monkey) for monkey in range(num_monkeys)])

    print(inspected_items)
    a = inspected_items[-2][0] * inspected_items[-1][0]
    print(a)



