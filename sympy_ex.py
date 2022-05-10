from sympy import solve, Symbol, pprint
x = Symbol('x')
k = Symbol('k')
poly = x**2 + 3*x + 4
poly2 = k-2
print(solve(poly2, 4))