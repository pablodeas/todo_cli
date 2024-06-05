# ToDo CLI Application

![cli.git](./src/todo_cli.mp4)

## Funcionalidades
O ToDo CLI permite:
- Listar todas as notas
- Inserir uma nova nota
- Deletar uma nota existente

## Requisitos
- Python 3
- sqlite3

## Instalação

### Clonar o Repositório
```sh
git clone https://github.com/pablodeas/todocli.git
cd todocli
```

### Configurar o Ambiente Virtual
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configurar o Banco de Dados
```sh
python sql/script001.py
```

## Uso

### Listar todas as notas
```sh
todo list
```

### Inserir uma nova nota
```sh
todo insert "Título da Nota" "Corpo da Nota"
```

### Deletar uma nota
```sh
todo delete Id_da_Nota
```