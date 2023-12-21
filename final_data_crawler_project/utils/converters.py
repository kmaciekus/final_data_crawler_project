def convert_to_float(value):
    if value == "":
        return None 
    else:
        try:
            return float(value.strip())
        except ValueError:
            # Handle the case where the conversion fails
            return None

def convert_to_int(value):
    if value == "":
        return None 
    else:
        try:
            return int(value.strip())
        except ValueError:
            # Handle the case where the conversion fails
            return None