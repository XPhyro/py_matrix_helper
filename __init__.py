#!/usr/bin/env python3
# Simple matrix helper for working with matrices. Some features might be specific, while others might be used even with custom class matrices.


def flatten_mat(mat):
    return [j for i in mat for j in i]
