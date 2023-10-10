# 1. How does this solution ensure data immutability?

# 2. Is this solution a pure function? Why or why not?

# 3. Is this solution a higher order function? Why or why not?

# 4. Would it have been easier to solve this problem using a different programming style?

# 5. Why in particular is functional programming a helpful paradigm when solving this problem?


def flatten_and_sort(lst):
    out = []
    for item in lst:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)
    return sorted(out)

nested = [0, -2, 5, 4, [5, 344, 4, 19], [215, 8585965]]

out = flatten_and_sort(nested)
print(out)
print(nested)