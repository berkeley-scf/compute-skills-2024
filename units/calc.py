import numpy as np
import time

def run_linalg(n):
    z = np.random.normal(0, 1, size=(n, n))
    print(time.time())
    x = z.T.dot(z)   # x = z'z
    print(time.time())
    U = np.linalg.cholesky(x)  # factorize as x = U'U
    print(time.time())

## This allows us to run the code from the command line
## without running it when we import the file as a module.
if __name__ == '__main__':
    run_linalg(4000)
