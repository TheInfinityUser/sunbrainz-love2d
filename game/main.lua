require("src.atlases.plant.cold_snapdragon")
require("src.animations.plant.cold_snapdragon")

local frame
local atlas
local anim

local animLayerSetter = {
	color = { 1.0, 1.0, 1.0, 1.0 },
	transform = love.math.newTransform(),

	[78] = {
		color = { 1.0, 1.0, 1.0, 1.0 },
		transform = love.math.newTransform(),

		[1] = {
			color = { 0.0, 0.0, 0.0, 0.0 },
			transform = love.math.newTransform()
		},
		[2] = {
			color = { 0.0, 0.0, 0.0, 0.0 },
			transform = love.math.newTransform()
		}
	}
}

function love.load()
	frame = 1

	atlas = Atlas.cold_snapdragon
	anim = Animations.cold_snapdragon
end

local function drawPart(partName, frameIndex, color, transform, layerSetter)
	local tf
	local col
	local _layerSetter
	for i, layer in ipairs(anim.part[partName][frameIndex]) do
		tf = love.math.newTransform()
		if layerSetter then
			tf:apply(layerSetter.transform)
			col = {
				layerSetter.color[1] * color[1] * layer.color[1],
				layerSetter.color[2] * color[2] * layer.color[2],
				layerSetter.color[3] * color[3] * layer.color[3],
				layerSetter.color[4] * color[4] * layer.color[4]
			}
			_layerSetter = layerSetter[layer.layer]
		else
			col = {
				color[1] * layer.color[1],
				color[2] * layer.color[2],
				color[3] * layer.color[3],
				color[4] * layer.color[4]
			}
			_layerSetter = nil
		end
		tf:apply(transform)
		tf:apply(layer.transform)
		if layer.part then
			drawPart(
				layer.part,
				layer.frame,
				col,
				tf,
				_layerSetter
			)
		else
			tf:apply(anim.base[layer.base].transform)
			tf:scale(anim.scaleFactor)
			love.graphics.setColor(col)
			love.graphics.draw(
				atlas.images[atlas.quads[layer.base].image],
				atlas.quads[layer.base].quad,
				tf
			)
		end
	end
end
local function drawAnimation(animName, frameIndex, color, transform, layerSetter)
	local tf
	local col
	local _layerSetter
	for i, layer in ipairs(anim.animation[animName][frameIndex]) do
		tf = love.math.newTransform()
		if layerSetter then
			tf:apply(layerSetter.transform)
			col = {
				layerSetter.color[1] * color[1] * layer.color[1],
				layerSetter.color[2] * color[2] * layer.color[2],
				layerSetter.color[3] * color[3] * layer.color[3],
				layerSetter.color[4] * color[4] * layer.color[4]
			}
			_layerSetter = layerSetter[layer.layer]
		else
			col = {
				color[1] * layer.color[1],
				color[2] * layer.color[2],
				color[3] * layer.color[3],
				color[4] * layer.color[4]
			}
			_layerSetter = nil
		end
		tf:apply(transform)
		tf:apply(layer.transform)
		if layer.part then
			drawPart(
				layer.part,
				layer.frame,
				col,
				tf,
				_layerSetter
			)
		else
			tf:apply(anim.base[layer.base].transform)
			tf:scale(anim.scaleFactor)
			love.graphics.setColor(col)
			love.graphics.draw(
				atlas.images[atlas.quads[layer.base].image],
				atlas.quads[layer.base].quad,
				tf
			)
		end
	end
end

local updateFps = 0
function love.update(dt)
	frame = math.floor(30 * love.timer.getTime()) % #anim.animation["idle"] + 1
end

function love.keypressed(key)
	--	if key == "d" then
	--		frame = frame % #anim.animation["attack"] + 1
	--	end
	--	if key == "a" then
	--		frame = (frame - 2) % #anim.animation["attack"] + 1
	--	end
end

function love.draw()
	love.graphics.setColor(1.0, 1.0, 1.0, 1.0)
	love.graphics.print(love.timer.getFPS())
	for i = 1, 1000 do
		drawAnimation("idle", frame, { 1.0, 1.0, 1.0, 1.0 },
			love.math.newTransform(), animLayerSetter)
	end
end
