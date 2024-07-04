from database.DAO import DAO
import networkx as nx

import copy
class Model:
    def __init__(self):
        # self._valori_fissi = None
        # self.get_valori_fissi()
        self._digraph = nx.DiGraph
        self.mappa_archi = {}
        # self._map_valori = {} MapId (associa all'id un oggetto con cui poi puntare al grafo)

        # self.output_ricorsione = None #Da adattare in base all'ouput desiderato

        self._cammino_massimo = None
        self._peso_cammino_massimo = None



    #def get_valori_fissi:
    #    self._valore_fisso = DAO.get_valore_fisso()

    #@property
    #def valori_fissi(self):
        #return self._valori_fissi


    def crea_grafo(self):

        self._digraph = nx.DiGraph()

        temp_cromosomi = self.get_cromosomi()

        self._digraph.add_nodes_from(temp_cromosomi)

        temp_correlazioni = self.get_correlazioni()
        self.mappa_archi = {}
        for c in temp_correlazioni:
            if (c.c1, c.c2) not in self.mappa_archi.keys():
                self.mappa_archi[(c.c1, c.c2)] = c.c
            else:
                self.mappa_archi[(c.c1, c.c2)] = self.mappa_archi[(c.c1, c.c2)]+c.c

        for a in self.mappa_archi.keys():
            self._digraph.add_edge(a[0], a[1], weight=self.mappa_archi[a])

    def get_cromosomi(self):
        return DAO.get_all_cromosomi()

    def get_correlazioni(self):
        return DAO.get_all_correlazioni()

    def get_cammino(self, s):
        temp_grafo = copy.deepcopy(self._digraph)

        for v in temp_grafo.nodes():
            temp_nodi = [v]
            temp_archi = []
            temp_distanza = 0
            self.ricorsione(s, temp_grafo, temp_nodi, temp_archi, temp_distanza)

        return self._peso_cammino_massimo, self._cammino_massimo

    def ricorsione(self, s, grafo, nodi, archi, distanza):
        if len(list(grafo.neighbors(nodi[-1]))) == 0:
            if self._peso_cammino_massimo is None or distanza > self._peso_cammino_massimo:
                self._peso_cammino_massimo = copy.deepcopy(distanza)
                self._cammino_massimo = copy.deepcopy(archi)
        else:
            for n in grafo.successors(nodi[-1]):
                if grafo[nodi[-1]][n]["weight"] >= s:
                    temp_grafo = copy.deepcopy(grafo)
                    temp_grafo.remove_node(nodi[-1])
                    archi.append((nodi[-1], n, grafo[nodi[-1]][n]["weight"]))
                    nodi.append(n)
                    distanza += archi[-1][2]
                    self.ricorsione(s, temp_grafo, nodi, archi, distanza)
                    distanza -= archi[-1][2]
                    nodi.pop()
                    archi.pop()
                else:
                    if self._peso_cammino_massimo is None or distanza > self._peso_cammino_massimo:
                        self._peso_cammino_massimo = copy.deepcopy(distanza)
                        self._cammino_massimo = copy.deepcopy(archi)



    def get_num_of_nodes(self):
        return len(list(self._digraph.nodes()))

    def get_num_of_edges(self):
        return len(list(self._digraph.edges(data=True)))

    def get_edges(self):
        return list(self._digraph.edges(data=True))

    def get_edge_min(self):
        min = None
        for e in self.get_edges():
            if min is None or min>e[2]["weight"]:
                min = e[2]["weight"]
        return min

    def get_edge_max(self):
        max = None
        for e in self.get_edges():
            if max is None or max < e[2]["weight"]:
                max = e[2]["weight"]
        return max

    def get_nedges_soglia(self, s):
        nmin = 0
        nmax = 0
        for e in self.get_edges():
            if e[2]["weight"] < s:
                nmin += 1
            elif e[2]["weight"] > s:
                nmax += 1
        return nmax, nmin


