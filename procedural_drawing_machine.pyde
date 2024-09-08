class Agent:
    # constructor to set initial agent values
    def __init__(self):
        self.x = random(17, width - 17)
        self.y = random(17, height - 17)
        self.vx = random(-2,2)
        self.vy = random(-2, 2)
        self.radius = random(8, 16)
        self.diam = 2 * self.radius
    
    # update agent position
    def update(self): 
        # update position
        self.updateByVelocity()
        # self.updateRandom()
        # self.updateNearest()

        # check boundary
        self.bounceBoundary()
        # self.wrapBoundary()
        # self.resetBoundary()
  
    # if agent gets to the edges, bounce back
    def bounceBoundary(self): 
        if self.x + self.radius >= width or self.x - self.radius <= 0: 
            self.vx *= -1
    
        if self.y + self.radius >= height or self.y - self.radius <= 0: 
            self.vy *= -1
  
    # if agent gets to the edges, wrap around to the opposite edge
    def wrapBoundary(self):
        if self.x > width: 
            self.x = self.x % width
    
        if self.x < 0: 
            self.x = self.x + width
    
        if self.y > height: 
            self.y = self.y % height
    
        if self.y < 0: 
            self.y = self.y + height
    

 # if agent gets to the edges, reset its position, velocity, etc
    def resetBoundary(self):
        if self.x > width or self.x < 0 or self.y > height or self.y < 0: 
            self.x = random(17, width - 17)
            self.y = random(17, height - 17)
            self.vx = random(-2, 2)
            self.vy = random(-2, 2)
            self.radius = random(8, 16)
            self.diam = 2 * self.radius
    
    # use velocity values to update position
    def updateByVelocity(self):
        self.x += self.vx
        self.y += self.vy
  
    # use random velocity values to update position
    def updateRandom(self): 
        self.vx = random(-3,3)
        self.vy = random(-3,3)
        self.x += self.vx
        self.y += self.vy
    
    def distComp(self, agentA, agentB): 
        distA = dist(self.x, self.y, agentA.x, agentA.y)
        distB = dist(self.x, self.y, agentB.x, agentB.y)
        return distA - distB

    # move away from nearest agent
    def updateNearest(self): 
        sortedByDist = agents.sorted(self.distComp.bind(self))
        closestAgent = sortedByDist[1]
        self.vx = map(closestAgent.x - self.x, -width, width, 4, -4)
        self.vy = map(closestAgent.y - self.y, -height, height, 4, -4)
        self.x += self.vx
        self.y += self.vy
    
    # draw agent
    def drawAgent(self): 
        ellipse(self.x, self.y, self.diam, self.diam)

    # draw based on currentMode
    def draw(self):
        if currentMode == POINT_MODE: 
            stroke(0)
            self.drawPoint()
        elif currentMode == FURTHEST_MODE: 
            stroke(0, 8)
            self.drawFurthest()
        elif currentMode == NEAREST_MODE: 
            stroke(0, 8)
            self.drawNearest()
        elif currentMode == OVERLAP_MODE:
            stroke(0, 16)
            noFill()
            self.drawOverlap()

    # draw black point at x, y
    def drawPoint(self):
        point(self.x, self.y)
  
    # draw a line between each agent and the agent furthest away from it
    def drawFurthest(self): 
        sortedByDist = agents.sorted(self.distComp.bind(self))
        furthestAgent = sortedByDist[len(sortedByDist) - 1]
        line(self.x, self.y, furthestAgent.x, furthestAgent.y)

    # draw a line between each agent and its nearest agent
    def drawNearest(self): 
        sortedByDist = agents.sorted(self.distComp.bind(self))
        nearestAgent = sortedByDist[1]
        line(self.x, self.y, nearestAgent.x, nearestAgent.y)
  
    # draw ellipse between agents when they overlap
    def drawOverlap(self): 
        for i in range(len(agents)):
            otherAgent = agents[i]
            if self != otherAgent: 
                tDist = dist(self.x, self.y, otherAgent.x, otherAgent.y)
                if tDist < self.radius + otherAgent.radius: 
                    cx = (self.x + otherAgent.x) / 2
                    cy = (self.y + otherAgent.y) / 2
                    ellipse(cx, cy, tDist)


#max number of agents
max_agents = 32

#array for keeping track of agents
agents = []

# keep track of current mode
AGENT_MODE = 0
POINT_MODE = 1
FURTHEST_MODE = 2
NEAREST_MODE = 3
OVERLAP_MODE = 4

current_mode = AGENT_MODE

def setup(): 
    size(800, 600)
  #set initial state
    current_mode = AGENT_MODE

  #create agents and store them in array 
    for i in range (max_agents):
        print (i)
        agents.append(Agent())
  

def draw(): 
  #update agents
    for i in range (len(agents)):
        print(i)
        agents[i].update()
  

  # depending on the mode:
    if (current_mode == AGENT_MODE):
        background(220, 20, 120)
        
    # draw agents
        noStroke()
        fill(255)
        for i in range (len(agents)):
            print(i)
            agents[i].drawAgent()
    
    else:
        for i in range (len(agents)):
            print(i)
            agents[i].draw()


def mouseClicked():
    #cycle through modes
    current_mode = (current_mode + 1) % 5
    if (current_mode != AGENT_MODE): 
        background(255)



def keyReleased():
    # if drawing:
    if (current_mode != AGENT_MODE):
    # s: save drawing
        if (key == "s" or key == "S"):
            saveCanvas("my-drawing", "jpg")

    # r: reset
        elif (key == "r" or key == "R"):
            background(255)
