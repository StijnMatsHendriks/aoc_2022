f = readlines(open("input.txt"))

let
cals_list = []
cals = 0
for snack in f
    if isempty(snack)
        push!(cals_list, cals)
        cals = 0
    else
        cals += parse(Int64, snack)
    end
end

a = maximum(cals_list)
b = sum(sort(cals_list)[end-2:end])

println(a, " ", b)
end