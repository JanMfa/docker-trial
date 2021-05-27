import requests

file_name = "Resources/Dango.jpg" # on the host machine
requests.get('http://0.0.0.0:5000/upload/', json={"file_name": file_name})