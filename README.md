## TopDown Builder

Este proyecto busca facilitar la creación de esquemas TopDown para estructurar bien nuestro codigo. Para ello se utiliza Graphviz y el usuario debe crear un archivo .txt con la sintaxis necesaria.

## Como clonar este repositorio para *Windows*

Primero es necesario descargar el binario (está dentro del ZIP archive) de Graphviz en: https://graphviz.org/download/ . La versión que se utilizó cuando se programó este proyecto es la **13.0.1**

Luego es necesario clonar este repositorio:

```bash
git clone https://github.com/LucasAugusto-py/TopDownBuilder.git
```

Entrar a la carpeta del repositorio

```bash
cd TopDown Builder
```

Crear una carpeta "resources" que tenga otra carpeta "graphviz":

```bash
mkdir resources/graphviz
```

Y arrastar el archivo "bin" que se descargó en el ZIP de Graphviz dentro de la carpeta Graphviz

Por último instalar todas las dependencias:

```bash
pip install -r requirements.txt
```

Para evitar conflictos se recomienda usar un entorno virtual de python

Ya con todo esto se podría ejecutar el compilador para crear el archivo .exe

```bash
pyinstaller --clean --noconfirm main.spec
```

## Proximamente para Linux...
