"""Decoradores workit"""

import re
from functools import wraps
from datetime import datetime
from typing import Callable, Any, Dict, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def validar_input(func: F) -> F:
    """
    Decorador para validar con patrones RegEx el input del formulario
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        sujeto = args[0]
        timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self = args[0]
        patterns: Dict[str, str] = getattr(self, 'patrones_regex', {})
        error_msg: Dict[str, str] = getattr(self, 'error_messages', {})
        data: Any = kwargs.get('data')

        try:
            if data:
                # Validar que ningún campo esté vacío
                for field, value in data.items():
                    if not str(value).strip():
                        raise ValueError(
                            f"Error al validar input para {field.capitalize()}"
                            ": no puede estar vacío"
                        )

                # Validar patrones RegEx
                for field, pattern in patterns.items():
                    if field in data:
                        value = str(data[field])
                        if not re.match(pattern, value):
                            msg = error_msg.get(
                                field,
                                f"Input inválido para {field}"
                            )
                            raise ValueError(msg)
            result: Any = func(*args, **kwargs)
            event: Dict[str, Any] = {
                'timestamp': timestamp,
                'operation': 'Validación de Input',
                'status': 'Success',
                'message': 'Validación de input completada',
                'data': data
            }
            sujeto.notify(event)
            return result
        except ValueError as e:
            raise e
    return wrapper


def log(operacion: str) -> Callable[[F], F]:
    """
    Decorador para registrar operaciones con formato simple
    """
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            sujeto = args[0]
            timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result: Any = func(*args, **kwargs)
                event: Dict[str, Any] = {
                    'timestamp': timestamp,
                    'operation': operacion,
                    'status': 'Success',
                    'message': f"{operacion} completado exitosamente",
                    'data': kwargs.get('data') if 'data' in kwargs else args[1]
                }
                sujeto.notify(event)
                return result
            except Exception as e:
                event: Dict[str, Any] = {
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
