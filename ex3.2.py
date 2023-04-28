reiniciar = str.lower ( input ( "Deseja iniciar o programa? Sim/Não: " ) )
freepass = 0
while ( reiniciar == "sim" ) and ( reiniciar != "não" ):
    idade = int ( input ( "Forneça a idade: " ) )

    if ( idade <= 10 ) or ( idade > 60 ):
        freepass += 1

    reiniciar = str.lower ( input ( "Continuar? Sim/Não: " ) )

print ( "A quantidade de pessoas que tiveram entrada gratuita é: ", freepass, "." )


    
