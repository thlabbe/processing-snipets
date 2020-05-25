#ellipse(50,50,80,80)
#from Math import sqrt, cos, sin
golden_angle =radians(137.5)

sqrts = list()
sins = list()
coss = list()
    
def setup():
    init()
    size(1024, 1024)
    background(100)
    strokeWeight(8)
    smooth()
    colorMode(RGB,1024)

    print(len(sqrts))    

              
def draw():
    clear()
    #stroke( mouseY )
    x = 512
    y = 512
    # C = mouseX / 10
    C = 30
    for a in range(0,1024):
        stroke(1024-a)
        r = C * sqrts[a] 
        x += r * coss[a] 
        y += r * sins[a] 
        point(x, y)   
    
def init():
    '''
    cos sin et sqrt sont "couteuses" :on ne les calcule qu'une fois
    '''
    global sqrts 
    global sins 
    global coss 
    sqrts = [sqrt(a) for a in range(0,1024)] 
    sins = [sin(golden_angle * a) for a in range(0,1024)] 
    coss = [cos(golden_angle * a) for a in range(0,1024)] 
