import numpy as np
from ppca_rs import Dataset

dataset = Dataset(np.matrix([[1.0, 1.0, np.nan], [1.0, 1.0, np.nan]], dtype="float64"))

print(dataset.empty_dimensions())
