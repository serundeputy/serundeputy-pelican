import numpy as np
import pandas as pd

def positivity(cases, tests):
    new_tests = tests['Molecular All Tests New']
    new_cases = cases['Positive New']
    avgs = (new_cases / new_tests) * 100
    
    return round(avgs.mean(), 2)
