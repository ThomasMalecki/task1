from simpleai.search import CspProblem, backtrack
words = []
word1 = input("Geef het eerste woord: ").upper()
words.append(word1)

word2 = input("Geef het tweede woord: ").upper()
words.append(word2)

word3 = input("Geef het derde woord: ").upper()
words.append(word3)

# Create a list of unique characters
variables = list(set(word1 + word2 + word3))

# Remove any non-alphabetical characters
variables = [char for char in variables if char.isalpha()]

domains = {}
# Make a domains object that defines the ranges of the chars first letters of words cannot have 0
for word in words:
    for i, char in enumerate(word):
        print(word[i])
        if i == 0:
            domains[char] = list(range(1, 10))
            print(i)
        else:
            domains[char] = list(range(10))

def constraint_unique(variables, values):
    return len(values) == len(set(values))

def constraint_add(variables, values):
    factor1 = ""
    factor2 = ""
    result = ""
    for char in words[0]:
        position = variables.index(char)
        factor1 += str(values[position])
    factor1 = int(factor1)
    for char in words[1]:
        position = variables.index(char)
        factor2 += str(values[position])
    factor2 = int(factor2)
    for char in words[2]:
        position = variables.index(char)
        result += str(values[position])
    result = int(result)
    return (factor1 + factor2) == result
#
constraints = [
    (variables, constraint_unique),
    (variables, constraint_add),
]
#here we use simpleAI to backtrack of a solution
problem = CspProblem(variables, domains, constraints)

output = backtrack(problem)

if output:
    solution = {var: output[var] for var in variables}
    
    print("\nDigits Solution:")
    for word in words:
        for char in word:
            if char.isalpha():
                print(solution[char], end=" ")
            else:
                print(char, end=" ")
        print()

    print("\nLetters Solution:")
    for word in words:
        for char in word:
            if char.isalpha():
                print(char, end=" ")
            else:
                print(char, end=" ")
        print()
else:
    print("No solution found.")