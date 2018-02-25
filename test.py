class Polynomial:
    def terms(self, terms):
        self.terms = terms
    def askPolynomial(self):
        polynomial = input()
    def createTerms(self):
        pass
class Terms:
    def __init__(self, coeff, vari):
        self.coeff = coeff
        self.vari = vari
        self.exponent = ""
    #Getters and Setters
    def setCoeff(self, coeff):
        self.coeff = coeff
    def setExponent(self, exponent):
        self.exponent = exponent
    def setVari(self, vari):
        self.vari = vari
    def getVari(self):
        return self.vari
    def getExponent(self):
        return self.exponent
    def getCoeff(self):
        return self.coeff
    #Loops through term and stops looping when non-numerical issue is encountered
    #Stores Coefficient as an integer in object
    def storeCoeff(self, term):
        coefficient = ''
        vari = term
        for n in term:
            if(n.isdigit()):
                coefficient += n
                new_vari = vari.replace(n, "")
            else:
                self.setCoeff(coefficient)
                self.setVari(new_vari)
                return int(coefficient)
    #Cehcks x is after coeff, therefore, power rule should be used
    def is_power_rule(self, term):
        for n in term:
            if(n.isalpha() and n == 'x'):
                return True
        return False

    def power_rule(self, term):
        exponent = ""
        n = term.find("^", 0, len(term))
        for i in range(n+1,len(term)):
            #Records all numerical values to right of a carrot ^^
            exponent += term[i]
            term = term[:i] + term[i+1:]
        #Loops through exponent to make sure values are all numerical
        self.setCoeff(int(exponent) * int(self.getCoeff()))
        self.setExponent(int(exponent)-1)
        self.setVari(term)
        return str(self.getCoeff()) + " " + self.getVari() + " " + str(self.getExponent())


fx = input("Please enter Polynomial")
new_term = Terms("1", "x")
print("storing")
new_term.storeCoeff(fx)
print(new_term.getVari())
if (new_term.is_power_rule(fx)):
    print(new_term.power_rule(new_term.getVari()))