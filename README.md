# Proyecto No. 1 

## Dependencias
Para ejecutar correctamente el proyecto, es necesario que la computadora tenga instalado lo siguiente:
- Python 
    - Streamlit
    - Pip
    - unittest
- Graphviz
- Docker (opcional)
## ¿Cómo ejecutar el proyecto?
Para ejecutar el proyecto de manera local, abre una terminal y ejecuta:
```sh
pip install streamlit graphviz unittest
streamlit run ./main.py
```
Si no deseas instalar los paquetes de python, y tienes docker instalado puedes hacer lo siguiente:
```sh
docker buildx build -t proyecto1-teoria .
docker run proyecto1-teoria
``` 
Para ejecutar las pruebas en el archvio test.py:
```sh
python -m unittest test_automata.py
```
