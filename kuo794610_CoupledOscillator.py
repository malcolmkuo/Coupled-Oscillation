from vpython import *
#Web VPython 3.2



x1 = -0.05     # initial x position of block 1
x2 = 0        # initial x position of block 2


x1dot = 0     # velocity of block 1
x2dot = 0     # velocity of block 2

left = sphere(pos=vector(-.2,0,0),radius=0.01, color=color.red)
right = sphere(pos=vector(0.2,0,0),radius=0.01, color=color.red)
block1 = box(pos=vector(-.07+x1,0,0),size=vector(0.04,0.02,0.02), color=color.yellow)
block2 = box(pos=vector(0.07+x2,0,0),size=vector(0.04,0.02,0.02), color=color.cyan)
spring1=helix(pos=left.pos, axis=block1.pos-left.pos, radius=0.01, thickness=0.003)
spring2 = helix(pos=block1.pos, axis=block2.pos-block1.pos, radius=0.005,thickness=0.003)
spring3 = helix(pos=right.pos, axis=block2.pos-right.pos, radius = 0.01, thickness=0.003)


#create and label the position graphs of each block
g1 = graph(xtitle="t",ytitle="x",width=500, height=250)
f1 = gcurve(color=color.blue, label="x1")
f2 = gcurve(color=color.red, label="x2")
f3 = gcurve(color=color.green)
f4 = gcurve(color=color.purple)

scene.waitfor("click")
#initial conditions
k = 15               # outer spring constants
m = 0.1             # mass of the 2 blocks
b = 30               # middle spring constant
t = 0                # time
dt = 0.01            # change in time for the animation
w1 = sqrt(k/m)       # frequency of block 1
w2 = sqrt((k+2*b)/m) # frequency of block 2


while t<5:
  rate(50)

   
  F1 = -k*x1-b*(x1-x2)         # force acting on block 1
  F2 = -k*x2 - b*(x2-x1)       # force acting on block 2
  x1ddot = F1/m                #acceleration written in terms of position
  x2ddot = F2/m               
  #update velocities and positions of the blocks
  x1dot = x1dot + x1ddot*dt
  x2dot = x2dot + x2ddot*dt
  x1 = x1 + x1dot*dt
  x2 = x2 + x2dot*dt
  block1.pos = vector(-0.07+x1,0,0)
  block2.pos = vector(0.07+x2,0,0)
  # update the position of the springs
  spring1.axis=block1.pos-left.pos
  spring2.pos=block1.pos
  spring2.axis=block2.pos-block1.pos
  spring3.axis = block2.pos - right.pos
  #update time
  t = t + dt
  #update positions of the blocks
  y1 = cos(w1*t)
  y2 = cos(w2*t)
  x1a = .5*(y1+y2)
  x2a = .5*(y1-y2)  
  #plotting the positions of the blocks
  f1.plot(t,x1+.05)
  f2.plot(t,x2+0.2)
  f3.plot(t,x1a)
  f4.plot(t,x2a + 0.25)
