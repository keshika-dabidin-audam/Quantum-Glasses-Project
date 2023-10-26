import os
from platform import system
import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL
import warnings
import numpy as np
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

# Ignore unnecessary warnings
warnings.simplefilter("ignore")

## Initialize the circuit
def initialize_circuit():
        """ 
        Initializes a quantum circuit
        """
        global circuit
        circuit=QuantumCircuit(1) # Passing one qubit
        return circuit

# Functions for RX,RY,RZ
# Defining colors and fonts - source to find color codes - imagecolorpicker
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font= ('Arial', 18)
display_font = ('Arial', 32) 
## Change theta function
def change_theta(num,window,circuit,key):
    """
    CHanges the global variable theta and destroys the window
    """
    global theta
    theta = num * np.pi
    if key=='x':
        circuit.rx(theta,0)
        theta = 0
    elif key=='y':
        circuit.ry(theta,0)
        theta = 0
    else:
        circuit.rz(theta,0)
        theta = 0
    window.destroy()

## Input function
def user_input(circuit,key):
    """
    Take the user input for rotation angle for parameterized
    Rotation gates Rx, Ry, Rz.
    """

    # Initialize and define the properties of window
    get_input = tkinter.Tk()
    get_input.title('Get Theta')
    get_input.geometry('360x160')
    get_input.resizable(0,0)

    val1 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='PI/4',command=lambda:change_theta(0.25,get_input,circuit,key))
    val1.grid(row=0, column=0)

    val2 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='PI/2',command=lambda:change_theta(0.50,get_input,circuit,key))
    val2.grid(row=0, column=1)

    val3 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='PI',command=lambda:change_theta(1.0,get_input,circuit,key))
    val3.grid(row=0, column=2)

    val4 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='2*PI',command=lambda:change_theta(2.0,get_input,circuit,key))
    val4.grid(row=0, column=3,sticky='W')

    nval1 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-PI/4',command=lambda:change_theta(-0.25,get_input,circuit,key))
    nval1.grid(row=1, column=0)

    nval2 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-PI/2',command=lambda:change_theta(-0.50,get_input,circuit,key))
    nval2.grid(row=1, column=1)

    nval3 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-PI',command=lambda:change_theta(-1.0,get_input,circuit,key))
    nval3.grid(row=1, column=2)

    nval4 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-2*PI',command=lambda:change_theta(-2.0,get_input,circuit,key))
    nval4.grid(row=1, column=3,sticky='W')

    text_object = tkinter.Text(get_input, height = 20, width = 20,bg="light cyan")

    note = """
    GIVE THE VALUE FOR THETA
    The value has the range [-2*PI,2*PI]
    """

    text_object.grid(sticky='WE',columnspan=4)
    text_object.insert(END,note)


# About button function
def about():
        """
        Displays the info about the project!
        """
        info = tkinter.Tk()
        info.title('About')
        info.geometry('650x500')
        # info.resizable(0,0)

        text = tkinter.Text(info, height = 20, width = 20)

        # Create label
        label = tkinter.Label(info, text = "About Quantum Glasses:")
        label.config(font =("Arial", 14))


        text_to_display = """ 
        About: Visualization tool for Single Qubit Rotation on Bloch Sphere
    
        
        Created using: Python, Tkinter, Qiskit
    
        Info about the gate buttons and corresponding qiskit commands:
    
        X = flips the state of qubit -                                 circuit.x()
        Y = rotates the state vector about Y-axis -                    circuit.y()
        Z = flips the phase by PI radians -                            circuit.z()
        Rx = parameterized rotation about the X axis -                 circuit.rx()
        Ry = parameterized rotation about the Y axis.                  circuit.ry()
        Rz = parameterized rotation about the Z axis.                  circuit.rz()
        S = rotates the state vector about Z axis by PI/2 radians -    circuit.s()
        T = rotates the state vector about Z axis by PI/4 radians -    circuit.t()
        Sd = rotates the state vector about Z axis by -PI/2 radians -  circuit.sdg()
        Td = rotates the state vector about Z axis by -PI/4 radians -  circuit.tdg()
        H = creates the state of superposition -                       circuit.h()
    
        For Rx, Ry and Rz, 
        theta(rotation_angle) allowed range in the app is [-2*PI,2*PI]
    
        In case of a Visualization Error, the app closes automatically.
        This indicates that visualization of your circuit is not possible.
    
        At a time, only ten operations can be visualized.
        """

        label.pack()
        text.pack(fill='both',expand=True)

        # Insert the text
        text.insert(END,text_to_display)

        # Run
        info.mainloop()

# Define the function for visualize button
def visualize_circuit(circuit,window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a separate tkinter window.
    Handles any possible visualization error
    """
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()


