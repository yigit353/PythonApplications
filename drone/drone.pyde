from box_model import Box
from drone_model import Drone


def setup():
    global img_drone, img_box, speed, drone, boxes, state
    size(800, 600)
    img_drone = loadImage('drone.png')
    img_box = loadImage('box.png')
    speed = 20
    drone = Drone(0, 0, speed, 100, 100, 'drone1')
    boxes = []
    boxes.append(Box(400, 400, 100, 100, 'box1'))
    boxes.append(Box(200, 400, 100, 100, 'box2'))
    boxes.append(Box(600, 500, 100, 100, 'box2'))
    state = 'none'
    
    with open('scenarios/scenario.dat') as f:
        for s in f:
            state = s.rstrip('\n')
            print state
            my_draw()
            delay(200)
    
def draw():
    pass    
    
def my_draw():
    global state
    
    if state == 'w':
        y_next = drone.next_up_y()
        if y_next >= 0:
            drone.y = y_next
    if state == 'a':
        x_next = drone.next_left_x()
        if x_next >= 0:
            drone.x = x_next
    if state == 's':
        y_next = drone.next_down_y()
        if y_next <= height - drone.height:
            drone.y = y_next
    if state == 'd':
        x_next = drone.next_right_x()
        if x_next <= width - drone.width:
            drone.x = x_next
            
    state = 'none'
    background(30)
    image(img_drone, drone.x, drone.y, drone.width, drone.height)
    for box in boxes:
        image(img_box, box.x, box.y, box.width, box.height)

'''
def keyReleased():
    global state
    state = 'none'
'''
    
'''
def keyPressed():
    global state
    state = key
''' 