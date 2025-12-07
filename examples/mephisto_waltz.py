#TODO completar ejemplo mephisto waltz

mephisto_waltz_transformations = {
    "0" : "001",
    "1" : "110"
}


mephisto_waltz_morphism = cobham.morphism(mephisto_waltz_transformations)
print(mephisto_waltz_morphism.apply("0",n=3))

print("Mephisto-Waltz: Morfismo -> Automata")

MW_automata = cobham.morphismToAutomata(mephisto_waltz_morphism,"0")
