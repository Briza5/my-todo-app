FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):  # otevře soubor pro čtení a načte obsah souboru v listu
    """ otevře soubor pro čtení a načte obsah souboru tedy
      todo-list..
    """
    with open(filepath, 'r', encoding="utf-8") as file_local:
            todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ zapisuje todo item list do souboru """
    with open(filepath, 'w', encoding="utf-8") as file:
            todos = file.writelines(todos_arg)


""" blok kódu, která se spustí při přímém spuštění modulu, ale ne při importu modulu
, protože v té chvíli nabývá proměnná __name__ hodnoty "functions" """
if __name__ == "__main__":
  print("Hello from functions")