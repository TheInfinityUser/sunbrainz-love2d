Animations.peashooter.part._peashooter_head = {
	{
		{
			layer = 1,
			part = "peashooter_head_base",
			frame = 1,
			color = { 1.0, 1.0, 1.0, 1.0 },
			transform = love.math.newTransform():setMatrix(
				1.0, 0.0, 0.0, 0.0,
				0.0, 1.0, 0.0, 0.0,
				0.0, 0.0, 1.0, 0.0,
				0.0, 0.0, 0.0, 1.0
			)
		},
		{
			layer = 2,
			part = "_custom",
			frame = 1,
			color = { 1.0, 1.0, 1.0, 1.0 },
			transform = love.math.newTransform():setMatrix(
				0.9915618943329317, 0.1296341378915593, 0.0, 5.0,
				-0.1296341378915593, 0.9915618943329317, 0.0, -20.299999237060547,
				0.0, 0.0, 1.0, 0.0,
				0.0, 0.0, 0.0, 1.0
			)
		}
	}
}