


class ControlPoint2D(object):
    
    def __init__(self, x, y, w=3):
        self.x = x
        self.y = y
        self.w = w / 2
        self.active = False
        self.active_color = color(250, 155, 100, 205)
        self.inactive_color = color(150, 155, 100, 205)
            
    def show(self):
        rectMode(RADIUS)
        noStroke()
        
        if self.active:
            c = self.active_color            
        else:
            c = self.inactive_color
            
        fill(c)
        rect(self.x , self.y, self.w, self.w)
        noFill()
        
    def is_mouse_over(self):
        self.active = (mouseX > self.x - self.w and mouseX < self.x + self.w and mouseY > self.y - self.w and mouseY < self.y + self.w) 
        # if self.active:
        #    msg = [ 'mouse', (mouseX, mouseY), 'coords', (self.x, self.y), 'w',self.w ]
        #    println(msg)
        return self.active
