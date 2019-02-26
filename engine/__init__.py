"""Autodiscussions eg. INCAR."""
import pandas as pd, numpy as np

class Struct(object):

    def __init__(self):
        """
        struct in opt->struct->elecstruct

        :ivar np.array(3,3) A: translation vector of crystal cell, or None
        :ivar pd.DataFrame(x,y,z,symbol) X:

        """
        super().__init__()
        self.A = None
        self.X = pd.DataFrame(columns=['x', 'y', 'z', 'symbol'])
