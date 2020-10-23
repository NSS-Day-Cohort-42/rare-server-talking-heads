from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from categories import get_all_categories, get_single_category, delete_category, create_category

class HandleRequests(BaseHTTPRequestHandler):

	def parse_url(self, path):
		
		url_segments = path.split("/")
		
		query_params = ""
		parameters = []
		request = {}
		request["resource"] = url_segments[1]
		if len(url_segments) > 2:
			params = url_segments[2]
			if "?" in params:
				[request["id"], query_params] = params.split("?")
				parameters = query_params.split("&")

				request["query_params"] = []

				for param in parameters:
					[ key, value ] = param.split("=")
					request["query_params"].append({ key: value })
				
				return request

			

			elif "?" in url_segments[1]:
				[request["resource"], query_params] = url_segments[1].split("?")
				parameters = query_params.split("&")

				request["query_params"] = []

				for param in parameters:
					[ key, value ] = param.split("=")
					request["query_params"].append({ key: value })


				return request
			

			else:
			#parse the params value to integer and if you can then add to response to object under key of 'id'
				
				id = None

				try:
					id = int(params)
				except IndexError:
					pass  # No route parameter exists: /animals
				except ValueError:
					pass  # Request had trailing slash: /animals/
				
				return (request['resource'], id)

	# # No query string parameter
		else:
			id = None

			

			return (request['resource'], id)

    # Here's a class function
	def _set_headers(self, status):
		self.send_response(status)
		self.send_header('Content-type', 'application/json')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

	def do_OPTIONS(self):
		self.send_response(200)
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
		self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
		self.end_headers()


	def do_GET(self):
			# Set the response code to 'Ok'
		self._set_headers(200)
		response = {}
		

		parsed = self.parse_url(self.path)

		if len(parsed) == 2:
			(resource, id) = parsed 

			
			if resource == "categories":
				if id is not None:
					response = f"{get_single_category(id)}"

				else:
					response = f"{get_all_categories()}"
			
		
		# elif len(parsed) == 3:
		# 	(resource, key, value) = parsed

		# 	if key == "email" and resource == "customers":
		# 		response = get_customer_by_email(value)
			
				
			

		self.wfile.write(response.encode())  

    

	# def do_PUT(self):
		
	# 	self._set_headers(204)
	# 	content_len = int(self.headers.get('content-length', 0))
	# 	post_body = self.rfile.read(content_len)
	# 	post_body = json.loads(post_body)

	# 	(resource, id) = self.parse_url(self.path) 	

	# 	# if resource == "animals":
	# 	# 	update_animal(id, post_body)

	# 	# elif resource == "locations":
	# 	#     update_location(id, post_body)
			
	# 	# elif resource == "employees":
	# 	#     update_employee(id, post_body)
			
	# 	# elif resource == "customers":
	# 	#     update_customer(id, post_body)


	# 	self.wfile.write("".encode())

    
	def do_DELETE(self):
		self._set_headers(204)

		(resource, id) = self.parse_url(self.path)

		if resource == "categories":
			delete_category(id)
		
	# 	# elif resource == "locations":
	# 	#     delete_location(id)
		
	# 	# elif resource == "employees":
	# 	#     delete_employee(id)

	# 	# elif resource == "customers":
	# 	#     delete_customer(id)
		
		self.wfile.write("".encode())

	def do_POST(self):
		self._set_headers(201)
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)

		# Convert JSON string to a Python dictionary
		post_body = json.loads(post_body)

		# Parse the URL
		(resource, id) = self.parse_url(self.path)


		new_category = None

        
		if resource == "categories":
			new_category = create_category(post_body)


		self.wfile.write(f"{new_category}".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()