import logging

def extract_parameter(req: dict, param_name: str):
    """
    Extract a parameter from a Dialogflow request.

    Args:
        req (dict): The JSON request payload from Dialogflow.
        param_name (str): The name of the parameter to extract.

    Returns:
        str or None: The value of the specified parameter if found, otherwise None.
    """
    
    try:
        # Log the incoming request structure
        logging.debug(f"Extracting parameter '{param_name}' from request: {req}")

        # Extract the parameter
        value = req['queryResult']['parameters'].get(param_name)

        # Log the extracted value
        if value:
            logging.debug(f"Successfully extracted parameter '{param_name}': {value}")
        else:
            logging.warning(f"Parameter '{param_name}' not found in the request or has no value.")

        return value
    except KeyError as e:
        logging.error(f"KeyError encountered while extracting parameter '{param_name}': {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error while extracting parameter '{param_name}': {e}")
        return None
