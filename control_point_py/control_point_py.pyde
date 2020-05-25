from control_point import ControlPoint2D

ctrl_points = []
locked_ctrl = -1
over_ctrl = -1
offset = ( 0.0, 0.0)
points = [ (50, 50), (150, 50), (200, 250), (400,400) ]

def setup():
    global ctrl_points, points
    w = 20 
    for p in points:
        ctrl_points.append(ControlPoint2D(p[0],p[1], w))
    #ctrl_points= [ControlPoint2D(50,50, w), ControlPoint2D(150, 50, w), ControlPoint2D(200, 250, w)]
    size(512, 512, OPENGL)
    strokeWeight(2)    
    
def draw():
    global ctrl_points
    global points
    background(100)
    noStroke()
    for i, c in enumerate(ctrl_points):
        c.show()    
        points[i] = (c.x, c.y)
    noFill()
    strokeWeight(3)
    stroke(255,255,0,250)
    curve( points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1], points[3][0], points[3][1])   
    stroke(255,0,0,250)
    bezier( points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1], points[3][0], points[3][1])   
    noStroke()
def mouseMoved():
    global ctrl_points, offset, over_ctrl
    over_ctrl = -1
    for i, c in enumerate(ctrl_points):
        if c.is_mouse_over():
            over_ctrl = i       
            
def mousePressed():
    global ctrl_points, over_ctrl, locked_ctrl, offset
    locked_ctrl = over_ctrl
    w = (0.0, 0.0)
    if locked_ctrl > -1:
        w = (ctrl_points[locked_ctrl].x, ctrl_points[locked_ctrl].y)
        
    offset = (mouseX - w[0], mouseY - w[1])
     
def mouseDragged():
    global locked_ctrl, offset
    
    if (locked_ctrl > -1):
        ctrl_points[locked_ctrl].x = mouseX - offset[0]
        ctrl_points[locked_ctrl].y = mouseY - offset[1]
    
