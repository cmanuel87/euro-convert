
def validar_entrada1( texto ):
    try:
         return str(long(texto))
    except ValueError:
         return ""

def validar_entrada2( texto ):
    try:
         return str(float(texto))
    except ValueError:
         return ""

def pelas_a_euros( entrada ): #Aquí viene lo que han tecleado
    return "%.2f" % (float(entrada)/166.386)

def euros_a_pelas( entrada ): #Aquí viene lo que han tecleado
    return "%d" % (float(entrada)*166.386)

