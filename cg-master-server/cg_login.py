#Sistema de login em python
import sqlite3
import re

def connect_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor

def validate_username(username):
    if re.match(r'^[a-zA-Z][a-zA-Z0-9-]{5,}$', username):
        return True
    else:
        return False

def singin(user,pw,pw_confirm):
    
    conn, cursor = connect_data()

    # usa a funcao validate_username(user) que valida nomes de usuário com pelo menos 6 caracteres, começando com uma letra e contendo apenas letras, números e traços
    check_name = validate_username(user)
    
    if check_name:
        pass
    else:
        return False

    cursor.execute("SELECT * FROM users WHERE username = ?", (user,))

    user_feedback = cursor.fetchone()

    if user_feedback:
        print('\nusername ja registrado, tente novamente:')
        return False
    else:
        if pw == pw_confirm:

            print('Registro concluido com sucesso!')
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pw))
            conn.commit()
            return True
        else:
            print('\nerro ao comparar senhas=> pw, pw_confirm!')
            return False

def login(user,pw):

    conn, cursor = connect_data()

    # execute e uma funcao do ojeto cursor que no caso realiza o trabalho de selecionar tudo de users e armazenar username e password
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, pw))

    # feedback 
    feedback = cursor.fetchone()

    if feedback:
        return True
    else:
        return False

conn, cursor = connect_data()
conn.close()