This code implementents the *Little Cobham's Theorem*,which allows us to take 
a **k-DFAO** (*Deterministic Finite Automaton with Output* with the language of the first k natural numbers) that computes a *infinite word a* and **convert** it, to the corresponding morphic representation  

# Building a Automaton
The automaton takes the 6 usual parts of a k-AFDO to make a instance of the class
**output_automata**. 

## Parts
The exact arguments are:
### language
Takes a natural number great than 1 to build de \Sigma_k
equivalent language
### states
take the name of the states as a list of strings,It is recommended that they be ordered numbers to allow conversion to morphism.
### initial_state
takes the name of one state in states to be the initial state
### transtition function
takes a 2-dimensional array, each "sub-array" represents the possible transitions in a certain state. for example, the transition function of the thue-morse automaton is:  
```python
[ ["0","1"], 
  ["1","0"] ]
```
+ when the **state 0** reads 0, it goes the state 0, when it reads 1 it goes to the state 1
+ when the **state 1** reads 0, it goes the state 1, when it reads 1 it goes to the state 0
### Output Language
self explanatory, it is a string

### Output Function
takes a list or a dictionary to build the output function.  
+ if it is a *dictionary* checks that its keys are the same as the states
+ if it is a *list* it checks the its lenght is the same as the quantity of states;if so, assign the *i* element as output for the *i* state

# Building and using a Morphism

# Automaton to Morphism

# Morphism to automata
