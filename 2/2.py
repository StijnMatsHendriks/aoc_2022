def solve_a(data, rules_win, rules_draw, score_form):
    scores = []
    for they, I in data:
        score = 0
        if I == rules_win[they]:
            score += 6
        elif I == rules_draw[they]:
            score += 3

        score += score_form[I]
        scores.append(score)
    return sum(scores)

def solve_b(data, rules_win, rules_draw, rules_lose, score_form):
    scores = []
    for they, I in data:
        score = 0
        if I == 'X':
            my_choice = rules_lose[they]
            score += score_form[my_choice]
        elif I == 'Y':
            my_choice = rules_draw[they]
            score += 3
            score += score_form[my_choice]
        else:
            my_choice = rules_win[they]
            score += 6
            score += score_form[my_choice]
        scores.append(score)
    return sum(scores)


d_win = {
    'C': 'X',
    'A': 'Y',
    'B': 'Z'
}

d_draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

d_lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}
scores_per_choice = {
    'X': 1,
    'Y': 2,
    'Z': 3
}



if __name__ == "__main__":
    data = [line.strip('\n').split(' ') for line in open('input.txt', 'r').readlines()]
    
    a = solve_a(data, d_win, d_draw, scores_per_choice)
    b = solve_b(data, d_win, d_draw, d_lose, scores_per_choice)
    print(a, b)

    
        


        