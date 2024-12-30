require("src.util")

function LoadAtlasRects(location, images)
	local lines = GetTokens(love.filesystem.read("assets/atlas/" .. location .. ".atl"), "\n")
	local rects = {}

	for i = 2, #lines do
		local items = GetTokens(lines[i], " ")

		rects[items[1]] = {}
		rects[items[1]].atlas = tonumber(items[2])
		rects[items[1]].quad = love.graphics.newQuad(
			items[3], items[4],
			items[5], items[6],
			images[tonumber(items[2])]
		)
	end

	return rects
end

function LoadAtlasImages(location)
	local n = tonumber(string.sub(love.filesystem.read("assets/atlas/" .. location .. ".atl"), 1, 1))
	local images = {}

	for i = 1, n do
		table.insert(images, love.graphics.newImage("assets/texture/" .. location .. "/" .. i .. ".png"))
	end

	return images
end
