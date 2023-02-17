import numpy as np
from .model import DefaultModel


def video2emb(video: np.array) -> np.array:
    vec = DefaultModel.get().forward(video)
    return vec