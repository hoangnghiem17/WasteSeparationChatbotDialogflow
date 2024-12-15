import sqlite3
import logging
from rapidfuzz import process  # Use rapidfuzz for fuzzy matching

def query_disposal_information(item: str) -> tuple:
    """
    Fetch disposal information from the database for a given item (Abfallart) using fuzzy matching.

    Args:
        item (str): Name of the item to query in the database.

    Returns:
        tuple or None: A tuple containing:
            - Entsorgungsweg (str): The method or place of disposal (e.g., "Recyclingzentrum").
            - Adresse (str or None): The address of the disposal location.
            - Link (str or None): A URL with more information.
            Returns None if no sufficiently close match is found.
    """
    try:
        logging.debug(f"Querying database for item: {item}")
        conn = sqlite3.connect("abfallABC_entsorgung.db")
        cursor = conn.cursor()

        # Fetch all rows and item names (Abfallart)
        cursor.execute("SELECT Abfallart, Entsorgungsweg, Adresse, Link FROM abfallABC_entsorgung")
        db_items = cursor.fetchall()
        conn.close()

        # Extract the names for fuzzy matching
        item_names = [row[0] for row in db_items]
        match = process.extractOne(item, item_names, score_cutoff=75)

        if match:
            best_match = match[0]
            logging.debug(f"Best match for '{item}': {best_match} with score {match[1]}")

            # Find and return the corresponding row
            for row in db_items:
                if row[0] == best_match:
                    return row[1:]  # Return Entsorgungsweg, Adresse, Link
        
        logging.warning(f"No sufficiently close match found for item: {item}")
        return None

    except Exception as e:
        logging.error(f"Error querying disposal information: {e}")
        return None
