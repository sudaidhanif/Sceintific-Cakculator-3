import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to plot the graph
def plot_function(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=str(func.__name__) + '(x)', color='b')
    plt.title(f"Graph of {func.__name__}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    st.pyplot(plt)

# Streamlit application
st.title("Scientific Graphical Calculator")

# Dropdown for function selection
function = st.selectbox("Choose a function:", 
                         ['sin', 'cos', 'tan', 'exp', 'log', 'polynomial'])

# Input for x-axis range
x_min = st.number_input("X min:", value=-10.0)
x_max = st.number_input("X max:", value=10.0)

# Polynomial coefficients input
if function == 'polynomial':
    coeffs_input = st.text_input("Enter coefficients (comma-separated):", "1,0")
    coeffs = [float(c) for c in coeffs_input.split(',')]
    func = lambda x: sum(c * x**i for i, c in enumerate(coeffs))
else:
    if function == 'sin':
        func = np.sin
    elif function == 'cos':
        func = np.cos
    elif function == 'tan':
        func = np.tan
    elif function == 'exp':
        func = np.exp
    elif function == 'log':
        func = np.log

# Button to plot the function
if st.button("Plot Function"):
    if x_min < x_max:
        plot_function(func, (x_min, x_max))
    else:
        st.error("Error: X min must be less than X max.")
