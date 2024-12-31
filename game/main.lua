require("src.loader")

function love.load()
	require("src.atlas.plant.doomshroom")
	require("src.image.plant.doomshroom")

	print(tostring(LoadedRects.doomshroom))
end

function love.update(dt)

end

function love.draw()
	love.graphics.draw(
		LoadedImages.doomshroom[LoadedRects.doomshroom.doomshroom_138x119.i],
		LoadedRects.doomshroom.doomshroom_138x119.q,
		100, 100
	)
end
