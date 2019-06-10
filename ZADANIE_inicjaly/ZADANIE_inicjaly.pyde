def setup():
    size(400,400)
    textSize(120)
    textAlign (CENTER)
    background(23,200,33)
def draw():
    if keyPressed:
        if key == 'j':
            fill(23,16,18)
        else:
            fill(255,221,133)
        text("J", width/2 - 120, height/2-50)
        if key == 'a':
            fill(23,16,18)
        else:
            fill(255,221,133)
        text("A", width/2 + 120, height/2-50)  # piszesz dopiero, gdy ustalisz kolor w którym ma napisać
    print(mouseX, mouseY)
    # brakuje obsługi myszy i strzałek



    s= createShape()
    s.beginShape()
    s.fill(33,23,144)
    s.noStroke()
    s.vertex(134, 144)
    s.vertex(0, 222, 400)
    s.vertex(323, 350)
    s.vertex(263, 200)    
    s.vertex(120, height/3*2- 20)
    s.endShape(CLOSE)
    shape(s,25,25)
