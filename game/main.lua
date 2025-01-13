require("src.atlases.plant.cold_snapdragon")
require("src.animations.plant.cold_snapdragon")

local time
local frame
local atlas
local anim

function love.load()
	time = 0
	frame = 1

	atlas = Atlas.cold_snapdragon
	anim = Animations.cold_snapdragon
end

local function drawPart(partName, frameIndex, color, transform)
	for i, layer in ipairs(anim.part[partName][frameIndex]) do
		if layer.part then
			drawPart(
				layer.part,
				layer.frame,
				{
					color[1] * layer.color[1],
					color[2] * layer.color[2],
					color[3] * layer.color[3],
					color[4] * layer.color[4],
				},
				transform
				* layer.transform
			)
		else
			love.graphics.setColor({
				color[1] * layer.color[1],
				color[2] * layer.color[2],
				color[3] * layer.color[3],
				color[4] * layer.color[4],
			})
			love.graphics.draw(
				atlas.images[atlas.quads[layer.base].image],
				atlas.quads[layer.base].quad,
				transform
				* layer.transform
				* anim.base[layer.base].transform
				* love.math.newTransform():scale(anim.scaleFactor)
			)
		end
	end
end
local function drawAnimation(animName, frameIndex, color, transform)
	for i, layer in ipairs(anim.animation[animName][frameIndex]) do
		if layer.part then
			drawPart(
				layer.part,
				layer.frame,
				{
					color[1] * layer.color[1],
					color[2] * layer.color[2],
					color[3] * layer.color[3],
					color[4] * layer.color[4],
				},
				transform
				* layer.transform
			)
		else
			love.graphics.setColor({
				color[1] * layer.color[1],
				color[2] * layer.color[2],
				color[3] * layer.color[3],
				color[4] * layer.color[4],
			})
			love.graphics.draw(
				atlas.images[atlas.quads[layer.base].image],
				atlas.quads[layer.base].quad,
				transform
				* layer.transform
				* anim.base[layer.base].transform
				* love.math.newTransform():scale(anim.scaleFactor)
			)
		end
	end
end

function love.update(dt)
	frame = math.floor(30 * time) % #anim.animation["attack"] + 1
	time = time + dt
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
	drawAnimation("attack", frame, { 1.0, 1.0, 1.0, 1.0 },
		love.math.newTransform())
end
