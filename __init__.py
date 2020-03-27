#!/usr/bin/env python3
# Simple matrix helper for working with matrices. Some features are specific, while others can be used even with custom class matrices.


def flatten_mat(mat):
    return [j for i in mat for j in i]
