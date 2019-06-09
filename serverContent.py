from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            # Check the file extension required and
            # set the right mime type

            sendReply = False
            if self.path.endswith(".mp4"):
                mimetype = 'video/mpeg'
                sendReply = True
            if self.path.endswith(".mp3"):
                mimetype = 'audio/mpeg'
                sendReply = True

            if sendReply == True:
                # Open the static file requested and send it
                f = open(curdir + sep + self.path, errors='ignore')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port', PORT_NUMBER)

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()