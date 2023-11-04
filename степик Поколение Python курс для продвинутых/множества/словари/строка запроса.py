def build_query_string(params):
	out = []
	for a, b in params.items():
		out.append(str(a) + '=' + str(b))
	return '&'.join(sorted(out))




