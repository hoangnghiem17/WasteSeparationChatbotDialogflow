import logging

import sqlite3

def query_disposal_information(item_name: str) -> tuple:
    """
    Fetch disposal information from the database for a given item (Abfallart).

    Args:
        item_name (str): Name of the item to query in the database.

    Returns:
        tuple or None: A tuple containing the disposal information:
            - Entsorgungsweg (str): The method or place of disposal (e.g., "Recyclingzentrum").
            - Adresse (str or None): The address of the disposal location, if available.
            - Link (str or None): A URL with more information, if available.
            Returns None if no matching row is found.
    """
    
    logging.debug(f"Querying database for item: {item_name}")
    conn = sqlite3.connect('abfallABC_entsorgung.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Entsorgungsweg, Adresse, Link FROM abfallABC_entsorgung WHERE LOWER(Abfallart) = LOWER(?)", (item_name,))
    result = cursor.fetchone()
    conn.close()
    logging.debug(f"Query result: {result}")
    return result
