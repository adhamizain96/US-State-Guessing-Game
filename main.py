#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
import pandas as p

screen = t.Screen()
screen.title('US State Guessing Game')
image = 'blank_states_img.gif'
#t.addshape() - name is the name of a gif-file and shape is None: Install the corresponding image shape
screen.addshape(image)
#t.shape() - set turtle shape to shape with given name or, if name is not given, return name of current shape
t.shape(image)

data = p.read_csv('50_states.csv')   
#to_list() - used to convert a series to list
states = data.state.to_list()
state_guess = []

while len(state_guess) < 50:
    #t.textinput() - pop up a dialog window for input of a string
    #t.title() - set title of turtle window to titlestring
    state_answer = screen.textinput(title = f'{len(state_guess)}/50 Correct', prompt = 'Guess another one?').title()
    if state_answer == 'Exit':
        incorrect = []
        for state in states:
            if state not in state_guess:
                incorrect.append(state)
        #p.DataFrame() - two-dimensional, size-mutable, potentially heterogeneous tabular data
        new_data = p.DataFrame(incorrect)
        new_data.to_csv('incorrect_states.csv')
        #break - terminate a loop and skip to the next code after the loop
        break
    if state_answer in states:
        state_guess.append(state_answer)
        s = t.Turtle()
        #t.turtle() - make the turtle invisible
        s.hideturtle()
        #t.penup() - pull the pen up - no drawing when moving
        s.penup()
        state_data = data[data.state == state_answer]
        #t.goto() - move turtle to an absolute position
        s.goto(int(state_data.x), int(state_data.y))
        #t.write() - write text
        s.write(state_answer, align = 'center')


# In[ ]:




