import streamlit as st
from shunting_yard import infix_a_postfix, agregar_concatenacion_implicita
from Thompson import Thompson_Algorithm
from Automata import Automata
from Subconjuntos import subsets_construction
from Minimizar import minimization

def main():
    st.set_page_config(page_title ='Automata', page_icon="https://png.pngtree.com/png-vector/20220719/ourmid/pngtree-robot-logo-template-vector-icon-illustration-sign-symbol-computer-vector-png-image_37807128.png")
    st.title('Construcción de Autómatas a partir de Expresiones Regulares')
    expression = st.text_input("Ingresa la expresión regular:")
    word = st.text_input("Ingresa la palabra que crees que pertence a la expresión regular:  ")
    if st.button("Generar Autómata"):
        if expression:
            try:
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

                DFA_n = subsets_construction(NFA)

                st.write("NFA a DFA: ")
                st.write(f"Estados: {DFA_n.states}")
                st.write(f"Alfabeto: {DFA_n.alphabet}")
                st.write(f"Estado inicial: {DFA_n.initial_state}")
                st.write(f"Estados finales: {DFA_n.final_states}")
                st.write(f"Transiciones: {DFA_n.transitions}")

                DFA = minimization(DFA_n)

                st.write("DFA minimizado: ")
                st.write(f"Estados: {DFA.states}")
                st.write(f"Alfabeto: {DFA.alphabet}")
                st.write(f"Estado inicial: {DFA.initial_state}")
                st.write(f"Estados finales: {DFA.final_states}")
                st.write(f"Transiciones: {DFA.transitions}")

                DFA.to_graph()
                
                is_word = DFA.simulate(word)

                st.image("./graph.png.png", caption="Automata Diagram", use_column_width=True)

                if is_word:
                    st.success('La expresión es satisfacible 😃')
                    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwebstockreview.net%2Fimages%2Fclipart-smile-smile-gif-2.gif&f=1&nofb=1&ipt=294231fe86a240d4509d6ae34b13cff3bc32cee00995943d15638eb2239d3d8f&ipo=images", width=200)
                else:
                    st.error('La expresión no es satisfacible 😞')
                    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fimages%2Ffc1d577e8b42f847e1ef1615b76a9483%2Ftenor.gif&f=1&nofb=1&ipt=46395077f203095ad2f2bb4fd4e8d16027782772c5832057cba83ad55ee6155e&ipo=images", width=200)




            except Exception as e:
                st.error(f"Error al generar el autómata: {e}")

if __name__ == "__main__":
    main()

