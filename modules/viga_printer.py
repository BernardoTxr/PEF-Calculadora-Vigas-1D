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

class Printer:
    def printar_normal(Viga):
        print("Printando gráfico da normal")
        pass
    def printar_cortante(Viga):
        print("Printando gráfico do cortante")
        pass
    def printar_fletor(Viga):
        print("Printando gráfico do fletor")
        pass
