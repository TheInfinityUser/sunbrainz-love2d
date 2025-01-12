require("src.loader")

function love.load()
	require("src.atlas.plant.doomshroom")
	require("src.image.plant.doomshroom")

	print(tostring(AtlasTextures.doomshroom))
end

function love.update(dt)

end

function love.draw()
	love.graphics.draw(
		Images.doomshroom[AtlasTextures.doomshroom.doomshroom_138x119.i],
		AtlasTextures.doomshroom.doomshroom_138x119.q,
		100, 100
	)
end
