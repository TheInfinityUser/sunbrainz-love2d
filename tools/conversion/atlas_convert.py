import json

print("Entity Name: ", end="")
e_name = input()
print("File: ", end="")
path = input()

file = open(path)
json = json.load(file)

text = "require(\"src.loader\")\n\nAtlasTextures." + e_name + " = {\n"
for atl_key in json["packet"]:
	sx = str(json["packet"][atl_key]["dimension"]["width"])
	sy = str(json["packet"][atl_key]["dimension"]["height"])
  
	for data_key in json["packet"][atl_key]["data"]:
		name = json["packet"][atl_key]["data"][data_key]["path"].split("/")[-1]
		index = str(int(atl_key[-1:]) + 1)
		x = str(json["packet"][atl_key]["data"][data_key]["default"]["ax"])
		y = str(json["packet"][atl_key]["data"][data_key]["default"]["ay"])
		w = str(json["packet"][atl_key]["data"][data_key]["default"]["aw"])
		h = str(json["packet"][atl_key]["data"][data_key]["default"]["ah"])

		text += "\t" + name + " = { i = " + index + ", q = love.graphics.newQuad(" + x + ", " + y  + ", " + w + ", " + h + ", " + sx + ", " + sy + ") },\n"

text = text[:-2] + "\n}"

file.close()

output = open("conversion\\outputs\\" + e_name + ".lua", "w")
output.write(text)
output.close()
