import http.server
import json
import datetime
import time

# Define the handler for our server
class HTTPReqHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Handle the endpoint for the current time
        if self.path == "/":
            # Fetch the current time in Toronto (which is in Eastern Time Zone)
            toronto_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-4)))
            response = {
                'current_time': toronto_time.strftime('%Y-%m-%d %H:%M:%S')
            }
            # Send the HTTP status
            self.send_response(200)
            # Set the content type to JSON
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Send the JSON response
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            # For any other endpoints, return a 404
            self.send_response(404)
            self.end_headers()

# Run the server on port $PORT
PORT = 80
startMSG = "Server running on http://localhost:"
webMSG = startMSG+str(PORT)

if __name__ == "__main__":
    httpd = http.server.HTTPServer(('localhost', PORT), HTTPReqHandler)
    print(webMSG)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("\nServer stopped!")
