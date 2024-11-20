import sqlite3

def get_entsorgungsinfo(item_name):
    conn = sqlite3.connect('abfallABC_entsorgung.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Entsorgungsweg, Adresse, Link FROM abfallABC_entsorgung WHERE Abfallart = ?", (item_name,))
    result = cursor.fetchone()
    conn.close()
    return result
