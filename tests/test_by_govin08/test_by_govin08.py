import sys
# I've illustrated all the path in my system to be more precise.
sys.path = ['C:\\github\\sumo\\tools',
            'C:\\Users\\유아이네트웍스\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip',
            'C:\\Users\\유아이네트웍스\\AppData\\Local\\Programs\\Python\\Python38\\DLLs',
            'C:\\Users\\유아이네트웍스\\AppData\\Local\\Programs\\Python\\Python38\\lib',
            'C:\\Users\\유아이네트웍스\\AppData\\Local\\Programs\\Python\\Python38',
            'c:\\Github\\test_sumo\\.venv\\lib\\site-packages']
import sumolib

# (1) I've created an sumolib.net.node.Node, where the name is specified
node1313 = sumolib.net.node.Node(id="1313", type="traffic_light", coord=(1816.19, 1836.81), incLanes=["903_0", "903_1"], name="N")

# The name of node1313 is printed well.
print(node1313.getName())


# (2) "SN.net.xml" is my own network file, which has nodes including 26588 and 5790
# I didn't specify any name of the node with id 26588
# I've specified the name of the node with id 5790 as N
net = sumolib.net.readNet("SN.net.xml") # my network file
nodes = net.getNodes()
n26588 = [node for node in nodes if node.getID()=='26588'][0]
n5790 = [node for node in nodes if node.getID()=='5790'][0]

print(n5790.getName()) # it prints None, as expected
print(n26588.getName()) # it also prints None, although it should be 'N'
