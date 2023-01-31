import requests


with open('sinetxt.txt', 'r', encoding='utf-8') as f:
    for url in f.readlines():
        name = url.strip('\n')
        url = "https://tva1.sinaimg.cn/large/" + name
        print("Downloading: " + name)
        response = requests.get(url)
        type = response.headers.get("Content-Type")
        type = type.replace("image/", "")
        if type == "jpeg":
            type = "jpg"
        with open('images\\' + name + "." + type, 'wb') as f:
            f.write(response.content)
            f.close()
        print("Saved: " + name + "." + type)
