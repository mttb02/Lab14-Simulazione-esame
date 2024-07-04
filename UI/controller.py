import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.crea_grafo()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))
        self._view.txt_result.controls.append(ft.Text(f"Informazioni sui pesi degli archi - valore minimo: {self._model.get_edge_min()} e valore massimo: {self._model.get_edge_max()}"))

        self._view.btn_countedges.disabled = False
        self._view.btn_search.disabled = False

        self._view.update_page()

    def handle_countedges(self, e):
        try:
            s = float(self._view.txt_name.value)
        except ValueError:
            self._view.create_alert("inserire un valore soglia float")
            return

        mag, min = self._model.get_nedges_soglia(s)
        self._view.txt_result2.controls.append(ft.Text(
            f"Numero di archi con perso maggiore della soglia: {mag}"))
        self._view.txt_result2.controls.append(ft.Text(
            f"Numero di archi con peso minore della soglia: {min}"))
        self._view.update_page()


    def handle_search(self, e):
        try:
            s = float(self._view.txt_name.value)
        except ValueError:
            self._view.create_alert("inserire un valore soglia float")
            return

        temp_peso, temp_cammino = self._model.get_cammino(s)

        self._view.txt_result3.controls.append(ft.Text(
            f"Peso cammino massimo: {temp_peso}"))
        print(temp_cammino)
        for a in temp_cammino:
            self._view.txt_result3.controls.append(ft.Text(
                (f"{a[0]} --> {a[1]}: {a[2]}")))


        self._view.update_page()
