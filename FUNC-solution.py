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

'''
# 1. How does this solution ensure data immutability?
This solution ensures data immutability by not modifying the original nested list (lst) that is passed as an argument to the flatten_and_sort function. Instead, it creates a new list (out) to hold the flattened and sorted elements. The original nested list remains unchanged after calling the function. In functional programming, immutability is a key principle, and this solution adheres to it by not altering the input data.

2. Is this solution a pure function? Why or why not?
This is not a pure function because it sorts the out list, which can be considered a side effect. A pure function should have no side effects and should not modify any external state. Sorting the out list inside the function affects the order of elements, which is a side effect.

3. Is this solution a higher order function? Why or why not?
No, this solution is not a higher-order function. A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. The flatten_and_sort function operates on a list but does not take or return functions as arguments or results. It is a standard function for list manipulation.

4. Would it have been easier to solve this problem using a different programming style?
The approach taken in this code is quite common for flattening and sorting a nested list in an imperative style. However, functional programming provides a more declarative and concise way to solve this problem. Using functional programming constructs like list comprehensions and higher-order functions, you can often write such code more elegantly. In Python, you can achieve the same result using itertools.chain and sorted with a key function.

5. Why in particular is functional programming a helpful paradigm when solving this problem?
Functional programming encourages immutability and the use of pure functions, which can lead to code that is easier to reason about, test, and maintain. It promotes a declarative style, which can make your code more concise and expressive. Functional programming constructs like list comprehensions, map, and filter can simplify tasks like flattening and transforming data structures. In this specific problem, functional programming can help you write code that is both efficient and clear in its intent.
'''