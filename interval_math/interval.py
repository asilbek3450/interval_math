import sympy as sp

class IntervalArithmetic:
    def __init__(self, lower, upper):
        if lower > upper:
            raise ValueError("Quyi chegara yuqori chegaradan katta bo‘lishi mumkin emas!")
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f"[{self.lower}, {self.upper}]"

    def __add__(self, other):
        if isinstance(other, IntervalArithmetic):
            return IntervalArithmetic(self.lower + other.lower, self.upper + other.upper)
        return IntervalArithmetic(self.lower + other, self.upper + other)

    def __sub__(self, other):
        if isinstance(other, IntervalArithmetic):
            return IntervalArithmetic(self.lower - other.upper, self.upper - other.lower)
        return IntervalArithmetic(self.lower - other, self.upper - other)

    def __mul__(self, other):
        if isinstance(other, IntervalArithmetic):
            values = [self.lower * other.lower, self.lower * other.upper,
                      self.upper * other.lower, self.upper * other.upper]
            return IntervalArithmetic(min(values), max(values))
        return IntervalArithmetic(self.lower * other, self.upper * other)

    def __truediv__(self, other):
        if isinstance(other, IntervalArithmetic):
            if other.lower <= 0 <= other.upper:
                raise ValueError("Cheksiz bo'lishi mumkin!")
            values = [self.lower / other.lower, self.lower / other.upper,
                      self.upper / other.lower, self.upper / other.upper]
            return IntervalArithmetic(min(values), max(values))
        if other == 0:
            raise ValueError("0 ga bo‘lish mumkin emas!")
        return IntervalArithmetic(self.lower / other, self.upper / other)

class IntervalQator:
    def __init__(self, funksiya, x0, daraja=5):
        self.x = sp.Symbol('x')
        self.funksiya = funksiya
        self.x0 = x0
        self.daraja = daraja
        self.taylor_qatori = self._taylorni_hisoblash()
    
    def _taylorni_hisoblash(self):
        qator = sp.series(self.funksiya, self.x, self.x0, self.daraja + 1).removeO()
        hadlar = qator.as_ordered_terms()
        formatlangan_hadlar = []
        for had in reversed(hadlar):
            had = had.rewrite(sp.factorial)
            formatlangan_hadlar.append(had)
        return sum(formatlangan_hadlar)
    
    def qiymatni_hisoblash(self, x_qiymat):
        natija = self.taylor_qatori.subs(self.x, x_qiymat)
        return natija
    
    def __repr__(self):
        qator_str = str(self.taylor_qatori).replace("factorial(", "").replace(")", "!")
        return f"Taylor({self.funksiya}, {self.x0}, {self.daraja}) = {qator_str}"

    def natijani_chiqarish(self, x_qiymat):
        natija = self.qiymatni_hisoblash(x_qiymat)
        return f"Taylor({self.funksiya}, {self.x0}, {self.daraja}) = {self.__repr__().split('= ')[1]}\nF({x_qiymat}) ≈ {natija.evalf():.3f}"


