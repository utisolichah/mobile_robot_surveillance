import SocketServer
import time

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        while 1:
            file = open("testfile.text", "r")
            cmd = file.read()
            file.close()
            open('file.txt', 'w').close()
            self.request.sendall(cmd)
            time.sleep(1)

        # self.request is the TCP socket connected to the client
        #self.data = self.request.recv(1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        #print self.data
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
#raspi ip 192.168.43.199
if __name__ == "__main__":

    HOST, PORT = "0.0.0.0", 9996

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer(HOST, PORT)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
