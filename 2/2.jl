# A
let 
f = readlines(open("input.txt"))

wins = ["A Y", "B Z", "C X"]
draws = ["A X", "B Y", "C Z"]


scores = Dict{Char, Integer}('X' => 1, 'Y' => 2, 'Z' => 3)
total_score = 0

for line in f
    opponent, me = line[1], line[3]
    total_score += scores[me]

    if line in wins
        total_score += 6
    elseif line in draws
        total_score += 3
    end

end
a = total_score
println(a)
end

# b
let 
f = readlines(open("input.txt"))

wins = ["A Y", "B Z", "C X"]
draws = ["A X", "B Y", "C Z"]
loses = ["A Z", "B X", "C Y"]

scores = Dict{Char, Integer}('X' => 1, 'Y' => 2, 'Z' => 3)
total_score = 0

for line in f
    opponent, result = line[1], line[3]
    if result == 'X'
        for choice in loses
            if choice[1] == opponent
                me = choice[3]
                total_score += scores[me]
            end
        end
    elseif result == 'Y'
        total_score += 3
        for choice in draws
            if choice[1] == opponent
                me = choice[3]
                total_score += scores[me]
            end
        end
    else
        total_score += 6
        for choice in wins
            if choice[1] == opponent
                me = choice[3]
                total_score += scores[me]
            end
        end
    end   
end

b = total_score
println(b)
end
