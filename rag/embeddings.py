import numpy as np

def embed(text):
    np.random.seed(abs(hash(text)) % 10**8)
    return np.random.rand(1536).astype("float32")
