import numpy as np


def calculate(arr):

    if len(arr) != 9:

        raise ValueError('List must contain nine numbers.')

    else:

        d = {}

        arr_row = [arr[:3], arr[3:6], arr[6:]]
        arr_col = [[a for a in arr if (arr.index(a)) in [i, 3 + i, 6 + i]] for i in range(3)]

        arr_mean = [np.mean([arr_row], axis=1), np.mean([arr_col], axis=1), np.mean(arr)]
        d['mean'] = [a.tolist()[0] for a in arr_mean[:-1]] + [arr_mean[-1]]

        arr_var = [np.var([arr_row], axis=1), np.var([arr_col], axis=1), np.var(arr)]
        d['variance'] = [a.tolist()[0] for a in arr_var[:-1]] + [arr_var[-1]]

        arr_std = [np.std([arr_row], axis=1), np.std([arr_col], axis=1), np.std(arr)]
        d['standard deviation'] = [a.tolist()[0] for a in arr_std[:-1]] + [arr_std[-1]]

        arr_max = [np.max([arr_row], axis=1), np.max([arr_col], axis=1), np.max(arr)]
        d['max'] = [a.tolist()[0] for a in arr_max[:-1]] + [arr_max[-1]]

        arr_min = [np.min([arr_row], axis=1), np.min([arr_col], axis=1), np.min(arr)]
        d['min'] = [a.tolist()[0] for a in arr_min[:-1]] + [arr_min[-1]]

        arr_sum = [np.sum([arr_row], axis=1), np.sum([arr_col], axis=1), np.sum(arr)]
        d['sum'] = [a.tolist()[0] for a in arr_sum[:-1]] + [arr_sum[-1]]

        return d