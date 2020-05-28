#!/usr/bin/env python3
# Simple matrix helper for working with matrices. Some features might be specific, while others might be used even with custom class matrices.


def flatten_mat(mat):
    if not isinstance(mat, list):
        raise TypeError("mat must be a list.")
    for i in mat:
        if not isinstance(i, list):
            raise TypeError("Each element of mat must be a list.")
    inner_len = len(mat[0])
    for i in mat:
        if len(i) != inner_len:
            raise ValueError(
                "Each element of mat must be of same size, i.e. mat must be rectangular."
            )

    return [j for i in mat for j in i]

def init_mat(h, w, v):
    if not isinstance(h, int):
        raise TypeError("h must be an int.")
    if not isinstance(w, int):
        raise TypeError("w must be an int.")
    if not isinstance(v, float):
        raise TypeError("v must be a float.")

    if h <= 0:
        raise ValueError("h must be positive.")
    if w <= 0:
        raise ValueError("w must be positive.")

    m = []
    for i in range(h):
        l = []
        for i in range(w):
            l.append(v)
        m.append(l)

    return m
