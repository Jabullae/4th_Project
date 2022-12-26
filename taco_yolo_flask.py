import requests
import os
import json

def send_data(url):
    path_dir = 'C:/dev/MLDL/mini/upload'
    file_list = os.listdir(path_dir)
    for name in file_list:
        files = {
       
            'file':open('C:/dev/MLDL/mini/upload' + name, 'rb')
        }
        res = requests.post(url,files=files)
        #name = res['name']
        res_json = res.json()
        if res_json['answer'] == "Detect":
            os.system("mv C:/dev/MLDL/mini/upload/" + name + " C:/dev/MLDL/mini/web" )
        else:
            os.system("rm -f C:/dev/MLDL/mini/upload/"+ name)
    return "Done"

url = "http://localhost/predict"
print(send_data(url))