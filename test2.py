from PIL import Image
import requests
import webbrowser
from io import BytesIO
import subprocess

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Jim_Carrey_2008.jpg/220px-Jim_Carrey_2008.jpg"
response = requests.get(url)
print(response)
img = Image.open(requests.get(url, stream=True).raw)
p = subprocess.Popen(["display", img])
raw_input("Give a name for image:")
p.kill()

#img.show()

# def get_image_details():
#     img.show()




