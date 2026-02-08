"""Decoradores workit"""

from functools import wraps
import re

def validar_input(func):
    """
    Decorador para validar con patrones RegEx el input del formulario
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        patterns = getattr(self, 'patrones_regex', {})
        error_msg = getattr(self, 'error_messages', {})
        
        data = kwargs.get('data')

        if data:
            # Validar que ningún campo esté vacío
            for field, value in data.items():
                if not str(value).strip():
                    raise ValueError(f"{field.capitalize()} no puede estar vacío")
            
            # Validar patrones RegEx
            for field, pattern in patterns.items():
                if field in data:
                    value = str(data[field])
                    if not re.match(pattern, value):
                        msg = error_msg.get(field, f"Input inválido para {field}")
                        raise ValueError(msg)
        return func(*args, **kwargs)
    return wrapper

def log(operacion):
    """
    Decorador para registrar operaciones con formato simple
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                print(f"[INFO] {operacion} completado exitosamente")
                return result
            except Exception as e:
                print(f"[ERROR] al ejecutar operación {operacion}: {e}")
                raise
        return wrapper
    return decorator
