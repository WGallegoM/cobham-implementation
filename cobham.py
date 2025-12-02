class output_automata:
    def __init__(self,k,states,initial_state,transition_function,output_language,output_function):
        self.language = k_language(k)
        self.states = states        
        self.initial_state = states
        self.transition_function = transition_function
        self.output_language = output_language
        self.output_function = output_function

    """def __init__(self,k,states,transition_function,output_language,output_function): #TODO Revisar Overwriting porque no se puede hacer
        self.language = k_language(k)
        self.states = states        
        self.initial_state = states[0] #toma como estado inicial el primer estado
        self.transition_function = transition_function
        self.output_language = output_language
        self.output_function = output_function"""

class sequence:
    pass

class morphism:
    """def __init__(self,language,transformations : dict):
        self.language = language
        self.transformations = transformations"""

    def __init__(self,transformations:dict):
        """se asume que el lenguaje esta bien definido 
        y toma todas las entradas de las trasnformaciones como el
        lenguaje
        """
        self.language = []
        self.transformations = {}
        self.wellDefined = True
        self.prolongableOn = []

        self.isKUniform = len(next(iter(transformations.values()))) #se toma la longitud de la primera imagen

        for x in transformations:
            self.language.append(x)
            self.transformations[x] = transformations[x]

            if len(transformations[x]) != self.isKUniform:
                self.isKUniform = -1

            if (self.isKUniform != 1 and transformations[x][0] == x): #Si aun se considera k_uniforme y hay un morfismo cuyo primer caracter sea la entrada
                self.prolongableOn.append(x)      #se toma como un caracter sobre el cual es prolongable

    def _info(self):
        out = f"Language = {language}"

        return out #TODO info llenar

    def _is_well_defined():
        """se verifica que todos los simbolos del lenguaje tenga una imagen
        y que, esta no se defina dos veces por simbolo
        """
        return 

    def _is_K_uniform():
        """Verifica que todas las imagenes sean de la misma longitud"""
        kUni = True #asumimos que es k_uniforme

        #for i in range(len(transformations)):

    def apply(self,word:str,n=1):
        output = ""

        for x in word:
            output += self.transformations[x]

        if n <= 1:
            return output
        else:
            return(self.apply(output,n=n-1))

            
def k_language(n):
    return [str(i) for i in range(n)]

def morphismToAutomata(h_morphism:morphism, prolongableOn:str):
    #VERIFICA LAS CONDICIONES SOBRE EL MORFISMO

    if h_morphism.isKUniform <= -1:
        raise ValueError("the morphism is not k_uniform")

    #Se toma el k correspondiente al k-uniforme del morfismo
    k = h_morphism.isKUniform

    #Se toma el estado inicial como el caracter sobre el que es prolongable el morfismo
    if prolongableOn in h_morphism.prolongableOn: #Si el morfismo es efectivamente prolongable en el argumento   
        initial_state = prolongableOn
    else:
        raise ValueError(f"The morphism is not prolongable on {prolongableOn}")

    #El conjunto de estados es igual al alfabeto de entrada del morfismo
    states = [x for x in h_morphism.transformations]
    

    #Se construye la funcion de transicion
    language_len = len(h_morphism.transformations)
    transition_function = [ [] for i in range(language_len)]

    for i in range(language_len):
        for j in range(k):
            transition_function[i].append( h_morphism.apply(states[i])[j] )


    output_language = k_language(language_len)
    output_function = "spam" #TODO mirar como se construye la funcion de salida

    #Declara el automata equivalente
    equivalent_automata = output_automata(
        k,
        states,
        initial_state,
        transition_function,
        output_language,
        output_function
    )

    return equivalent_automata