# Arquivo responsável pela criação da viga


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

# Importar de outros arquivos:
from modules.viga_analysis import Calculator
from modules.viga_printer import Printer


class Viga:
    # Construtor da classe
    def __init__(self, tamanho, localizacao_f_verticais, intensidades_f_verticais, momentos, suportes):
        self.tamanho = tamanho
        self.localizacao_f_verticais = localizacao_f_verticais
        self.intensidades_f_verticais = intensidades_f_verticais
        self.momentos = momentos
        self.suportes = suportes
        Printer.printar_desenho_inicial(self)

    # Método para calcular as reações de apoio
    def calcular_reacoes(self):
        Calculator.calcular_forcas_horizontais(self)
        Calculator.calcular_forcas_verticais(self)
        Calculator.calcular_momento(self)

    def printar_graficos(self):
        Printer.printar_normal(self)
        Printer.printar_cortante(self)
        Printer.printar_fletor(self)

    





