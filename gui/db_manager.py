import sqlite3
import os

def init_db(): 
    conn = sqlite3.connect('handle.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS handles (
        handle text UNIQUE, 
        checked text,
        available text
        )
    """)
    c.execute("""CREATE TABLE IF NOT EXISTS har (
        har text
        )
    """)
    conn.commit()
    conn.close()

def get_har(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "SELECT * FROM har"
    cursor.execute(query)
    c.commit()
    rows = cursor.fetchall()
    c.close()
    return rows

def delete_har(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "DELETE FROM har"
    cursor.execute(query)
    c.commit()
    c.close()    
    
def add_har(har): 
    delete_har()
    harToText = str(har)
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "INSERT INTO har (har) VALUES (?)"
    cursor.execute(query, [harToText])
    c.commit()
    c.close()

def add_handle(handle): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    try:
        c.execute('BEGIN')
        query = "INSERT INTO handles (handle, checked) VALUES (?, ?);"
        values = (handle, 'unchecked')
        cursor.execute(query, values)
        c.commit()
    except sqlite3.Error as e:
        # Rollback the transaction if an error occurs
        c.rollback()
        print(f"Error: {str(e)}")
    finally:
        # Close the database connection
        c.close()
    c.close()

def delete_handle(handle): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    handle_to_delete = handle
    delete_query = "DELETE FROM handles WHERE handle = ?"
    cursor.execute(delete_query, (handle_to_delete,))   
    c.commit()
    c.close()

def update_handle(handle, available): 
    c = sqlite3.connect('handle.db')   
    cursor = c.cursor()
    new_value = "checked"
    update_query = f"UPDATE handles SET checked = ?, available = ? WHERE handle = ?"
    cursor.execute(update_query, (new_value, available, handle))  
    c.commit()
    c.close()

def get_unchecked_handles(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "SELECT * FROM handles WHERE checked = ?"
    cursor.execute(query, ('unchecked',))
    rows = cursor.fetchall()
    c.commit()
    c.close()
    return rows

def get_checked_handles(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "SELECT * FROM handles WHERE checked = ?"
    cursor.execute(query, ('checked',))
    rows = cursor.fetchall()
    c.commit()
    c.close()
    return rows

def get_available_handles(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "SELECT * FROM handles WHERE available = ?"
    cursor.execute(query, ('available',))
    rows = cursor.fetchall()
    c.commit()
    c.close()
    return rows

def validate_handle(handle): 
    if len(handle) < 3:
        return False
    for char in handle:
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_0987654321." :
            return False
    return True

def validate_har(file_path):
    file_name = os.path.basename(file_path)
    if file_name.endswith('.har') and "youtube.com" in file_name:
        return True
    else:
        return False