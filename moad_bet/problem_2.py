class Polynomial:
    def __init__(self, coefficients):
        self.coefficients: list = coefficients

    def __str__(self):
        ans = []
        for i, val in enumerate(self.coefficients):
            if val == 0:
                continue
            if i == 0:
                ans.append(f'{val}')
            else:
                if val > 0:
                    ans.append("+")
                else:
                    ans.append("-")
                val = abs(val)
                ans.append(f'{val if val != 1 else ""}x{f'^{i}' if i != 1 else ""}')
        #print(ans)
        return " ".join(ans)

    def add(self, other):
        i = 0
        u = 0
        coefs = []
        while i < len(self.coefficients) and u < len(other.coefficients):
            coefs.append(self.coefficients[i] + other.coefficients[u])
            i += 1
            u += 1
        while i < len(self.coefficients):
            coefs.append(self.coefficients[i])
            i += 1
        while u < len(other.coefficients):
            coefs.append(other.coefficients[u])
            u += 1
        #print(coefs)
        return Polynomial(coefs)

    def subtract(self, other):
        neg_coefs = []
        for i in other.coefficients:
            neg_coefs.append(i * -1)
        return self.add(Polynomial(neg_coefs))

    def multiply(self, other):
        coefs = []
        for i in range(len(self.coefficients) + len(other.coefficients)):
            coefs.append(0)
        for i, k in enumerate(self.coefficients):
            for u, p in enumerate(other.coefficients):
                coefs[i + u] += k * p
        #print(coefs)
        return Polynomial(coefs)

    def evaluate(self, x):
        ans = 0
        for i, val in enumerate(self.coefficients):
            ans += val * (x ** i)
        return ans

p = Polynomial([1, 2, 3])

print(p)
