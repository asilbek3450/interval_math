class Interval:
    def __init__(self, lower, upper):
        if lower > upper:
            raise ValueError("Quyi chegara yuqori chegaradan katta bo‘lishi mumkin emas!")
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f"[{self.lower}, {self.upper}]"

    def __add__(self, other):
        if isinstance(other, Interval):
            return Interval(self.lower + other.lower, self.upper + other.upper)
        return Interval(self.lower + other, self.upper + other)

    def __sub__(self, other):
        if isinstance(other, Interval):
            return Interval(self.lower - other.upper, self.upper - other.lower)
        return Interval(self.lower - other, self.upper - other)

    def __mul__(self, other):
        if isinstance(other, Interval):
            values = [self.lower * other.lower, self.lower * other.upper,
                      self.upper * other.lower, self.upper * other.upper]
            return Interval(min(values), max(values))
        return Interval(self.lower * other, self.upper * other)

    def __truediv__(self, other):
        if isinstance(other, Interval):
            if other.lower <= 0 <= other.upper:
                raise ValueError("Bo‘lish amali 0 ga bo‘lishni o‘z ichiga oladi!")
            values = [self.lower / other.lower, self.lower / other.upper,
                      self.upper / other.lower, self.upper / other.upper]
            return Interval(min(values), max(values))
        if other == 0:
            raise ValueError("0 ga bo‘lish mumkin emas!")
        return Interval(self.lower / other, self.upper / other)
