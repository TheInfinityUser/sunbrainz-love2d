function GetTokens(str, delim)
	local tokens = {}
	for token in string.gmatch(str, "([^" .. delim .. "]+)") do
		table.insert(tokens, token)
	end
	return tokens
end
