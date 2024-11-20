import logging

from services.database import query_disposal_information

def generate_response(item_name: str) -> str:
    """
    Generate a response based on disposal information retrieved from the database.

    Args:
        item_name (str): The name of the item for which disposal information is requested.

    Returns:
        str: A response string providing disposal instructions. The response varies based on the
        completeness of the data retrieved:
            - Case 1: All data (disposal method, address, and link) is available.
            - Case 2: Address is available, but no link is provided.
            - Case 3: Neither address nor link is available.
            - If no data is found, a message indicating the lack of information is returned.
    """
    
    logging.debug(f"Generating response for item: {item_name}")

    try:
        # Fetch disposal info from the database
        entsorgungsinfo = query_disposal_information(item_name)
        logging.debug(f"Database query result for '{item_name}': {entsorgungsinfo}")

        if entsorgungsinfo:
            entsorgungsort, adresse, link = entsorgungsinfo

            # Case 1: All columns are available
            if adresse and link:
                response = (
                    f"Der Entsorgungsort für {item_name} ist {entsorgungsort} "
                    f"bei der folgenden Adresse: {adresse}. "
                    f"Du findest weitere Informationen zu der Adresse hier: {link}"
                )
                logging.debug(f"Response for item '{item_name}' (Case 1): {response}")
                return response

            # Case 2: "Link" is empty
            elif adresse and not link:
                response = (
                    f"Der Entsorgungsort für {item_name} ist {entsorgungsort} "
                    f"bei der folgenden Adresse: {adresse}."
                )
                logging.debug(f"Response for item '{item_name}' (Case 2): {response}")
                return response

            # Case 3: Both "Link" and "Adresse" are empty
            elif not adresse and not link:
                response = (
                    f"Der Entsorgungsort für {item_name} ist {entsorgungsort}."
                )
                logging.debug(f"Response for item '{item_name}' (Case 3): {response}")
                return response

        else:
            # No results from the database
            response = f"Für {item_name} konnte ich leider keinen Entsorgungsort finden."
            logging.warning(f"No disposal info found for item '{item_name}'.")
            return response

    except Exception as e:
        # Log any unexpected errors
        logging.error(f"An error occurred while generating response for item '{item_name}': {e}")
        return "Es ist ein Fehler aufgetreten. Bitte versuche es später erneut."
