import json

print("Entity Name: ", end="")
e_name = input()
print("File: ", end="")
path = input()

file = open(path)
json = json.load(file)

text = "require(\"src.loader\")\n\n"
text += "Atlas." + e_name + " = {\n"
text += "\timages = {\n"
i = 1
for atl_key in json["packet"]:
	text += "\t\tlove.graphics.newImage(\"assets/plant/" + e_name + "/" + str(i) + ".png\"),\n"
	i += 1
text = text[:-2] + "\n\t},\n"
text += "\tquads = {\n"
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

		text += "\t\t" + name + " = { image = " + index + ", quad = love.graphics.newQuad(" + x + ", " + y  + ", " + w + ", " + h + ", " + sx + ", " + sy + ") },\n"

text = text[:-2] + "\n\t}\n}"

file.close()

output = open("conversion\\outputs\\" + e_name + ".lua", "w")
output.write(text)
output.close()
