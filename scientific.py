%%writefile app.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Define the functions to plot
def f1(x):
    return np.sin(x)

def f2(x):
    return np.cos(x)

def f3(x):
    return np.tan(x)

def f4(x):
    return x ** 2

def plot_function(func, x_range=(-10, 10), num_points=100):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=str(func.__name__))
    plt.title(f'Plot of {func.__name__}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    st.pyplot(plt)

# Streamlit app
st.title("Scientific Graphical Calculator")

st.sidebar.header("Select a Function")
function_choice = st.sidebar.selectbox(
    "Choose a function to plot:",
    ("sin(x)", "cos(x)", "tan(x)", "x^2")
)

x_range = st.sidebar.slider("Select x range:", -10.0, 10.0, (-10.0, 10.0))

if function_choice == "sin(x)":
    plot_function(f1, x_range)
elif function_choice == "cos(x)":
    plot_function(f2, x_range)
elif function_choice == "tan(x)":
    plot_function(f3, x_range)
elif function_choice == "x^2":
    plot_function(f4, x_range)
