import qiskit as qiskit
import tkinter 
from tkinter import LEFT
from functions import *

# Define window 
root=tkinter.Tk()
root.title('Quantum Glasses')

# Set the icon
root.iconbitmap(default='logo.ico')
root.geometry('399x425') # size of window
root.resizable(0,0) # Blocking the resizing feature

# Defining colors and fonts - source to find color codes - imagecolorpicker
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font= ('Arial', 18)
display_font = ('Arial', 32)

# Define functions
# Displaying quantum gate buttons function
def display_gate(gate_input):
        """
        Adds a corresponding gate notation in the display to track the operations.
        If the number of operation reach ten, all gate buttons are disabled.
        """
        # Insert the defined gate
        display.insert(END,gate_input)

        # Check if the number of operations has reached ten, if yes,
        # disable all the gate buttons
        input_gates = display.get()
        num_gates_pressed = len(input_gates)
        list_input_gates = list(input_gates)
        search_word = ["R","D"]
        count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
        num_gates_pressed-=sum(count_double_valued_gates)
        if num_gates_pressed==10:
            gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard]
            for gate in gates:
                gate.config(state=DISABLED)


# Clear button function
def clear(circuit):
    """
    Clears the display!
    Reintializes the Quantum Circuit for fresh calculation!
    Checks if the gate buttons are disabled, if so, enables the buttons
    """
    # clear the display
    display.delete(0, END)

    # reset the circuit to initial state |0>
    initialize_circuit()

    # Checks if the buttons are disabled and if so, enables them
    if x_gate['state']==DISABLED:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard]
        for gate in gates:
            gate.config(state=NORMAL)

# Initializing the circuit
circuit=initialize_circuit()
theta=0

# Define Layout


# Define the frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root, bg='black')
display_frame.pack() # insert the elements in window
button_frame.pack(fill='both', expand =True )

# Define the Display Frame Layout
display = tkinter.Entry(display_frame, width = 120, font = display_font, bg= background, borderwidth=10, justify=LEFT)
display.pack(padx=3,pady=4)

# Define first row of buttons 
x_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'X',command=lambda:[display_gate('x'),circuit.x(0)])
y_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'Y',command=lambda:[display_gate('y'),circuit.y(0)])
z_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'Z',command=lambda:[display_gate('z'),circuit.z(0)])

# Define positions of first row buttons 
x_gate.grid(row=0,column=0,ipadx=45,pady=1)
y_gate.grid(row=0,column=1,ipadx=45,pady=1)
z_gate.grid(row=0,column=2,ipadx=53,pady=1,sticky='E') # sticky E stands for east

# Define second row of buttons 
Rx_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'RX',command= lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'RY',command= lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'RZ',command= lambda:[display_gate('Rz'),user_input(circuit,'z')])
Rx_gate.grid(row=1,column=0,columnspan=1,sticky='WE',pady=1)
Ry_gate.grid(row=1,column=1,columnspan=1,sticky='WE',pady=1)
Rz_gate.grid(row=1,column=2,columnspan=1,sticky='WE',pady=1)

# Define third row of buttons
s_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'S',command= lambda:[display_gate('s'),circuit.s(0)])
sd_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'SD',command= lambda:[display_gate('SD'),circuit.sdg(0)])
hadamard = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'H',command= lambda:[display_gate('H'),circuit.h(0)])
s_gate.grid(row=2,column=0,columnspan=1,sticky='WE',pady=1)
sd_gate.grid(row=2,column=1,sticky='WE',pady=1)
hadamard.grid(row=2,column=2,rowspan=2,sticky='WENS',pady=1)

# Define fourth row of buttons
t_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'T',command= lambda:[display_gate('t'),circuit.t(0)])
td_gate = tkinter.Button(button_frame,font=button_font,bg=buttons, text= 'TD',command= lambda:[display_gate('TD'),circuit.tdg(0)])
t_gate.grid(row=3,column=0,sticky='WE',pady=1)
td_gate.grid(row=3,column=1,sticky='WE',pady=1)

# Define the Quit and Visualize buttons
quit = tkinter.Button(button_frame,font=button_font,bg=special_buttons, text= 'Quit',command= root.destroy)
visualize = tkinter.Button(button_frame,font=button_font,bg=special_buttons, text= 'Visualize',command= lambda:visualize_circuit(circuit,root))
quit.grid(row=4,column=0,columnspan=2,sticky='WE',ipadx=5,pady=1)
visualize.grid(row=4,column=2,columnspan=1,sticky='WE',ipadx=8,pady=1)

# Define the clear button
clear_button = tkinter.Button(button_frame,font=button_font,bg=special_buttons, text= 'Clear',command= lambda:clear(circuit))
clear_button.grid(row=5,column=0,columnspan=3,sticky='WE')

# Define the about button
about_button = tkinter.Button(button_frame,font=button_font,bg=special_buttons, text= 'About',command=about)
about_button.grid(row=6,column=0,columnspan=3,sticky='WE')


# Run the main loop
root.mainloop()
