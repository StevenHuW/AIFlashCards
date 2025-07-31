import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS flashcard_sets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                   )
                   ''')
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS flashcards (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   set_id INTEGER NOT NULL,
                   word TEXT NOT NULL,
                   definition TEXT NOT NULL,
                   FOREIGN KEY (set_id) REFERENCES flashcard_sets(id)
                   )
                   ''')
    
def add_set(conn, name):
    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO flashcard_sets (name)
                   VALUES (?)
                   ''', (name,))
    
    set_id = cursor.lastrowid
    conn.commit()

    return set_id


if __name__ == '__main__':

    # SQLite to create database and create tables
    conn = sqlite3.connect('flashcards.db')
    create_tables(conn)

    root = tk.Tk()
    root.title('FlashCard App')
    root.geometry('1280x960')

    style = Style(theme='darkly')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButton', font=('TkDefaultFont', 16))

    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text='Create Set')

    ttk.Label(create_set_frame, text='Set name:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Word:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=word_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Definition:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=definition_var, width=30).pack(padx=5, pady=5)

    ttk.Button(create_set_frame, text='Add Word').pack(padx=5, pady=10)

    ttk.Button(create_set_frame, text='Save Set').pack(padx=5, pady=10)

    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text='Select Set')

    sets_combobox = ttk.Combobox(select_set_frame, state='readonly')
    sets_combobox.pack(padx=5, pady=40)

    ttk.Button(select_set_frame, text='Select Set').pack(padx=5, pady=5)

    ttk.Button(select_set_frame, text='Delete Set').pack(padx=5, pady=5)

    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text='Learn Mode')

    card_index = 0
    current_tabs = []

    word_label = ttk.Label(flashcards_frame, text='', font=('TkDefaultFont', 24))
    word_label.pack(padx=5, pady=40)

    definition_label = ttk.Label(flashcards_frame, text='')
    definition_label.pack(padx=5, pady=5)

    ttk.Button(flashcards_frame, text='Flip').pack(side='left', padx=5, pady=5)

    ttk.Button(flashcards_frame, text='Next').pack(side='right', padx=5, pady=5)

    ttk.Button(flashcards_frame, text='Previous').pack(side='right', padx=5, pady=5)

    # populate_sets_combobox()

    root.mainloop()
