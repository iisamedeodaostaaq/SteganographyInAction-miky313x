count_quadrati=0
p=1
redpx1=1
blupx1=1
greenx1=1
string=''
immagine = loadImage("Out.tiff")
immagine.loadPixels()

while redpx1==0 or blupx1==0 or greenpx1==0 or redpx1>128 or blupx1>128 or greenpx1>128 :
    redpx=red(immagine.pixels[p])
    blupx=blue(immagine.pixels[p])
    greenpx=green(immagine.pixels[p])
    redpx1=int(redpx)
    blupx1=int(blupx)
    greenpx1=int(greenpx)
    print(chr(redpx1))
    print(chr(greenpx1))
    print(chr(blupx1))
    string=string+chr(redpx1)+chr(greenpx1)+chr(blupx1)
    print string
    p=p+50
    count_quadrati=count_quadrati+1
    if count_quadrati==10
        count_quadrati=0
        p=p+(49*500)
  
  
  
