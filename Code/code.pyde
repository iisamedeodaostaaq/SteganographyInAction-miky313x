def setup():
    size(500,500)
    noStroke()
    
    redpx=0
    bluepx=0
    greenpx=0
    count=0
    count_quadrati=0
    larg=0
    altezza=0
    incremento_alt=50
    testo = open("testo.txt")              #apre il testo lo mette in una stringa e legge la sua lunghezza
    testo_tot = testo.read()
    lunghezza_testo=len(testo_tot)
    while count < lunghezza_testo :
        if count < lunghezza_testo :
            redpx = ord(testo_tot[count])  #prende la lettera e la trasforma in codice ascii con ord
            count=count+1
        else:                              #se finiscono i caratteri il quadrato viene completato con il valore 255
            redpx=255 
        if count < lunghezza_testo :
            bluepx = ord(testo_tot[count])
            count=count+1
        else:
            bluepx=255 
        if count < lunghezza_testo :
            greenpx = ord(testo_tot[count])
            count=count+1
            count_quadrati=count_quadrati+1
        else:
            greenpx=255
            count_quadrati=count_quadrati+1
        if count_quadrati % 10 == 0 :            #va a capo quando arriva a 10 quadrati e riparte da sinistra
            larg=0
            altezza=altezza+incremento_alt
        fill(redpx, bluepx, greenpx);            #prende i numeri convertiti e crea un quadrato
        rect(larg,altezza,50,50)
        larg=larg+50
        print(count, redpx, bluepx, greenpx)

    testo.close()
    while count_quadrati % 10 != 0 :           #quando il testo e' finito e non arriva a 10 quadrati completa la linea con quadrati neri
        fill(0, 0, 0);
        rect(larg,altezza,50,50)
        larg=larg+50
