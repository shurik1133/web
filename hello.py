def application(environ, start_response):
	qs = environ['QUERY_STRING']
	print("qs = ", qs)
	body = list(map(lambda s: bytes(s + '\n', 'ascii'), qs.split('&')))
	print('body = ', body)
	status = '200 OK'
	content_length = sum(map(len, body))
	print('len =', content_length)
	headers = [
		('Content-Type', 'text/plain'),
		('Content-Length', str(content_length))
	]
	start_response(status, headers)
	return body
