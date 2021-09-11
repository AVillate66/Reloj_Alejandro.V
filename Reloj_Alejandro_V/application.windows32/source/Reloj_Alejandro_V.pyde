horizontal_position= 0 
minutos= 0
hora =0

def setup(): 
    size (700,300)

def draw ():
    global horizontal_position
    global minutos
    global hora 
    
    background(51)
    
    ellipse(horizontal_position, 50, 75,75)
    
    if horizontal_position >width:
        horizantal_position==0
    else:
        horizontal_position = map(second(),0,59, 0, width)
    
    ellipse(minutos,150, 85, 75)
    
    if minutos > width:
        minutos =0 
    else:
        minutos = map(minute(),0,59,0, width)
   
    ellipse (hora, 250, 100, 75) 
    if hora > width:
        hora= 0 
    else:
        hora= map(hour(),0,12,0,width) 
                
                  
              
          
        
