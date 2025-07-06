import streamlit as st
import functions as funct


todos = funct.get_todos() # načte soubor todos.txt

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # do proměnné todo ukládáme value
                                        # ze session_state s konkrétním key
    todos.append(todo) # přidá nové todo do načteného listu todos
    funct.write_todos(todos)  # zapíše nový list do todos.txt


    




st.title("My Todo App") # hlavní nadpis
st.subheader("Tohle je moje todo app") # podnadpis
st.write("Tahle aplikace zvýší efektivitu tvé práce") # běžný text

# pro každé todo načtené z listu todos, které pocházejí se souboru todos.txt vytvoří checkbox
for index, todo in enumerate(todos): # ve for loopu přidáme pomocí enumerate index
    checkbox = st.checkbox(todo, key=todo) # pro identifikace jednotlivých checkboxu
                                           # přidáme unikátní key a checkboxi uložíme do proměnné
    if checkbox: # pokud je proměnná checkobx true tak bude z listu odstraněn záznam s indexem,
        # který náleží k této proměnné
        todos.pop(index)
        funct.write_todos(todos) # zapsání nového todos do souboru
        del st.session_state[todo] # odstranění příslušného todo ze session_state dictionary
# vytvoří input box s placeholderem
        st.rerun() # tato fuknce refreshne aplikaci a tím zobrazí aktuální stav
st.text_input(label="", placeholder="Přidej nový úkol",
              on_change=add_todo, key="new_todo") # on_change vyvole event, který se zaznamená
                                                 # do session state a je tam označen přislušným 
                                                 # key



#print("Hello") # pro dev kontrolu jak program dobíhá a v jakém pořadí
#st.session_state # pro dev účely, kontrola obsahu session_stat