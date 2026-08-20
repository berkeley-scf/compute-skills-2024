def deriv(f, x, eps = 1e-5):
    return (f(x+eps) - f(x)) / eps


def deriv2(f, x, eps = 1e-5):
    return (deriv(f, x+eps, eps) - deriv(f, x, eps)) / eps


def optimize(x0, f, tol =1e-4):
    x_new = x0 - deriv(f, x0)/ deriv2(f, x0)
    x = x0
    while abs(x_new - x) > tol:
        x = x_new
        x_new = x0 - deriv(f, x) / deriv2(f, x)
    return {"x": x_new,
            'value': f(x_new)}



