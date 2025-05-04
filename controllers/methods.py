import numpy as np

from sympy import *

x = Symbol('x')
N_MAKS = 30

def cek_lebar(lebar, e):
    if e >= lebar:
        return True

    return False

def hitung_c(a, b, f_a, f_b) -> np.float64:
    c = ((f_b*a) - (f_a*b))/(f_b - f_a)
    return np.float64(c)

def hitung_error(x_r_1, x_r):
    return np.abs(x_r_1 - x_r)

def biseksi(a, b, f_x, e, datas=[]):
    
    global x
    
    a = np.float64(a)
    b = np.float64(b)
    lebar = np.float64(0)

    f_x_func = lambdify(x, f_x)

    f_a = f_x_func(a)
    f_b = f_x_func(b)

    if (f_a * f_b) > 0:
        return np.float64(0), datas

    c = (a+b)/2

    f_c = f_x_func(c)
    
    datas.append([a, c, b, f_a, f_c, f_b])
    print(len(datas))

    if f_c * f_a < 0:
        lebar = c - a

        if cek_lebar(lebar, e):
            cp_datas = datas.copy()
            datas.clear()
            return c, cp_datas

        return biseksi(
            a=a,
            b=c,
            f_x=f_x,
            e=e
        )

    elif f_c * f_a > 0:
        lebar = b - c

        if cek_lebar(lebar, e):
            cp_datas = datas.copy()
            datas.clear()
            return c, cp_datas

        return biseksi(
            a=c,
            b=b,
            f_x=f_x,
            e=e
        )
        
def regula_falsi(a, b, f_x, e):

    global x

    a = np.float64(a)
    b = np.float64(b)

    f_x_func = lambdify(x, f_x)

    f_a = f_x_func(a)
    f_b = f_x_func(b)

    c = hitung_c(a, b, f_a, f_b)
    f_c = f_x_func(c)

    error = np.abs(f_c)

    if error > e:

        if f_c*f_a < 0:
            return regula_falsi(
                a=a,
                b=c,
                f_x=f_x,
                e=e
            )

        elif f_c*f_a > 0:
            return regula_falsi(
                a=c,
                b=b,
                f_x=f_x,
                e=e
            )
    else:
        return c
    
def iterasi_sederhana(x_initial, f_x, e, max_iterations=N_MAKS):
    
    global x
    
    func = lambdify(x, f_x)
    
    x_r = np.float64(x_initial)
    for _ in range(max_iterations):
        x_r_1 = func(x_r)

        if np.isinf(x_r_1):
            return np.inf

        error = hitung_error(x_r_1, x_r)

        if error <= e:
            return x_r_1

        x_r = x_r_1

    print("Maximum iterations reached without convergence.")
    return np.inf

def newton_raphson(x_initial, f_x, e):
    
    global x
    
    x_r = np.float64(x_initial)

    f_x_func = lambdify(x, f_x)
    f_x_val = f_x_func(x_r)

    f_x_prime_func = f_x.diff(x)
    f_x_prime_func = lambdify(x, f_x_prime_func)
    f_x_prime = f_x_prime_func(x_r)

    x_r_1 = (x_r) - (f_x_val/f_x_prime)

    error = hitung_error(x_r_1, x_r)

    if error >= e:
        return newton_raphson(
            x_initial=x_r_1,
            f_x=f_x,
            e=e
        )
    else:
        return x_r_1
    
def secant(x_r_min_1, x_r, f_x, e):

    global x
    
    x_r_min_1, x_r = np.float64(x_r_min_1), np.float64(x_r)

    f_x_func = lambdify(x, f_x)

    y_r_min_1 = f_x_func(x_r_min_1)
    y_r = f_x_func(x_r)

    x_r_1 = x_r - (y_r*(x_r-x_r_min_1))/(y_r-y_r_min_1)

    y_r_1 = f_x_func(x_r_1)

    error = hitung_error(x_r_1, x_r)

    if e < error:
        return secant(
            x_r_min_1=x_r,
            x_r=x_r_1,
            f_x=f_x,
            e=e
        )
    else:
        return x_r
