from .api import addBlog
if len(data) is 0:
	conn.commit()
	return {'StatusCode':'200','Message': 'User creation success'}
else:
	return {'StatusCode':'1000','Message': str(data[0])}

	