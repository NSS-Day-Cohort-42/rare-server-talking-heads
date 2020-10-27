from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from categories import get_all_categories, get_single_category, delete_category, create_category, update_category
from posts import get_all_posts, get_single_post, get_posts_by_category, create_new_post, delete_post, get_posts_by_user
from users import create_user, get_user_by_email
from comments import get_comments_by_post, create_comment, delete_comment
from tags import get_all_tags, create_tag

class HandleRequests(BaseHTTPRequestHandler):

	def parse_url(self, path):
		path_params = path.split("/")
		resource = path_params[1]

		# Check if there is a query string parameter
		if "?" in resource:
			# GIVEN: /customers?email=jenna@solis.com

			param = resource.split("?")[1]  # email=jenna@solis.com
			resource = resource.split("?")[0]  # 'customers'
			pair = param.split("=")  # [ 'email', 'jenna@solis.com' ] 
			key = pair[0]  # 'email' 
			value = pair[1]  # 'jenna@solis.com'


			return ( resource, key, value )

		# No query string parameter
		else:
			id = None

			try:
				id = int(path_params[2])
			except IndexError:
				pass  # No route parameter exists: /animals
			except ValueError:
				pass  # Request had trailing slash: /animals/

			return (resource, id)

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
			
			if resource == "posts":
				if id is not None:
					response = f"{get_single_post(id)}"
				else:
					response = f"{get_all_posts()}"

			if resource == "tags":
				response = f"{get_all_tags()}"
		
		elif len(parsed) == 3:
			(resource, key, value) = parsed

			if key == "category_id" and resource == "posts":
				response = get_posts_by_category(value)

			if key == "user_id" and resource == "posts":
				response = get_posts_by_user(value)
			
			if key == "post_id" and resource == "comments":
				response = get_comments_by_post(value)
			

			if key == "email" and resource == "users":
				response = get_user_by_email(value)
			

		self.wfile.write(response.encode())  

	def do_POST(self):
		self._set_headers(201)
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)

		# Convert JSON string to a Python dictionary
		post_body = json.loads(post_body)

		# Parse the URL
		(resource, id) = self.parse_url(self.path)

		# Initialize new resource
		new_resource = None

		if resource == "register":
			new_resource = create_user(post_body)

		if resource == "categories":
			new_resource = create_category(post_body)
		
		if resource == "comments":
			new_resource = create_comment(post_body)
		

		if resource == "posts":
			new_resource = create_new_post(post_body)

		if resource == "tags":
			new_resource = create_tag(post_body)

		self.wfile.write(f"{new_resource}".encode())


	def do_PUT(self):
		
		self._set_headers(204)
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)
		post_body = json.loads(post_body)

		(resource, id) = self.parse_url(self.path) 	

		if resource == "categories":
			success = update_category(id, post_body)
			if success:
				self._set_headers(204)
			else:
				self._set_headers(404)

		self.wfile.write("".encode())
    
	def do_DELETE(self):
		self._set_headers(204)

		(resource, id) = self.parse_url(self.path)

		if resource == "categories":
			delete_category(id)
		
		if resource == "comments":
			delete_comment(id)

		if resource == "posts":
			delete_post(id)

		self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()