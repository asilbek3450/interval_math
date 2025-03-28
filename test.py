from interval_math.interval import IntervalArithmetic, IntervalQator
from sympy import sin, cos, exp
import sympy as sp

qator_sin = IntervalQator(sin(sp.Symbol('x')), 0, 5)
qator_cos = IntervalQator(cos(sp.Symbol('x')), 0, 5)
qator_exp = IntervalQator(exp(sp.Symbol('x')), 0, 5)

print(qator_sin.natijani_chiqarish(0.5))
print(qator_cos.natijani_chiqarish(0.5))
print(qator_exp.natijani_chiqarish(0.5))
