from shunting_yard import agregar_concatenacion_implicita, infix_a_postfix
from Thompson import Thompson_Algorithm
from Subconjuntos import subsets_construction
from Minimizar import minimization
from Automata import Automata
import itertools

exp = '(a|b)*c'

exp = agregar_concatenacion_implicita(exp)

exp = infix_a_postfix(exp)

print(exp)

automata = Thompson_Algorithm(exp)



dfa_n = subsets_construction(automata)


def find_partition(state, partitions):
    for partition in partitions:
        if state in partition:
            return partition 
        


def minimize(dfa):
    cond = True
    old_partitions = [set(dfa.states) - set(dfa.final_states), set(dfa.final_states)] #Creamos una lista que almacena la primera partición
    old_partitions = [s for s in old_partitions if s != set()] #Comporbamos que la partición no esté vacía
    while cond:
        new_partition = [set(part) for part in old_partitions] #Esta lista almacenará otra partición en base a la antigua partición

        for i in old_partitions:
            new_partition.append(set()) #Añadimos un nuevo conjunto vacío a la nueva partición
            if len(i) > 0:  # Verificar que la partición no esté vacía
                reference_state = list(i)[0] #Definimos un estado de referencia

            for j in i:
                if j != reference_state:
                      for k in dfa.alphabet: #Evaluar la salida para cada caracter de cada estado
                        state_partition = find_partition(dfa.transitions[reference_state][k], old_partitions) #Encontrar la partición del estado de referencia:
                        if dfa.transitions[j][k] not in state_partition: #Si el estado con el caracter k no está en la partición del estado de referencia
                            new_partition[-1].add(j) #Añadimos el estado a la nueva partición
                            idx = old_partitions.index(i) #Obtenemos el índice de la antigua partición
                            new_partition[idx].remove(j) #Removemos el estado de la antigua partición
                            break
            if len(new_partition[-1]) == 0: #verificamos si la nueva partición está vacía
                new_partition.pop() #Si está vacía, la eliminamos

        if set(map(frozenset, new_partition)) == set(map(frozenset, old_partitions)): #Si no hay estados en la nueva partición, se termina el ciclo
            cond = False
        else:
            old_partitions = new_partition #La antigua partición se convierte en la nueva partición
    print(new_partition)

    # Mapeamos las nuevas particiones a estados enteros del AFD
    new_transitions = {}
    new_states= []
    final_states = []
    for i in range(len(new_partition)):
        new_states.append(i)
        new_transitions[i] = {}
        #Si el estado inicial está en la partición, se define como el estado incial del nuevo autómata
        if dfa.initial_state in new_partition[i]:
            initial_state = i
        #Si la intersección de la partición y los estados finales no es vacia,  se añade a la lista de estados finales

        if len(new_partition[i].intersection(set(dfa.final_states))) > 0:
            final_states.append(i)
        
        random_state = next(iter(new_partition[i]))

        for j in dfa.alphabet:
            incoming_state = dfa.transitions[random_state][j]
            partition = find_partition(incoming_state, new_partition)
            index = new_partition.index(partition)
            new_transitions[i][j] = index
            
        

    return Automata(new_states, dfa.alphabet, initial_state, final_states, new_transitions)
            



print(dfa_n)

part = minimize(dfa_n)

set6 = {1,2,3}
set7 = {4,3,6}


print(part)


word = 'aac'

print(part.simulate(word))