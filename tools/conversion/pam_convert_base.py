import json

print("Entity Name: ", end="")
e_name = input()
print("File: ", end="")
path = input()

file = open(path)
json = json.load(file)

text = "require(\"src.loader\")\n\nAnimations." + e_name + ".scaleFactor = 0.78125\nAnimations." + e_name + ".base = {\n"
for img in json["image"]:
	text += "\t" + img["path"] + " = {\n\t\ttransform = love.math.newTransform()\n"
	if not (img["transform"][1] == 0.0 and img["transform"][2] == 0.0):
		text += "\t\t\t:shear(" + str(img["transform"][1]) + ", " + str(img["transform"][2]) + ")\n"
	if not (img["transform"][0] == 1.0 and img["transform"][3] == 1.0):
		if img["transform"][0] == img["transform"][3]:
			text += "\t\t\t:scale(" + str(img["transform"][0]) + ")\n"
		else:
			text += "\t\t\t:scale(" + str(img["transform"][0]) + ", " + str(img["transform"][3]) + ")\n"
	if not (img["transform"][4] == 0.0 and img["transform"][5] == 0.0):
		text += "\t\t\t:translate(" + str(img["transform"][4]) + ", " + str(img["transform"][5]) + ")\n"
	text += "\t},\n"
text = text[:-2] + "\n}"

file.close()

output = open("conversion\\outputs\\base.lua", "w")
output.write(text)
output.close()
