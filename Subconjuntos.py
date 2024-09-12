from Automata import Automata



def closure(automata, state):
    states = [state] #Creamos un conjunto que va a contener los estados obtenidos

    if "ε" in automata.transitions[state]: #Verificamos si el estado tiene la epsilon transición

        for i in states:
            if "ε" in automata.transitions[i]:
                states += automata.transitions[i]["ε"]


    return set(states)


def subsets(nfa):




    pass





