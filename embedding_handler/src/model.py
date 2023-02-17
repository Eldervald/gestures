import numpy as np


class Model:
    def forward(self, x):
        return np.zeros(256, dtype=np.float64)


class DefaultModel:
    _model = None

    @classmethod
    def get(cls):
        if cls._model is None:
            cls._model = Model()
        return cls._model
