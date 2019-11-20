def setup():
    size(500,500)
    
    redpx=0
    bluepx=0
    greenpx=0
    count=0
    count_quadrati=0
    larg=0
    altezza=0
    incremento_alt=50
    # Legge un file.
    testo = open("testo.txt")
    testo_tot = testo.read()
    lunghezza_testo=len(testo_tot)
    while count < lunghezza_testo :
        if count < lunghezza_testo :
            redpx = ord(testo_tot[count])
            count=count+1
        else:
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
        if count_quadrati % 10 == 0 :
            larg=0
            altezza=altezza+incremento_alt
        fill(redpx, bluepx, greenpx);
        rect(larg,altezza,50,50)
        larg=larg+50
        print(count, redpx, bluepx, greenpx)

    testo.close()
    while count_quadrati % 10 != 0 :
        fill(255, 255, 255);
        rect(larg,altezza,50,50)
        larg=larg+50
