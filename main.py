import streamlit as st
from shunting_yard import infix_a_postfix, agregar_concatenacion_implicita
from Thompson import Thompson_Algorithm
from Automata import Automata
from Subconjuntos import subsets_construction
from Minimizar import *
from NFA import NFA
from DFA import DFA

predefined_expressions = [
    'aa(bb)*c',
    '(a|b)*abb',
    '(b|b)*abb(a|b)*',
    'abbaa'
]

def main():
    st.set_page_config(page_title ='Automata', page_icon="https://png.pngtree.com/png-vector/20220719/ourmid/pngtree-robot-logo-template-vector-icon-illustration-sign-symbol-computer-vector-png-image_37807128.png")
    st.title('Construcción de Autómatas a partir de Expresiones Regulares')
    predefined_option = st.selectbox(
        "Selecciona una expresión predefinida o ingresa la tuya:",
        options=["Ingresar manualmente"] + predefined_expressions
    )
    
    # Campo de texto para ingresar una expresión regular
    expression = st.text_input(
        "Ingresa la expresión regular:", 
        "" if predefined_option == "Ingresar manualmente" else predefined_option
    )
    word = st.text_input("Ingresa la palabra que crees que pertence a la expresión regular:  ")
    if st.button("Generar Autómata"):
        if expression:
            try:
                #expression = remove_epsilon(expression)
                expression = agregar_concatenacion_implicita(expression)
                postfix_expression = infix_a_postfix(expression)
                st.write(f"Expresión en notación postfix: {postfix_expression}")

                NFA = Thompson_Algorithm(postfix_expression)
                st.write("NFA:")
                st.write(f"Estados: {NFA.states}")
                st.write(f"Alfabeto: {NFA.alphabet}")
                st.write(f"Estado inicial: {NFA.initial_state}")
                st.write(f"Estados finales: {NFA.final_states}")
                st.write(f"Transiciones: {NFA.transitions}")
                st.write("Simulación del NFA: ")
                is_NFA_word, NFA_register = NFA.simulate(word)
                for transition in NFA_register:
                    st.write(transition)
                NFA.to_graph("NFA")
                st.image("./NFA.png", caption="Diagrama del autómata no determinista  ", use_column_width=True)
                json_NFA = NFA.to_json("NFA.json")

                for transition in NFA_register:
                    st.write(transition)

                DFA_n = subsets_construction(NFA)

                st.write("NFA a DFA: ")
                st.write(f"Estados: {DFA_n.states}")
                st.write(f"Alfabeto: {DFA_n.alphabet}")
                st.write(f"Estado inicial: {DFA_n.initial_state}")
                st.write(f"Estados finales: {DFA_n.final_states}")
                st.write(f"Transiciones: {DFA_n.transitions}")
                st.write("Simulación del DFA inicial: ")
                is_DFA_word, DFA_register = DFA_n.simulate(word)
                for transition in DFA_register:
                    st.write(transition)
                DFA_n.to_graph("DFA")
                json_DFA1 = DFA_n.to_json("DFA1,json")
                st.image("./DFA.png", caption="Diagrama del autómata determinista sin minimizar", use_column_width=True)

                DFA = minimize(DFA_n)

                st.write("DFA minimizado: ")
                st.write(f"Estados: {DFA.states}")
                st.write(f"Alfabeto: {DFA.alphabet}")
                st.write(f"Estado inicial: {DFA.initial_state}")
                st.write(f"Estados finales: {DFA.final_states}")
                st.write(f"Transiciones: {DFA.transitions}")
                st.write("Simulación del DFA minimizado: ")
                is_DFAN_word, DFAN_register = DFA.simulate(word)
                for transition in DFAN_register:
                    st.write(transition)
                DFA.to_graph("DFAMIN")
                
                print(DFA)
                json_DFA = DFA.to_json("DFA_MIN.json")

                st.image("./DFAMIN.png", caption="Diagrama del automata minimizado", use_column_width=True)

                if is_DFAN_word:
                    st.success('La expresión es satisfacible 😃')
                    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwebstockreview.net%2Fimages%2Fclipart-smile-smile-gif-2.gif&f=1&nofb=1&ipt=294231fe86a240d4509d6ae34b13cff3bc32cee00995943d15638eb2239d3d8f&ipo=images", width=200)
                else:
                    st.error('La expresión no es satisfacible 😞')
                    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fimages%2Ffc1d577e8b42f847e1ef1615b76a9483%2Ftenor.gif&f=1&nofb=1&ipt=46395077f203095ad2f2bb4fd4e8d16027782772c5832057cba83ad55ee6155e&ipo=images", width=200)


                st.download_button(
                    label="Descargar Automata JSON",
                    data=json_NFA,
                    file_name="automaton.json",
                    mime="application/json"
                )

                st.download_button(
                    label="Descargar Automata DFA JSON",
                    data=json_DFA1,
                    file_name="automaton_dfa.json",
                    mime="application/json"
                )

                st.download_button(
                    label="Descargar Automata DFA Minimizado JSON",
                    data=json_DFA,
                    file_name="automaton_dfa_min.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(f"Error al generar el autómata: {e}")

if __name__ == "__main__":
    main()

