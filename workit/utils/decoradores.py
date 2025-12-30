"""Decoradores workit"""

from functools import wraps
import re

def validar_input(patterns, error_msg = None):
    """
    Decorador para validar con patrones RegEx el input del formulario
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = kwargs.get('data')

            if data:
                for field, pattern in patterns.items():
                    if field in data:
                        value = str(data[field])
                        if not re.match(pattern, value):
                            if error_msg and field in error_msg:
                                msg = error_msg[field]
                            else:
                                msg = f"Input inválido para {field}"
                            return ValueError(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def log(operation, success = None):
    """
    Decorador para imprimir mensajes de log
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                if success:
                    msg =  f"✅ {operation} completado"
                    print(msg)
                return result

            except Exception as e:
                print(f"❌ Error en {operation}: {e}")
        return wrapper
    return decorator
