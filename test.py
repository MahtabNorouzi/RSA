class RSA():
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e
        self.phi_n = (p-1) * (q-1)
        self.n = p*q

    def exponentiation(self, bas, exp):
        if exp == 0:
            return 1
        if exp == 1:
            return bas % self.n

        t = self.exponentiation(bas, int(exp / 2))
        t = (t * t) % self.n

        if (exp % 2 == 0):
            return t

        else:
            return ((bas % self.n) * t) % self.n


    def modInverse(self):
        m0 = self.phi_n
        y = 0
        x = 1
 
        if (self.phi_n == 1):
            return 0
 
        while (self.e > 1): 
            q = self.e // self.phi_n
            t = self.phi_n

            self.phi_n = self.e % self.phi_n
            self.e = t
            t = y
            y = x - q * y
            x = t
 
        if (x < 0):
            x = x + m0
 
        return x
 

    
    def encryption(self, m):
        x = self.exponentiation(m, self.e)
        return x % self.n

    def decryption(self,c):
        d = self.modInverse(self.e, self.phi_n)
        return pow(c, d, self.n)


rsa = RSA(1234567, 3456677, 54545)
encrypted = rsa.encryption(1382074648)
decrypted = rsa.decryption(12345)