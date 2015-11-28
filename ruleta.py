import random as rand

def main ():
	#capital es la cuantitat de diners de la que disposem
	# aposta es la cuantitat de diners que apostem
	# numero es el numero al qual apostem
	# sorteig es el numero que surt a la ruleta
	# nguanyades es el contador de les partides que em guanyat
	# nperdudes es el contador de les partides que em perdut
	capital=1000
	aposta=0
	numero=0
	sorteig=0
	nguanyades=0
	nperdudes=0
	print "Benvingut a la ruleta de la sort."
	print "Tens un capital de " + `capital` +"e, quan vols apostar?"
	aposta =  input()
	while (aposta!=0 and capital!=0):
		#Entrara en aquest bucle mentres s'aposti mes de 0 i es tingui capital.	
		if (aposta<=capital and aposta>0):
			#Si l'aposta es correcta, es a dir, menor o igual que el capital i positiva ens demanara el numero al que volem apostar.			
			print "Introdueix el numero al qual vols apostar:"
			numero = input()
			while ((numero<=0) or (numero>=37)):
				#Si apostem a un numero erroni que no esta entre 1 i 36 ambdos inclosos ens dira que es erroni i que n'introduim un altre.
				print "No has introduit un numero valid torna-ho a intentar!"
				print "Introdueix el numero al qual vols apostar: "
				numero = input()
			#Quan el numero sigui correcte sortira del bucle, fara el sorteig i ens dira si em guanyat o perdut.
			sorteig = rand.randint(0,37)
			print "Has apostat al numero "+`numero`+" i ha sortit el numero " + `sorteig`
			if (sorteig==numero):
				aposta=aposta*36
				print "Has guanyat " + `aposta`+ "e."
				capital=capital+aposta
				nguanyades+=1
			else:
				print "Has perdut "+`aposta`+"e."
				capital=capital-aposta
				nperdudes+=1
			if (capital!=0):
				#Ens donara l'opcio continuar jugant si el capital no es 0, perque en cas d'arruinar-nos no ens ho demani.
				print "Tens un capital "+`capital`+"e, quan vols apostar?"
				aposta = input()
		else:
			#Si la cantitat apostada era negativa o superior al capital ens dira que ho tornem a provar.
			print "No has introduit una quantitat valida torna-ho a intentar!"
			aposta = input()
		
	if (capital==0):
	#Si t'has arruinat et dona un misatge
		print "Mala sort! Ho has perdut tot!"
	else:
	#Si ens queda ens en mostrara la quantitat
		print "El teu capital final es: "+`capital`+"."
	#Finalment ens mostra les partides guanyades i perdudes.
	print"Has guanyat "+ `nguanyades` + " partides i n'has perdut "+`nperdudes`+"."

main()