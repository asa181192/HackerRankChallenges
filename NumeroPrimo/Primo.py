def numeroPrimo(n, i):    
    if n == i:
        return 1
    if n == 1 :
        return 0
    elif n % i == 0:
        return 0
    else:
        return numeroPrimo(n, i + 1)

def esPrimo(n):
    return numeroPrimo(n,2)
# LUIS SIUL

#  OSO , oxxxo


if __name__ == '__main__':

      i = 1
      while i <= 200:
          result = esPrimo(i)

          if result:
             print("Numero es primo " + str(i))
          else:
             print("numero no es primo " + str(i))

          i += 1
  
