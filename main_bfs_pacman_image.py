# Group 2
# Members:
#  BT19CSE004 Vedant Ghuge
#  BT19CSE082 Yashpal Singh Baghel
#  BT19CSE108 Dushyant Singh
#  BT19ECE036 Vishal Karangale

from tkinter import *
from tkinter.ttk import *
import time
from functionsformain import *
from PIL import ImageTk, Image

defaultMap = [
	[1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1],
	[1, 0, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1],
]

currentMap = defaultMap
widthPath = 50
widthWall = 50
heightPath = 50
heightWall = 50

pacmanStart = (6, 1)
pacmanGoal = (3,3)
class game:
	def __init__(self, master = None):
		self.master = master
		self.smooth = False
		self.doneOnce = False
		self.x = 0
		self.y = 0
		self.xdest = 0
		self.ydest = 0
		self.gotoNode = (0,0)
		self.firstTime = True
		self.width = currentMap[0].__len__() * widthPath + (currentMap[0].__len__() + 1) * widthWall
		self.height = currentMap.__len__() * heightPath + (currentMap.__len__() + 1) * heightWall
		self.canvas = Canvas(master, width=self.width, height=self.height)
		self.canvas.configure(bg='blue')
		self.goalxa = pacmanGoal[1] * (widthPath + widthWall) + widthWall
		self.goalya = pacmanGoal[0] * (heightPath + heightWall) + heightWall
		self.goalxb = (pacmanGoal[1]) * (widthPath + widthWall) + widthWall+ heightWall
		self.goalyb = (pacmanGoal[0]) * (heightPath + heightWall) + widthWall+ heightWall
		

		

		self.goal = self.canvas.create_oval(self.goalxa + 5, self.goalya + 5, self.goalxb - 5, self.goalyb - 5, fill = "Green")
		self.rectanglexa = pacmanStart[1] * (widthPath + widthWall) + widthWall
		self.rectangleya = pacmanStart[0] * (heightPath + heightWall) + heightWall
		self.rectanglexb = (pacmanStart[1]) * (widthPath + widthWall) + widthWall+ heightWall
		self.rectangleyb = (pacmanStart[0]) * (heightPath + heightWall) + widthWall+ heightWall
		

		

		self.imae = Image.open("pacman.png").resize((self.rectanglexb-self.rectanglexa,self.rectangleyb-self.rectangleya))
		

		self.photo = ImageTk.PhotoImage(self.imae)
		

		self.image = self.canvas.create_image(self.rectanglexa, self.rectangleya, image = self.photo, anchor = NW)
		self.rectangle = self.image
		self.canvas.pack()
		self.bfsPath = []
		self.bfsVisited = []
		self.bfsVisited  , self.bfsPath = bfs(currentMap, pacmanStart, pacmanGoal)
		

		

		

		self.dfsPath = self.bfsVisited
		self.dfsVisited = self.bfsVisited
		print(self.bfsPath)
		print(self.bfsVisited)
		

		self.drawWall()
		self.movement()
	
	def drawWall(self):
		for i in range(len(currentMap)):
			for j in range(len(currentMap[i])):
				if currentMap[i][j] == 1:
					xa = j * (widthPath + widthWall) + widthWall
					ya = i * (heightPath + heightWall) + heightWall
					xb = (j) * (widthPath + widthWall) + widthWall+ heightWall
					yb = (i) * (heightPath + heightWall) + widthWall+ heightWall
					self.canvas.create_rectangle(xa,ya,xb,yb, fill="blue", width=widthPath)

	def movement(self):

		self.canvas.move(self.rectangle, self.x, self.y)
		print("Moving")
		print(self.xdest , self.ydest , self.x , self.y )
		if self.xdest == 0 and self.ydest == 0:
			self.x = 0
			self.y = 0
			print(self.x, self.y)
			

			if self.dfsPath.__len__() != 0:
				lastNode = self.gotoNode
				self.gotoNode = self.dfsPath.pop(0)
				if self.bfsPath[2:] == self.dfsPath:
					self.smooth = True
				print("GotoNode: " , self.gotoNode)
				print("GotoNode: " , self.gotoNode)
				print("LastNode: " , lastNode)
				

				print((self.gotoNode[1] - lastNode[1]))
				print((self.gotoNode[0] - lastNode[0]))
				self.xdest = (self.gotoNode[1] - lastNode[1]) * (widthPath + widthWall)
				print(self.xdest)
				if self.xdest != 0 and self.firstTime:
					self.xdest = self.xdest + widthWall - self.rectanglexa
					print(self.xdest)
				

				self.ydest = (self.gotoNode[0] - lastNode[0]) * (heightPath + heightWall)
				if self.ydest != 0 and self.firstTime:
					self.ydest = self.ydest + heightWall - self.rectangleya
				self.firstTime = False
				

				print( "Dest Coords" , self.xdest , self.ydest)
				

				


			if self.dfsPath.__len__() == 0 and not self.doneOnce:
				self.dfsPath = self.bfsPath.copy()
				self.doneOnce = True
				print("Goal Reached")
				


		if self.xdest != 0:
			self.x = self.xdest/(abs(self.xdest)) * 5
			if not self.smooth: self.x = self.xdest
			self.xdest = self.xdest - self.x
		if self.ydest != 0:
			self.y = self.ydest/(abs(self.ydest)) * 5
			if not self.smooth: self.y = self.ydest
			self.ydest = self.ydest - self.y 
		if self.smooth: self.canvas.after(50, self.movement)
		else: self.canvas.after(500, self.movement)
	
	def left(self, event):
		self.xdest = self.xdest -(widthPath + widthWall)
		self.ydest = 0
	
	def right(self, event):
		self.xdest =self.xdest +  widthPath + widthWall
		self.ydest = 0

	def up(self, event):
		self.xdest = 0
		self.ydest =self.ydest -(widthPath + widthWall)
	
	def down(self, event):
		self.xdest = 0
		self.ydest = self.ydest + widthPath + widthWall

if __name__ == "__main__":
	map = defaultMap
	print("Playing Game using BFS")
	print("Create a new map? (y/n)")
	if input() == "y":
		currentMap = createNewMap()
		print("Created new map")
		

	else:
		print("Using default map")
	print("Map is : ")
	printMap(currentMap, (-1, -1), (-1, -1))

	print("Change start and goal? (y/n)")
	if input() == "y":
		while True:
			print("Enter start coordinates: ")
			pacmanStart = (int(input("Start Row : ")), int(input("Start Col : ")))
			print("Enter goal coordinates: ")
			pacmanGoal = (int(input("Goal Row : ")), int(input("Goal Col : ")))
			if map[pacmanStart[0]][pacmanStart[1]] == 1 or map[pacmanGoal[0]][pacmanGoal[1]] == 1:
				print("Invalid coordinates")
			else :
				break
	else: 
		start = pacmanStart
		goal = pacmanGoal

	print("Starting with Map: ")
	printMap(map, pacmanStart, pacmanGoal)
	master = Tk()
	gfg = game(master)
	mainloop()
