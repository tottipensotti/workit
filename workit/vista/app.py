"""App"""

from tkinter import Tk, messagebox
from typing import Dict, Any, Tuple, List, Optional
from workit.controlador import Controlador
from .componentes import Botonera, Header
from .formulario import Formulario
from .tabla import Tabla


class App:
    """Clase para crear la UI"""
    def __init__(self, title: str) -> None:
        self.root: Tk = Tk()
        self.root.title(title)
        self.root.configure(bg="white")
        self.controlador_vista: Controlador = Controlador()
        self.encabezado: Header = Header(self.root, "Agregue su ejercicio")
        self.formulario: Formulario = Formulario(
            self.root,
            color="white",
            ancho_col=20
        )
        self.botones: Botonera = Botonera(
            self.root,
            agregar=self.registrar,
            modificar=self.modificar,
            borrar=self.borrar
        )
        self.tabla: Tabla = Tabla(
            self.root,
            columns=(
                "#",
                "Ejercicio",
                "Peso (kg)",
                "Repeticiones",
                "Series",
                "Fecha"
            )
        )

        self.encabezado.mostrar()
        self.formulario.crear()
        self.botones.generar_botones()
        self.tabla.mostrar()
        self.actualizar_vista()
        self.root.mainloop()

    def registrar(self) -> None:
        """Agregar un nuevo registro"""
        data: Dict[str, Any] = {
            "ejercicio": self.formulario.valor_ejercicio.get(),
            "peso": self.formulario.valor_peso.get(),
            "reps": self.formulario.valor_reps.get(),
            "series": self.formulario.valor_series.get(),
            "fecha": self.formulario.valor_fecha.get()
        }
        try:
            self.controlador_vista.agregar_registro(data=data)
            self.formulario.limpiar_formulario()
            self.actualizar_vista()
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))

    def borrar(self) -> None:
        """Elimina registro seleccionado en la vista"""
        item: Tuple[str, ...] = self.tabla.tree.selection()
        if not item:
            messagebox.showwarning(
                "Advertencia",
                "Debe seleccionar un registro"
            )
            return

        item_id: str = self.tabla.tree.item(item, "values")[0]
        confirmacion: bool = messagebox.askyesno(
            "Confirmar borrado",
            f"Desea eliminar el registro {item_id}?"
        )

        if not confirmacion:
            return

        try:
            self.controlador_vista.borrar_registro(int(item_id))
            self.actualizar_vista()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def modificar(self) -> None:
        """Modifica el registro seleccionado"""
        item: Tuple[str, ...] = self.tabla.tree.selection()

        if not item:
            messagebox.showwarning(
                "Advertencia",
                "Debe seleccionar un registro de la tabla para modificar"
            )
            return

        valores: Tuple[str, ...] = self.tabla.tree.item(item, "values")
        id_registro: int = int(valores[0])

        confirmacion: bool = messagebox.askyesno(
            "Confirmar modificación",
            f"Desea modificar el registro {id_registro}?"
        )

        if not confirmacion:
            return

        data: Dict[str, Any] = {
            "id": id_registro,
            "ejercicio": self.formulario.valor_ejercicio.get(),
            "peso": self.formulario.valor_peso.get(),
            "reps": self.formulario.valor_reps.get(),
            "series": self.formulario.valor_series.get(),
            "fecha": self.formulario.valor_fecha.get()
        }

        try:
            self.controlador_vista.modificar_registro(data)
            self.formulario.limpiar_formulario()
            self.actualizar_vista()
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))

    def actualizar_vista(self) -> None:
        """Actualiza el contenido de la vista con los datos de la bbdd"""
        items_tree: Tuple[str, ...] = self.tabla.tree.get_children()

        for item in items_tree:
            self.tabla.tree.delete(item)

        registros: Optional[List[Any]] = self.controlador_vista.consultar_registro()
        if registros:
            for registro in registros:
                self.tabla.tree.insert("", "end", values=(
                    registro.id,
                    registro.ejercicio,
                    registro.peso,
                    registro.reps,
                    registro.series,
                    registro.fecha
                ))
