from http.server import BaseHTTPRequestHandler, HTTPServer
import json

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
				else:
					if "?" in url_segments[1]:
						[request["resource"], query_params] = url_segments[1].split("?")
						parameters = query_params.split("&")
						request["query_params"] = []
				for param in parameters:
					[ key, value ] = param.split("=")
					request["query_params"].append({ key: value })
				return request

	# No query string parameter
		else:
			id = None

			try:
				id = int(query_params[2])
			except IndexError:
				pass  # No route parameter exists: /animals
			except ValueError:
				pass  # Request had trailing slash: /animals/

			return (request['resource'], request['id'])

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
			# Your new console.log() that outputs to the terminal
			print(self.path)

			parsed = self.parse_url(self.path)

			# if len(parsed) == 2:
			# 	(resource, id) = parsed 
			
				# if resource == "animals":
				# 	if id is not None:
				# 		response = f"{}"

				# 	else:
				# 		response = f"{}"
				
			
			# elif len(parsed) == 3:
			# 	(resource, key, value) = parsed

				# if key == "email" and resource == "customers":
				# 	response = get_customer_by_email(value)
				
				
			

			# self.wfile.write(response.encode())  

    

	def do_PUT(self):
		
		self._set_headers(204)
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)
		post_body = json.loads(post_body)

		(resource, id) = self.parse_url(self.path)

		# if resource == "animals":
		# 	update_animal(id, post_body)

		# elif resource == "locations":
		#     update_location(id, post_body)
			
		# elif resource == "employees":
		#     update_employee(id, post_body)
			
		# elif resource == "customers":
		#     update_customer(id, post_body)


		self.wfile.write("".encode())

    
	def do_DELETE(self):
		self._set_headers(204)

		(resource, id) = self.parse_url(self.path)

		# if resource == "animals":
		# 	delete_animal(id)
		
		# elif resource == "locations":
		#     delete_location(id)
		
		# elif resource == "employees":
		#     delete_employee(id)

		# elif resource == "customers":
		#     delete_customer(id)
		
		self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()