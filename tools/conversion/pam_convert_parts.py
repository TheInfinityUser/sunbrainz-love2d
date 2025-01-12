import json

e_name = "doomshroom"
path = "d:\MyFiles\PVZ\doomshroom.pam.json"

file = open(path)
js = json.load(file)

def transform_to_str(transform, line_start):
	t = "love.math.newTransform()\n"
	if len(transform) == 6:
		if not (transform[1] == 0.0 and transform[2] == 0.0):
			t += line_start + ":shear(" + str(transform[1]) + ", " + str(transform[2]) + ")\n"
		if not (transform[0] == 1.0 and transform[3] == 1.0):
			if transform[0] == transform[3]:
				t += line_start + ":scale(" + str(transform[0]) + ")\n"
			else:
				t += line_start + ":scale(" + str(transform[0]) + ", " + str(transform[3]) + ")\n"
		if not (transform[4] == 0.0 and transform[5] == 0.0):
			t += line_start + ":translate(" + str(transform[4]) + ", " + str(transform[5]) + ")\n"
	if len(transform) == 2:
		if not (transform[0] == 0.0 and transform[1] == 0.0):
			t += line_start + ":translate(" + str(transform[0]) + ", " + str(transform[1]) + ")\n"
	if len(transform) == 3:
		if not (transform[2] == 0.0):
			t += line_start + ":rotate(" + str(transform[2]) + ")\n"
		if not (transform[0] == 0.0 and transform[1] == 0.0):
			t += line_start + ":translate(" + str(transform[0]) + ", " + str(transform[1]) + ")\n"
	return t

def append_to_text(st):
	global text
	text += "\t{\n"
	for l in st:
		if not st[l]:
			continue
		text += "\t\t[" + str(l) + "] = {\n"
		if "base" in st[l]:
			text += "\t\t\tbase = \"" + str(st[l]["base"]) + "\",\n"
		if "part" in st[l]:
			text += "\t\t\tpart = \"" + str(st[l]["part"]) + "\",\n"
			text += "\t\t\tframe = " + str(st[l]["frame"]) + ",\n"
		text += "\t\t\tcolor = { " + \
			str(st[l]["color"][0]) + ", " + \
			str(st[l]["color"][1]) + ", " + \
			str(st[l]["color"][2]) + ", " + \
			str(st[l]["color"][3]) + " },\n"
		text += "\t\t\ttransform = " + transform_to_str(st[l]["transform"], "\t\t\t\t")
		text += "\t\t},\n"
	text = text[:-2] + "\n\t},\n"

for sprite in js["sprite"]:

	text = "require(\"src.loader\")\n\nAnimations." + e_name + ".part." + sprite["name"].replace(" ", "_") + " = {\n"

	state = {}

	for frame in sprite["frame"]:
		for layer in frame["append"]:
			if layer["index"] + 1 not in state:
				state[layer["index"] + 1] = {}

	for frame in sprite["frame"]:
		for layer in frame["append"]:
			if layer["sprite"]:
				state[layer["index"] + 1]["part"] = js["sprite"][layer["resource"]]["name"]
				state[layer["index"] + 1]["frame"] = 0
				state[layer["index"] + 1]["// length"] = len(js["sprite"][layer["resource"]]["frame"])
			else:
				state[layer["index"] + 1]["base"] = js["image"][layer["resource"]]["path"]
			state[layer["index"] + 1]["color"] = [ 1.0, 1.0, 1.0, 1.0 ]
		for layer in frame["change"]:
			state[layer["index"] + 1]["transform"] = layer["transform"]
			if layer["color"]:
				state[layer["index"] + 1]["color"] = layer["color"]
		for layer in frame["remove"]:
			del state[layer + 1]
		append_to_text(state)
		for l in state:
			if "frame" in state[l]:
				state[l]["frame"] = (state[l]["frame"] + 1) % state[l]["// length"]

	text = text[:-2] + "\n}"

	output = open("conversion\\outputs\\" + sprite["name"].replace(" ", "_") + ".lua", "w")
	output.write(text)
	output.close()
