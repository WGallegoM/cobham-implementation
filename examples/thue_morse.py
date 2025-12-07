from .. import cobham

thue_morse_transformations = {
    "0" : "01",
    "1" : "10"
}

thue_morse_morphism = cobham.morphism(thue_morse_transformations)

thue_morse_automata = cobham.output_automata(
    2, #k-languages
    ["0","1"], #states
    "0", #initial State
    [
        ["0","1"], #q_0: 0 -> q_0, 1 -> q_1 
        ["1","0"]  #q_1: 0 -> q_1, 1 -> q_0
    ],                                          #Transition function
    cobham.k_language(2),                   #output language
    ["0","1"] # q_0 -> 0 , q_1 -> 1             #Output function
)

TM_automata = cobham.morphismToAutomata(thue_morse_morphism,"0")
TM_morphism = cobham.automataToMorphism(thue_morse_automata)

print("\\\\--------------------------------------THUE-MORSE--------------------------------------\\\\")
print(f"Thue-morse morphism applied 2 times over 0110 is {thue_morse_morphism.apply("0110",n=2)}")

print(f"the original morphism is: \n{thue_morse_morphism._info()}")
print(f"the original automaton is: \n{thue_morse_automata._info()}")

print(f"\nthe result converting the morphism to a automaton is: \n{TM_automata._info()}")
print(f"\nthe result converting the automaton to a morphism is: \n{TM_morphism._info()}")

print(f"los morfismos de TM son iguales: {TM_morphism == thue_morse_morphism}")
print(f"los automatas de TM son iguales: {TM_automata == thue_morse_automata}")