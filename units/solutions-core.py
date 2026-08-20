## Basic implementation

def deriv(f, x, eps=1e-8):
    return (f(x+eps) - f(x)) / eps


def deriv2(f, x, eps=1e-6):
    return (deriv(f, x+eps, eps) - deriv(f, x, eps)) / eps


def optimize(x0, f, tol=1e-4):
    x = x0
    x_new = x - deriv(f, x) / deriv2(f, x)
    while abs(x_new - x) > tol:
        x = x_new
        x_new = x - deriv(f, x) / deriv2(f, x)
    return {"x": x_new, "value": f(x_new)}


def test_fun(x):
    return x**4/4 - x**3 -x


## Implementation with error trapping and warnings.

import warnings

def optimize(x0, f, tol=1e-4):
    if not callable(f):
       raise TypeError(f"Argument `f` is not a function, it is of type {type(f)}")
    if not np.isreal(x0):
       raise TypeError(f"Argument `x0` is not numeric")
    
    x = x0
    x_new = x - deriv(f, x) / deriv2(f, x)
    while abs(x_new - x) > tol:
        x = x_new
        x_new = x - deriv(f, x) / deriv2(f, x)
    converged = True
    if deriv2(f, x) <= 0:
       warnings.warn("Positive second derivative; local maximum found")
       converged = False
    
    return {"x": x_new, "value": f(x_new), "convergence": converged}

