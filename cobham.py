class output_automata:
    def __init__(self,k,states,initial_state,transition_function,output_language,output_function):
        #K-language
        if isinstance(k,int):
            if k>=1:
                self.language = k_language(k)
            else:
                raise ValueError("k is less than 1, therefore there is no valid language")
        else:
            raise TypeError("No valid type for language, it must be a Int")

        #STATES
        if not isinstance(states,list):
            raise TypeError("states must be a list")
        if not all(isinstance(x,str) for x in states):
            raise TypeError("All the elements of states must be strings")
        else:
            self.states = states        
        
        #INITIAL_STATE
        if not isinstance(initial_state,str):
            raise TypeError("initial_state must be a String")
        else:
            if not(initial_state in states):
                raise ValueError("Initial_state is not in States")
            else:
                self.initial_state = initial_state
        
        self.transition_function = transition_function
        self.output_language = output_language
        
        self.output_function = {}

        if isinstance(output_function,list): 
            """si output function es una lista,entonces al estado i
            se le asigna el output i"""
            if len(output_function) != len(states):
                raise ValueError("the lenght of output_function is not the same as the quantity of states")
            else:
                for i in range(len(states)):
                    self.output_function[states[i]] = output_function[i]   

        elif isinstance(output_function,dict):
            """Si output_function es diccionario se asigna
            de inmediato como la funcion de output"""
            if (set(states) != set(output_function.keys())):
                raise ValueError("The keys of output_function are not the same as the states")

            self.output_function = output_function
            
    """def __init__(self,k,states,transition_function,output_language,output_function): #TODO Revisar Overwriting porque no se puede hacer
        self.language = k_language(k)
        self.states = states        
        self.initial_state = states[0] #toma como estado inicial el primer estado
        self.transition_function = transition_function
        self.output_language = output_language
        self.output_function = output_function"""

    def _info(self):
        out = f"Language: {self.language}\n"

        out += "States: "
        for state in self.states:
            if state == self.initial_state:
                out += f"({state}) ,"
            else:
                out += f"{state} ,"

        out += "\nTransition function:\n"

        for i in range(len(self.transition_function)):
            out += f"   {self.states[i]}: "
            for j in range(len(self.transition_function[i])):
                out += f" {self.transition_function[i][j]}, "
            
            if i < len(self.transition_function)-1:
                out += "\n"

        out += "\nOutput Language: "
        out += " ,".join(self.output_language)

        out += "\nOutput function: "
        for key,value in self.output_function.items():
            out += f"{key} -> {value}, "

        return out

    def __eq__(self,otherAutomata):
        isEqual = True #Se asumen iguales

        if not isinstance(otherAutomata,output_automata):
            return NotImplementedError
        elif(
            self.language == otherAutomata.language and
            self.states == otherAutomata.states and            
            self.initial_state == otherAutomata.initial_state and
            self.transition_function == otherAutomata.transition_function and
            self.output_language == otherAutomata.output_language and
            self.output_function == otherAutomata.output_function 
        ):
            return True
        else:
            return False

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
    
    def __str__(self):
        out = ""
        for key in self.transformations:
            out += key + " -> " + self.transformations[key] + "; "
        
        return out

    def _info(self):
        out  = f"Language: {self.language}\n"
        
        out += "Morphism: "
        for key in self.transformations:
            out += f"{key} -> {self.transformations[key]} ;"
        
        if self.isKUniform >= 0:
            out += f"\n{self.isKUniform}-uniform \n"
        else:
            out += "not k-uniform\n"

        out += f"prolongable on: {", ".join(self.prolongableOn)}\n"

        return out
    def __eq__(self,otherMorphism):

        if not isinstance(otherMorphism,morphism):
            return NotImplementedError
        elif(
            self.language == otherMorphism.language and                    
            self.transformations == otherMorphism.transformations and                
            self.wellDefined == otherMorphism.wellDefined and                
            self.prolongableOn == otherMorphism.prolongableOn and                
            self.isKUniform == otherMorphism.isKUniform        #TODO mirar como se puede debilitar las condiciones de igualdad           
        ):
            return True
        else:
            return False

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

def automataToMorphism(M_automata:output_automata):
    lenStates = len(M_automata.states)
    h_images = []
    k = len(M_automata.language)
    h_morphism = {}

    for i in range(lenStates):
        #h_images.append("".join(M_automata.transition_function[i]))
        h_morphism[M_automata.states[i]] = "".join(M_automata.transition_function[i])
    
    return morphism(h_morphism)

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

    #Se construye la funcion de output

    test_string = h_morphism.apply(prolongableOn,n=k) #TODO cuantas veces se necesita aplicar el morfismo para que salgan todos los caracteres

    first_appearance = {} #se declara la primera aparicion de cada caracter

    for i in range(len(test_string)):
        if not(test_string[i] in first_appearance): #si no esta la clave del numero encontrado se agrega
            first_appearance[test_string[i]] = i    #y se guarda como primera aparicion
            if len(first_appearance) == language_len:
                break #si ya se encontraron todos los caracteres se acaban los ciclos

    output_function = {} #TODO ajustar para que la comparacion de automatas sea correcta

    for key in first_appearance:
        output_function[key] = test_string[first_appearance[key]] 


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

