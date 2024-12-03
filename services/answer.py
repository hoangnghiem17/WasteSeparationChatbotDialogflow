import logging

from services.database import query_disposal_information

def generate_response(item_name: str) -> str:
    """
    Generate a response based on disposal information retrieved from the database.

    Args:
        item_name (str): The name of the item for which disposal information is requested.

    Returns:
        str: A response string providing disposal instructions based on completeness of the data retrieved.
    """
    
    logging.debug(f"Generating response for item: {item_name}")

    try:
        # Fetch disposal info from the database
        entsorgungsinfo = query_disposal_information(item_name)
        
        if entsorgungsinfo:
            # Unpack results
            entsorgungsort, adresse, link = entsorgungsinfo

            # Construct response dynamically
            entsorgungsort_text = f"Der Entsorgungsort für {item_name} ist {entsorgungsort}."
            adresse_part = f" bei der folgenden Adresse: {adresse}." if adresse else ""
            link_part = f" Du findest weitere Informationen hier: {link}" if link else ""
            response = entsorgungsort_text + adresse_part + link_part

            logging.debug(f"Response for '{item_name}': {response}")
            return response
        else:
            # No results found
            response = f"Für {item_name} konnte ich leider keinen Entsorgungsort finden."
            logging.warning(f"No disposal info found for item '{item_name}'.")
            return response

    except Exception as e:
        # Log and handle unexpected errors
        logging.error(f"An error occurred while generating response for '{item_name}': {e}")
        return "Es ist ein Fehler aufgetreten. Bitte versuche es später erneut."
