
def calculate_exspression(expression):
    try:
        expression = expression.strip().replace(' ', '')
        allowed_chars = ('0123456789+-*/.()')
        if not all(c in allowed_chars for c in expression):
            return None
        result = eval(expression)
        return str(result)
    except:
        return None