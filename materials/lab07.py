def euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclid(b, a % b)
        return d, y, x - (a // b) * y


def func(x, a, b, G, H, P, Q):
    sub = x % 3

    if sub == 0:
        x = x * G % P
        a = (a + 1) % Q

    if sub == 1:
        x = x * H % P
        b = (b + 1) % P

    if sub == 2:
        x *= x % P
        a *= 2 % Q
        b *= 2 % Q

    return x, a, b


def pollard(G, H, P):
    Q = int((P - 1) // 2)

    x = G*H
    a = 1
    b = 1

    X = x
    A = a
    B = b

    for i in range(1, P):
        x, a, b = func(x, a, b, G, H, P, Q)
        X, A, B = func(X, A, B, G, H, P, Q)
        X, A, B = func(X, A, B, G, H, P, Q)

        if x == X: break

    nom = a-A
    denom = B-b

    return (euclid(denom, Q)[1] * nom) % Q


def main():
    a = 10
    b = 64
    p = 107

    x = pollard(a, b, p)
    print(f"{a}^{x} = {b}(mod {p})")


if __name__ == '__main__':
    main()
