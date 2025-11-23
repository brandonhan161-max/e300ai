# electronics_chatbot_web_with_diagrams.py
import streamlit as st
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Electronics Chatbot", layout="wide")

# ==============================================================
# OHM’S LAW CALCULATOR
# ==============================================================
def ohm_law(V, I, R):
    try:
        V = float(V) if V else None
        I = float(I) if I else None
        R = float(R) if R else None

        if V is None and I and R:
            return f"Voltage = {I * R} V"
        elif I is None and V and R:
            return f"Current = {V / R} A"
        elif R is None and V and I:
            return f"Resistance = {V / I} Ω"
        else:
            return "Enter any two values."
    except:
        return "Invalid input."

# ==============================================================
# SERIES & PARALLEL CALCULATOR
# ==============================================================
def sp_resistors(values):
    try:
        R = [float(x) for x in values.split(",")]
        series = sum(R)
        parallel = 1 / sum(1/r for r in R)
        return f"Series = {series} Ω\nParallel = {parallel:.3f} Ω"
    except:
        return "Invalid resistor list. Example: 10,5,20"

# ==============================================================
# ELECTRONICS PROBLEM SOLVER
# ==============================================================
def solve_problem(q):
    q = q.lower()

    if "ohm" in q:
        return (
            "**Ohm’s Law Explained**\n"
            "V = I × R\n\n"
            "Voltage = push of electrons\n"
            "Current = flow of electrons\n"
            "Resistance = opposition\n"
            "Change any one and the others adjust."
        )
    if "and gate" in q:
        return (
            "**AND Gate**\n"
            "Outputs 1 only if BOTH inputs are 1.\n"
            "Truth table:\n"
            "0 0 → 0\n0 1 → 0\n1 0 → 0\n1 1 → 1"
        )
    if "or gate" in q:
        return (
            "**OR Gate**\n"
            "Outputs 1 if ANY input is 1."
        )
    if "not gate" in q:
        return (
            "**NOT Gate**\n"
            "Outputs the opposite of input.\n"
            "0 → 1\n1 → 0"
        )

    if "v=" in q or "i=" in q or "r=" in q:
        V = I = R = None
        if "v=" in q: V = q.split("v=")[1].split()[0]
        if "i=" in q: I = q.split("i=")[1].split()[0]
        if "r=" in q: R = q.split("r=")[1].split()[0]
        return ohm_law(V, I, R)

    if "resistor" in q or "series" in q or "parallel" in q:
        nums = "".join([c for c in q if c.isdigit() or c == ","])
        if nums:
            return sp_resistors(nums)

    return "I can explain Ohm’s Law, logic gates, or solve resistor problems."

# ==============================================================
# CIRCUIT DIAGRAMS
# ==============================================================
def plot_series_circuit():
    fig, ax = plt.subplots(figsize=(5,2))
    ax.plot([0,1,2,3,4], [1,1,1,1,1], color='black')  # wire
    ax.text(1,1.05,'R1', fontsize=12)
    ax.text(3,1.05,'R2', fontsize=12)
    ax.axis('off')
    st.pyplot(fig)

def plot_parallel_circuit():
    fig, ax = plt.subplots(figsize=(5,3))
    ax.plot([0,4],[2,2], color='black')  # top wire
    ax.plot([0,4],[0,0], color='black')  # bottom wire
    ax.plot([1,1],[0,2], color='black')  # R1 vertical
    ax.plot([3,3],[0,2], color='black')  # R2 vertical
    ax.text(1,2.05,'R1', fontsize=12)
    ax.text(3,2.05,'R2', fontsize=12)
    ax.axis('off')
    st.pyplot(fig)

def plot_logic_gate(gate):
    fig, ax = plt.subplots(figsize=(5,3))
    if gate == "AND":
        ax.plot([0,1],[1,1], color='black')
        ax.plot([0,1],[0,0], color='black')
        ax.add_patch(plt.Circle((1.5,0.5),0.5,fill=False, color='black'))
        ax.plot([2,3],[0.5,0.5], color='black')
        ax.text(1.5,0.5,'AND', ha='center', va='center')
    elif gate == "OR":
        ax.plot([0,1],[0,0], color='black')
        ax.plot([0,1],[1,1], color='black')
        ax.plot([1,2],[0,0.5], color='black')
        ax.plot([1,2],[1,0.5], color='black')
        ax.plot([2,3],[0.5,0.5], color='black')
        ax.text(1.5,0.5,'OR', ha='center', va='center')
    elif gate == "NOT":
        ax.plot([0,1],[0.5,0.5], color='black')
        ax.plot([1,2],[0,1], color='black')
        ax.plot([1,2],[1,0], color='black')
        ax.add_patch(plt.Circle((2,0.5),0.05, fill=True, color='black'))
        ax.text(1.5,0.5,'NOT', ha='center', va='center')
    ax.axis('off')
    st.pyplot(fig)

# ==============================================================
# STREAMLIT UI
# ==============================================================

st.title("⚡ Electronics Chatbot + Diagrams")

# Chat input
st.subheader("Chat with the Bot")
user_input = st.text_input("Ask a question (Ohm's law, logic gates, series/parallel):")
if st.button("Send"):
    if user_input.strip() != "":
        answer = solve_problem(user_input)
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**Bot:** {answer}")

# Ohm's Law Calculator
st.subheader("🛠 Ohm’s Law Calculator")
col1, col2, col3 = st.columns(3)
with col1:
    V_input = st.text_input("Voltage (V)", key="V")
with col2:
    I_input = st.text_input("Current (I)", key="I")
with col3:
    R_input = st.text_input("Resistance (Ω)", key="R")
if st.button("Calculate Ohm’s Law"):
    result = ohm_law(V_input, I_input, R_input)
    st.success(result)

# Series/Parallel Calculator
st.subheader("🔗 Series/Parallel Resistor Calculator")
res_input = st.text_input("Enter resistor values separated by commas (e.g., 10,5,20)", key="resistors")
if st.button("Calculate Series/Parallel"):
    result = sp_resistors(res_input)
    st.success(result)

# Circuit Diagrams
st.subheader("📐 Circuit Diagrams")
if st.button("Show Series Circuit"):
    plot_series_circuit()
if st.button("Show Parallel Circuit"):
    plot_parallel_circuit()

# Logic Gate Images
st.subheader("💡 Logic Gate Diagrams")
gate_option = st.selectbox("Select a logic gate", ["AND", "OR", "NOT"])
if st.button("Show Logic Gate"):
    plot_logic_gate(gate_option)
