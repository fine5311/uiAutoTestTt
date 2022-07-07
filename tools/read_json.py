import json
import os

from config import BASE_PATH


def get_json(filename):
    file_path = BASE_PATH + os.sep + 'data' + os.sep + filename
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def get_mp_login(filename):
    arr1=[]
    json = get_json(filename)
    for data in json:
    #     # print(data)
         arr2 = []
         arr2.append(data['username'])
         arr2.append(data['code'])
         arr2.append(data['expect'])
         arr1.append(arr2)


    return arr1

def get_mp_publish(filename):
    arr1=[]
    json = get_json(filename)
    for data in json:
    #     # print(data)
         arr2 = []
         arr2.append(data['title'])
         arr2.append(data['content'])
         arr2.append(data['channel'])
         arr1.append(arr2)


    return arr1

def get_app_login(filename):
    arr1=[]
    json = get_json(filename)
    for data in json:
    #     # print(data)
         arr2 = []
         arr2.append(data['username'])
         arr2.append(data['code'])

         arr1.append(arr2)


    return arr1

if __name__ == '__main__':
    data1 = get_mp_login("mp_login.json")
    print(data1)
