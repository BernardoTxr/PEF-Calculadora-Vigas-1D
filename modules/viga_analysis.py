# Arquivo responsável pela análise da viga

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

class Calculator:
    def calcular_forcas_horizontais(Viga):
        print("Calculando forças horizontais")
        pass
    def calcular_forcas_verticais(Viga):
        print("Calculando forças verticais")
        pass
    def calcular_momento(Viga):
        print("Calculando momento")
        pass