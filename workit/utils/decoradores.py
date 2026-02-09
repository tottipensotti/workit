"""Decoradores workit"""

import re
from functools import wraps
from datetime import datetime
from .observadores import obtener_sujeto_log


def validar_input(func):
    """
    Decorador para validar con patrones RegEx el input del formulario
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        sujeto = obtener_sujeto_log()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self = args[0]
        patterns = getattr(self, 'patrones_regex', {})
        error_msg = getattr(self, 'error_messages', {})

        data = kwargs.get('data')

        try:
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
            result = func(*args, **kwargs)
            event = {
                'timestamp': timestamp,
                'operation': 'Validación de Input',
                'status': 'Success',
                'message': 'Validación de input completada',
                'data': data
            }
            sujeto.notify(event)
            return result
        except ValueError as e:
            event = {
                'timestamp': timestamp,
                'operation': 'Validación de Input',
                'status': 'Error',
                'message': str(e),
                'data': data
            }
            sujeto.notify(event)
            raise
    return wrapper

def log(operacion):
    """
    Decorador para registrar operaciones con formato simple
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sujeto = obtener_sujeto_log()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                event = {
                    'timestamp': timestamp,
                    'operation': operacion,
                    'status': 'Success',
                    'message': f"{operacion} completado exitosamente",
                    'data': kwargs.get('data') if 'data' in kwargs else args[1]
                }
                sujeto.notify(event)
                return result
            except Exception as e:
                event = {
                    'timestamp': timestamp,
                    'operation': operacion,
                    'status': 'Error',
                    'message': str(e),
                    'data': kwargs.get('data') if 'data' in kwargs else args[1]
                }
                sujeto.notify(event)
                raise
        return wrapper
    return decorator
