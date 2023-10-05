import streamlit as st
from simpleai.search import CspProblem, backtrack

# Function to solve the CSP problem
def solve_csp(word1, word2, word3):
    words = [word1, word2, word3]

    # Create a list of unique characters
    variables = list(set(word1 + word2 + word3))

    # Remove any non-alphabetical characters
    variables = [char for char in variables if char.isalpha()]

    domains = {}
    # Make a domains object that defines the ranges of the characters; first letters of words cannot have 0
    for word in words:
        for i, char in enumerate(word):
            if i == 0:
                domains[char] = list(range(1, 10))
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

    constraints = [
        (variables, constraint_unique),
        (variables, constraint_add),
    ]

    # Create the CSP problem
    problem = CspProblem(variables, domains, constraints)

    # Solve the CSP problem
    output = backtrack(problem)

    if output:
        solution = {var: output[var] for var in variables}
        return solution
    else:
        return None

# Streamlit UI
st.title("CSP Solver")
st.write("Enter three words to find a valid digit assignment:")

word1 = st.text_input("Enter the first word:")
word2 = st.text_input("Enter the second word:")
word3 = st.text_input("Enter the third word:")

if st.button("Solve"):
    if word1 and word2 and word3:
        word1 = word1.upper()
        word2 = word2.upper()
        word3 = word3.upper()
        
        solution = solve_csp(word1, word2, word3)
        
        if solution:
            st.write("Solution Found:")
            st.write("Digits Solution:")
            for word in [word1, word2, word3]:
                for char in word:
                    if char.isalpha():
                        st.write(solution[char], end=" ")
                    else:
                        st.write(char, end=" ")
                st.write("\n")
        else:
            st.write("No solution found.")
