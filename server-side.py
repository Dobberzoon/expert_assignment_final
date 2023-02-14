import socket
import sys
import requests
import json

request_url = "https://www.mediawiki.org/w/api.php?action=query&format=json&prop=revisions&list=allrevisions&meta=siteinfo&continue=&titles=Main%20Page&formatversion=2&rvprop=user%7Ccomment&arvlimit=50&arvdir=newer"

response = requests.get(request_url)
response_json = response.json() # This method is convenient when the API returns JSON
json_formatted_str = json.dumps(response_json, indent=2)
print(json_formatted_str)


def server():
    host = socket.gethostname()
    port = 7000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    connection, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        connection.send(data.encode())
    connection.close()


def wikipedia_api_GET_request():
    pass

# if __name__ == "__main__":
#     server()
