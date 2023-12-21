def text_value_error_handler(text: str) -> ValueError | str:
    if type(text) is not str:
        raise ValueError("Search text must be string")
    elif text.isdigit():
        raise ValueError("Search text must not contain only numbers")
    else:
        return text