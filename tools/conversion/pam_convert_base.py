import json

e_name = "cold_snapdragon"
path = "d:\MyFiles\PVZ\cold_snapdragon.pam.json"

file = open(path)
js = json.load(file)

text = "Animations." + e_name + " = {}\n"
text += "Animations." + e_name + ".size = { x = " + str(js["size"]["width"]) + ", y = " + str(js["size"]["height"]) + "}\n"
text += "Animations." + e_name + ".scaleFactor = 0.78125\n"
text += "Animations." + e_name + ".base = {\n"
for img in js["image"]:
	text += "\t" + img["path"] + " = {\n\t\ttransform = love.math.newTransform():setMatrix(\n"
	text += "\t\t\t" + str(img["transform"][0]) + ", " + str(img["transform"][2]) + ", 0.0, " + str(img["transform"][4]) + ",\n"
	text += "\t\t\t" + str(img["transform"][1]) + ", " + str(img["transform"][3]) + ", 0.0, " + str(img["transform"][5]) + ",\n"
	text += "\t\t\t0.0, 0.0, 1.0, 0.0,\n"
	text += "\t\t\t0.0, 0.0, 0.0, 1.0\n\t\t)\n"
	text += "\t},\n"
text = text[:-2] + "\n}\n"
text += "Animations." + e_name + ".part = {}\n"
text += "Animations." + e_name + ".animation = {}"

file.close()

output = open("conversion\\outputs\\base.lua", "w")
output.write(text)
output.close()
