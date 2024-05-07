# Arquivo responsável por printar os gráficos da viga

# Standard Library Imports
from collections import namedtuple
from math import radians
import time

# Third Party Imports
import numpy as np
from sympy import (integrate, lambdify, Piecewise, sympify, symbols,
                   linsolve, sin, cos, oo, SingularityFunction)
from sympy.abc import x
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.path as mpath

class Printer:
    def printar_desenho_inicial(Viga):
        print("Printando desenho inicial")
        TAMANHO_VIGA = Viga.tamanho
        LOCALIZACAO_FORCAS_VERTICAIS = Viga.localizacao_f_verticais
        INTENSIDADE_FORCAS_VERTICAIS = Viga.intensidades_f_verticais
        LOCALIZACAO_SUPORTES = Viga.suportes

        fig, ax = plt.subplots()
        rect = mpatches.Rectangle((0, -0.1), TAMANHO_VIGA, 0.2, color='blue', alpha=0.7)
        for i in range(len(LOCALIZACAO_FORCAS_VERTICAIS)):
            if INTENSIDADE_FORCAS_VERTICAIS[i] > 0:
                arrow = mpatches.Arrow(LOCALIZACAO_FORCAS_VERTICAIS[i], 0.6 , 0, -0.5, width=1)
                ax.add_patch(arrow)
                ax.text(LOCALIZACAO_FORCAS_VERTICAIS[i], 0.65, str(INTENSIDADE_FORCAS_VERTICAIS[i])+'N', fontsize=12, ha='center')
            else:
                arrow = mpatches.Arrow(LOCALIZACAO_FORCAS_VERTICAIS[i], -0.6 , 0, 0.5, width=1)
                ax.add_patch(arrow)
                ax.text(LOCALIZACAO_FORCAS_VERTICAIS[i], -0.7, str(-1*INTENSIDADE_FORCAS_VERTICAIS[i])+'N', fontsize=12, ha='center')
        for i in range(len(LOCALIZACAO_SUPORTES)):
            suporte = mpatches.RegularPolygon((LOCALIZACAO_SUPORTES[i], -0.2), 3, 0.1, color='red')
            ax.text(LOCALIZACAO_SUPORTES[i], -0.35, str(LOCALIZACAO_SUPORTES[i])+'m', fontsize=12, ha='center')
            ax.add_patch(suporte)
        # Mostre o grid em y sempre de -1 a 1
        ax.set_ylim(-1, 1)
        ax.set_xlim(0 - TAMANHO_VIGA/10, TAMANHO_VIGA*1.1)
        ax.add_patch(rect)
        plt.show()

    def printar_normal(Viga):
        print("Printando gráfico da normal")
        pass
    def printar_cortante(Viga):
        print("Printando gráfico do cortante")
        pass
    def printar_fletor(Viga):
        print("Printando gráfico do fletor")
        pass
