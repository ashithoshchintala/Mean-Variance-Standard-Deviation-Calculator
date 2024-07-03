import numpy as np

def calculate(lists):
    if len(lists) == 9:
        values = np.array(lists)
        matrix = values.reshape(3, 3)
        print(matrix)
        calculations = {
            'mean': [
                np.mean(matrix, axis=0).tolist(),
                np.mean(matrix, axis=1).tolist(),
                np.mean(matrix).tolist()
            ],
            'variance': [
                np.var(matrix, axis=0).tolist(),
                np.var(matrix, axis=1).tolist(),
                np.var(matrix).tolist()
            ],
            'standard deviation': [
                np.std(matrix, axis=0).tolist(),
                np.std(matrix, axis=1).tolist(),
                np.std(matrix).tolist()
            ],
            'max': [
                np.max(matrix, axis=0).tolist(),
                np.max(matrix, axis=1).tolist(),
                np.max(matrix.flatten()).tolist()
            ],
            'min': [
                np.min(matrix, axis=0).tolist(),
                np.min(matrix, axis=1).tolist(),
                np.min(matrix.flatten()).tolist()
            ],
            'sum': [
                np.sum(matrix, axis=0).tolist(),
                np.sum(matrix, axis=1).tolist(),
                np.sum(matrix.flatten()).tolist()
            ]
        }
    else:
        raise ValueError('List must contain nine numbers.')
    
    return calculations
