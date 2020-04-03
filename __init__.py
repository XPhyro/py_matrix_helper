#!/usr/bin/env python3
# Simple matrix helper for working with matrices. Some features might be specific, while others might be used even with custom class matrices.


def flatten_mat(mat):
    if mat is not list:
        raise TypeError("mat must be a list.")
    for i in mat:
        if i is not list:
            raise TypeError("Each element of mat must be a list.")
    inner_len = len(mat[0])
    for i in mat:
        if len(i) != inner_len:
            raise ValueError(
                "Each element of mat must be of same size, i.e. mat must be rectangular."
            )

    return [j for i in mat for j in i]
