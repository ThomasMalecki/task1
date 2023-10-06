import streamlit as st
from simpleai.search import CspProblem, backtrack

# Function to solve the CSP problem
def solve_csp(word1, word2, word3):
    # ... (Your existing solve_csp function)

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
            
            # Display the math question layout
            st.markdown("<h3>Math Question:</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{word1} + {word2} = {word3}</p>", unsafe_allow_html=True)
            
            # Display the solution in digits
            st.markdown("<h3>Solution in Digits:</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{' '.join([str(solution[char]) if char.isalpha() else char for char in word1])} + " \
                        f"{' '.join([str(solution[char]) if char.isalpha() else char for char in word2])} = " \
                        f"{' '.join([str(solution[char]) if char.isalpha() else char for char in word3])}</p>",
                        unsafe_allow_html=True)
        else:
            st.write("No solution found.")
