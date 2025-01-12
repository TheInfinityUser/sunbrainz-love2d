require("src.image.plant.peashooter")
require("src.atlas.plant.peashooter")
require("src.animation.plant.peashooter.init")

local time
local frame

function love.load()
	time = 0
	frame = 1
end

local function drawPart(anim, partName, frameIndex, color, transform)
	for i, layer in ipairs(anim.part[partName][frameIndex]) do
		if layer.part then
			drawPart(
				anim,
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
				Images.peashooter[AtlasTextures.peashooter[layer.base].i],
				AtlasTextures.peashooter[layer.base].q,
				transform
				* layer.transform
				* Animations.peashooter.base[layer.base].transform
				* love.math.newTransform():scale(Animations.peashooter.scaleFactor)
			)
		end
	end
end

local function drawAnimation(anim, animName, frameIndex, color, transform)
	for i, layer in ipairs(anim.animation[animName][frameIndex]) do
		if layer.part then
			drawPart(
				anim,
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
				Images.peashooter[AtlasTextures.peashooter[layer.base].i],
				AtlasTextures.peashooter[layer.base].q,
				transform
				* layer.transform
				* Animations.peashooter.base[layer.base].transform
				* love.math.newTransform():scale(Animations.peashooter.scaleFactor)
			)
		end
	end
end

function love.update(dt)
	frame = math.floor(30 * time) % 144 + 1
	time = time + dt
end

function love.draw()
	drawAnimation(Animations.peashooter, "test", frame, { 1.0, 1.0, 1.0, 1.0 },
		love.math.newTransform():translate(390 / 2, 390 / 2))
end
