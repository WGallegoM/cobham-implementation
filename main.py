import cobham

h_transformations = {
    "0" : "01",
    "1" : "10"
}

mephisto_waltz_transformations = {
    "0" : "001",
    "1" : "110"
}

thue_morse_morphism = cobham.morphism(h_transformations)
mephisto_waltz_morphism = cobham.morphism(mephisto_waltz_transformations)

print(thue_morse_morphism.apply("0110",n=2))
print(mephisto_waltz_morphism.apply("0",n=3))

thue_morse_automata = cobham.output_automata(
    2, #k-languages
    ["q_0","q_1"], #states
    "q_0", #initial State
    [
        ["0","1"], #q_0: 0 -> q_0, 1 -> q_1 
        ["1","0"]  #q_1: 0 -> q_1, 1 -> q_0
    ],                                          #Transition function
    cobham.k_language(2),                   #output language
    ["0","1"] # q_0 -> 0 , q_1 -> 1             #Output function
)





print("Mephisto-Waltz: Morfismo -> Automata")

MW_automata = cobham.morphismToAutomata(mephisto_waltz_morphism,"0")
#TM_automata = cobham.morphismToAutomata(thue_morse_morphism,"0")

#print(str(mephisto_waltz_morphism))
#print(mephisto_waltz_morphism._info())

print(thue_morse_automata._info())

print("\n \\\\------------------ITS OVER!------------------\\\\")