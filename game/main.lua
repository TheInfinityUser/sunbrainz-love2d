require("src.atlas_loader")

function love.load()
	Images = LoadAtlasImages("assets/plant/doomshroom")
	Rects = LoadAtlasRects("assets/plant/doomshroom", Images)
end

function love.update(dt)

end

function love.draw()
	local i = 1
	for key, rect in pairs(Rects) do
		love.graphics.draw(Images[rect.atlas], rect.quad, 100 * i, 100)
		i = i + 1
	end
end
