import json
import math

e_name = "cold_snapdragon"
path = "d:\MyFiles\PVZ\cold_snapdragon.pam.json"

file = open(path)
js = json.load(file)

def transform_to_str(transform, line_start):
	text = "love.math.newTransform():setMatrix(\n"
	if len(transform) == 6:
		text += line_start + "\t" + str(transform[0]) + ", " + str(transform[2]) + ", 0.0, " + str(transform[4]) + ",\n"
		text += line_start + "\t" + str(transform[1]) + ", " + str(transform[3]) + ", 0.0, " + str(transform[5]) + ",\n"
		text += line_start + "\t0.0, 0.0, 1.0, 0.0,\n"
		text += line_start + "\t0.0, 0.0, 0.0, 1.0\n"
	if len(transform) == 2:
		text += line_start + "\t1.0, 0.0, 0.0, " + str(transform[0]) + ",\n"
		text += line_start + "\t0.0, 1.0, 0.0, " + str(transform[1]) + ",\n"
		text += line_start + "\t0.0, 0.0, 1.0, 0.0,\n"
		text += line_start + "\t0.0, 0.0, 0.0, 1.0\n"
	if len(transform) == 3:
		text += line_start + "\t" + str(math.cos(transform[0])) + ", " + str(-math.sin(transform[0])) + ", 0.0, " + str(transform[1]) + ",\n"
		text += line_start + "\t" + str(math.sin(transform[0])) + ", " + str(math.cos(transform[0])) + ", 0.0, " + str(transform[2]) + ",\n"
		text += line_start + "\t0.0, 0.0, 1.0, 0.0,\n"
		text += line_start + "\t0.0, 0.0, 0.0, 1.0\n"
	text += line_start + ")\n"
	return text

def append_state_to_text(text, st):
	if len(st) == 0:
		text += "\t{},\n"
		return text
	text += "\t{\n"
	for l in st:
		text += "\t\t{\n"
		text += "\t\t\tlayer = " + str(l["layer"]) + ",\n"
		if "base" in l:
			text += "\t\t\tbase = \"" + str(l["base"]) + "\",\n"
		elif "part" in l:
			text += "\t\t\tpart = \"" + str(l["part"]) + "\",\n"
			text += "\t\t\tframe = " + str(l["frame"]) + ",\n"
		text += "\t\t\tcolor = { " + \
			str(l["color"][0]) + ", " + \
			str(l["color"][1]) + ", " + \
			str(l["color"][2]) + ", " + \
			str(l["color"][3]) + " },\n"
		text += "\t\t\ttransform = " + transform_to_str(l["transform"], "\t\t\t")
		text += "\t\t},\n"
	text = text[:-2] + "\n\t},\n"
	return text

def state_dict_to_sorted_list(state):
	_state = []
	for item in sorted(state.items()):
		if not ("base" in item[1] or "part" in item[1]):
			continue
		_state.append(item[1])
		_state[-1]["layer"] = item[0]
	return _state

def convert_sprite(sprite, section, name, _type):
	text = "Animations." + e_name + "." + _type + "[\"" + name + "\"] = {\n"

	state = {}
	
	for f in range(0, section[1]):
		frame = sprite["frame"][f]
		for layer in frame["append"]:
			if layer["index"] + 1 not in state:
				state[layer["index"] + 1] = {}

	for f in range(0, section[1]):
		frame = sprite["frame"][f]
		for layer in frame["append"]:
			if layer["sprite"]:
				state[layer["index"] + 1]["part"] = js["sprite"][layer["resource"]]["name"]
				state[layer["index"] + 1]["frame"] = 1
				state[layer["index"] + 1]["// length"] = len(js["sprite"][layer["resource"]]["frame"])
			else:
				state[layer["index"] + 1]["base"] = js["image"][layer["resource"]]["path"]
			state[layer["index"] + 1]["color"] = [ 1.0, 1.0, 1.0, 1.0 ]
		for layer in frame["change"]:
			state[layer["index"] + 1]["transform"] = layer["transform"]
			if layer["color"]:
				state[layer["index"] + 1]["color"] = layer["color"]
		for layer in frame["remove"]:
			state[layer + 1] = {}
		if f >= section[0]:
			text = append_state_to_text(text, state_dict_to_sorted_list(state))
		for l in state:
			if "frame" in state[l]:
				state[l]["frame"] = state[l]["frame"] % state[l]["// length"] + 1

	text = text[:-2] + "\n}"

	output = open("conversion\\outputs\\" + name + ".lua", "w")
	output.write(text)
	output.close()

	print("require(\"src.animations.plant." + e_name + "." + _type + "s." + name + "\")")

for sprite in js["sprite"]:
	convert_sprite(
		sprite,
		[sprite["work_area"]["start"], sprite["work_area"]["start"] + sprite["work_area"]["duration"]],
		sprite["name"],
		"part"
	)

animations = []
for f in range(js["main_sprite"]["work_area"]["start"], js["main_sprite"]["work_area"]["start"] + js["main_sprite"]["work_area"]["duration"]):
	if js["main_sprite"]["frame"][f]["label"] != "":
		animations.append({ "name": js["main_sprite"]["frame"][f]["label"] })
		animations[-1]["start"] = f
	if js["main_sprite"]["frame"][f]["stop"]:
		animations[-1]["end"] = f + 1

for anim in animations:
	convert_sprite(
		js["main_sprite"],
		[anim["start"], anim["end"]],
		anim["name"],
		"animation"
	)
