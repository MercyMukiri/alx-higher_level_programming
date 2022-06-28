#!/usr/bin/python3
"""
101-lazy_matrix_mul module

This module defines the lazy matrix multiplication using Numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ multiplies two matrices"""
    return numpy.matmul(m_a, m_b)
