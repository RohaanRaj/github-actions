import socket
import os

print(os.name)
print(socket.gethostname())

path = "/config/message.txt"

with open (path, "r") as file:
    content = file.read()
    print("\nThese are the contents inside config/\n" +content)

#print("\n Printing secret text from github secrets " + ${{secrets.SECRET_MESSAGE}})
