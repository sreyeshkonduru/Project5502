import numpy as np
import math
from Project5502.production.function import predict_subscribe

def test_make_prediction():
    watch = -8.1
    duration = 1.4
    ctr = -0.7
    interest = 0
    misses = 0.32
    subscribe = 0.67
    
    result = predict_subscribe(watch, duration, ctr, interest)
    
    assert isinstance(result,dict)
    assert isinstance(result['Misses Out'], np.float64)
    assert isinstance(result['Subscribes'], np.float64)
    assert math.isclose(result['Misses Out'], misses, abs_tol=0.1)
    assert math.isclose(result['Subscribes'], subscribe, abs_tol=0.1)