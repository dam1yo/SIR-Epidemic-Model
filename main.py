
if __name__ == '__main__':
    N = int(input('Population Size = '))
    fiN = float(input('μN = '))
    fiS = float(input('μS = '))
    betaIS = float(input('βIS = '))
    S = int(input('S = '))
    So = int(input('So = '))
    t = int(input('Unit Time in days = '))
    In = int(input('I = '))
    Io = int(input('Io = '))
    epsI = float(input('γI = '))
    fiI = float(input('μI = '))
    R = int(input('R = '))
    Ro = int(input('Ro = '))
    fiR = float(input('μR = '))

    def calcSus():
        if S == So and So >= 0:
            ds = fiN - fiS - betaIS / N
            ds = ds / t
            print('Susceptibles per unit time = ', ds)
        else:
            print('S and So did not meet the criteria')

    def calcInf():
        if In == Io and Io >= 0:
            di = betaIS/N - epsI - fiI
            di = di/t
            print('Infectives per unit time = ', di)
        else:
            print('I and Io did not meet the criteria')

    def calcRem():
        if R == Ro and Ro >= 0:
            dr = epsI - fiR
            dr = dr/t
            print('Removed per unit time = ', dr)
        else:
            print("R and Ro did not meet the criteria")

    calcSus()
    calcInf()
    calcRem()
