import random
 
 
def OneLongestNonDecreasing(prog):
    length, v, end = 0, 1, 0
    for i in range(1, len(prog)):
        if prog[i] >= prog[i - 1]:
            v += 1
        else:
            if v > length:
                length, end = v, i
            v = 1
 
    return length, end
 
 
def LongestNonDecreasingWithHighestSum(prog):
    length, v = 0, 1
    progressions = []
    for i in range(1, len(prog)):
        if prog[i] >= prog[i - 1]:
            v += 1
        else:
            if v >= length:
                length = v
                progressions.append(prog[i - v:i])
            v = 1
    max_sum = 0
    max_arr = []
    for p in [p for p in progressions if len(p) == length]:
        if sum(p) > max_sum:
            max_arr = p
            max_sum = sum(p)
 
    return max_sum, max_arr
 
 
progression = [random.randint(0, 100) for i in range(100)]
sub_length, index = OneLongestNonDecreasing(progression)
max_aggr, max_list = LongestNonDecreasingWithHighestSum(progression)
 
print("Generated array:")
print(', '.join([str(k) for k in progression]))
print("First longest non decreasing sub progression:")
print(f"{sub_length}:{[str(k) for k in progression[index - sub_length:index]]}")
print("Longest non decreasing sub progression with the biggest sum:")
print(f"{max_aggr}:{max_list}")
