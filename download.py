import os
import hashlib
import requests


print('Download new sinetxt...')
response = requests.get('https://www.dmoe.cc/sinetxt.txt')
new_file = response.content

with open('sinetxt.txt', 'rb') as f:
    old_file = f.read()
    f.close()

old_md5 = hashlib.md5(old_file).hexdigest()
new_md5 = hashlib.md5(new_file).hexdigest()

print('New File MD5: ' + new_md5)
print("Old File MD5: " + old_md5)

if old_md5 == new_md5:
    print('The sinetxt has not changed!')
    exit(0)

with open('sinetxt.txt', 'wb') as f:
    f.write(new_file)
    f.close()

with open('sinetxt.txt', 'r', encoding='utf-8') as f:
    for url in f.readlines():
        name = url.strip('\n')
        url = "https://tva1.sinaimg.cn/large/" + name
        if os.path.exists('images/' + name + '.jpg'):
            print("Already exists: " + name + '.jpg')
        else:
            print("Downloading: " + name + '.jpg')
            response = requests.get(url)
            with open('images\\' + name + ".jpg", 'wb') as f:
                f.write(response.content)
                f.close()
            print("Saved: " + name + '.jpg')

print("Done!")
