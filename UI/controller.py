import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        r=self._model.getUmiditaMedia(self._mese)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("L'umidita media nel mese selezionato è:"))
        for i in r:
            self._view.lst_result.controls.append(ft.Text(str(i)))
        self._view._page.update()

    def handle_sequenza(self, e):
        l, c=self._model.getPercorso(self._mese)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"La sequenza ottima ha costo {c} ed è:"))
        for i in l:
            self._view.lst_result.controls.append(ft.Text(str(i)))
        self._view._page.update()

    def read_mese(self, e):
        self._mese = int(e.control.value)

