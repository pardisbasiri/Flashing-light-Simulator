import math


def calculate_i_d(v0, vd, r):
    return (v0 - vd) / r


def calculate_vd(v_t, i_d, i_s, eta):
    return eta * v_t * math.log(i_d / i_s + 1)


def solve_equations(v0, r, i_s, eta, e=0.00001):
    vd = 0.8
    v_t = 26 * 10 ** -3
    while True:
        i_d = calculate_i_d(v0, vd, r)
        new_vd = calculate_vd(v_t, i_d, i_s, eta)
        print(f"Result I: {i_d} V: {new_vd}")
        if math.fabs(new_vd - vd) < e:
            break
        vd = new_vd


solve_equations(26, -10 ** 3, 10 ** -5, 2)