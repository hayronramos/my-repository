reboot = str.lower( input( "Deseja iniciar o programa? Sim/Não: " ) )
totalvacinas = 0
while ( reboot == "sim" ) and ( reboot != "não" ):
    idade = int ( input ( "Forneça a idade: " ) )
    if ( idade >= 3 ) and ( idade <= 6 ):
        totalvacinas += 1
    reboot = str.lower( input( " Deseja continuar o programa? Sim/Não: " ) )
print ( "O total de vacinas aplicadas foi: ", totalvacinas, "." )
