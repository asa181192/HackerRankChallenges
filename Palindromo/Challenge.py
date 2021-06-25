def palindromo(s):

    i = 0
    esPalindromo = 1
    # obtenemos cadea inversa
    while i < len(s):
        #textoInverso.append( (s[i] - 1) - i  )
        if s[i] != s[(len(s) - 1) - i] :
            esPalindromo = 0
            break
        i += 1

    return esPalindromo


# LUIS SIUL

#  OSO , oxxxo

if __name__ == '__main__':

    result = palindromo("alfredo")
    if result:
        print("es palindromo")
    else:
        print("no es palindromo")
