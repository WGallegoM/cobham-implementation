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
the morphism just takes a dictionary to define the the images of the language.  For example:
```python
thue_morse_transformations = {
    "0" : "01",
    "1" : "10"
}
```
## Parts of a morphism (attributes)
### Language
takes the keys of the language and interpret as a Language, that is stored in a list
### Transformations
Is the input od the constructor, tell how the characters are transformed
### ProlongableOn
It is a list of characters that stores the characters to which the morphism can be prolonged. These are the characters for which applying the morphism results in a string that begins with the same input character.

### isKUniform
It is a integer that indicates the k-uniformity of the morphism. If the morphism is not k-uniform takes the value -1

## Applying the morphism
The morphism can be applied over a character or a string with the method .apply, this method has a optional argument *n* which can be used to apply the morphism through composition *n times*.

# Other useful things
+ Both morphish and output automata have  _info function wich outputs all the attributes in a beatiful way. It is useful for debugging and checking the instances

+ the function **k-language(n)** builds a language which characters are the first k natural numbers.

# Automaton to Morphism
Briefly, It takes a output automata and makes a equivalent morphism. For this takes the automata, every state as a entry of the morphism, and the ordered outputs as the image.

# Morphism to automata

First verifies it is a convertable morphism. checks that is k-uniform and prolongable. The user enter as input a character on wich the morphism is prolongable, this will be taken as the initial state.  

The states will be the same as the language of the morphism.

The transition function of the state *a* will be determined by the output of the morphism over the same character. The i  transiton will be the state corresponding to the i character of h(a)

To make the output function first we must build a dictionary that indicates the *first appearance* of every character ain a *test_string* which is the result of applying the morphism on the character of the input.  Finally, takes as output of the character *a*, the character that appears in the index of the first appearance.