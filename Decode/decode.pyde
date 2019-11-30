count_quadrati=0
p=1
redpx1=1
blupx1=1
greenpx1=1
string=''
immagine = loadImage("Out.tiff")
immagine.loadPixels()

while redpx1!=0 or blupx1!=0 or greenpx1!=0 or redpx1<128 or blupx1<128 or greenpx1<128 :               #ripete il ciclo finche non e presente il colore nero(=0) o non e' un valore ascii(>128)
    redpx=red(immagine.pixels[p])                                  #prende il valore rosso del pixel
    blupx=blue(immagine.pixels[p])
    greenpx=green(immagine.pixels[p])
    redpx1=int(redpx)                                              #pone il valore intero perche era preso come float
    blupx1=int(blupx)
    greenpx1=int(greenpx)
    print(chr(redpx1))                                             #converte il valore numerico in carattere
    print(chr(greenpx1))
    print(chr(blupx1))
    string=string+chr(redpx1)+chr(greenpx1)+chr(blupx1)            #aggiunge alla stringa vuotai caratteri ricavati
    p=p+50
    count_quadrati=count_quadrati+1
    if count_quadrati==10:                                         #va a capo quando passa i 10 quadrati
        count_quadrati=0
        p=p+(49*500)
    if redpx1==0 or blupx1==0 or greenpx1==0 or redpx1>128 or blupx1>128 or greenpx1>128 :    #interrompe il ciclo quando incontra il quadrato nero(=0) o un valore sopra il 128
        print string
        break
  
  
