def numeroPrimo(n):

    esPrimo = 0

    if n == 2:
        return 1
    
    #primo 
    if n % 2 != 0:
        if n % 3 != 0: 
            esPrimo = 1

    return esPrimo

# LUIS SIUL

#  OSO , oxxxo

if __name__ == '__main__':
    

    result = numeroPrimo(2027)

    if result:
        print("Numero es primo")
    else:
        print("numero no es primo")
