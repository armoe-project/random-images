import os
import hashlib
import requests

def convert_image_to_webp(image_file_name):
    """
    将给定的.jpg图片转换为.webp格式，并保存在固定的目录中。

    参数:
    image_file_name (str): 原始图片的文件名（包括路径）
    """

    webp_dir = 'images/webp'  # 固定的webp图片的目录

    # 创建存储webp图片的文件夹，如果不存在的话
    if not os.path.exists(webp_dir):
        os.makedirs(webp_dir)

    # 检查文件是否是.jpg格式
    if image_file_name.endswith('.jpg'):
        img = Image.open(image_file_name)
        # 将图片转换为RGB模式，以确保它可以被转换为webp格式
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # 保存图片为webp格式
        img.save(os.path.join(webp_dir, os.path.splitext(os.path.basename(image_file_name))[0] + '.webp'), 'webp')

        print(f"Image {image_file_name} has been converted to webp format!")

# 打印开始下载新的sinetxt.txt文件的消息
print('Download new sinetxt...')

# 从指定URL下载新的sinetxt.txt文件
response = requests.get('https://www.dmoe.cc/sinetxt.txt', verify=False)
new_file = response.content

# 读取本地的旧sinetxt.txt文件
with open('sinetxt.txt', 'rb') as f:
    old_file = f.read()
    f.close()

# 计算新旧文件的MD5 hash值
old_md5 = hashlib.md5(old_file).hexdigest()
new_md5 = hashlib.md5(new_file).hexdigest()

# 打印新旧文件的MD5 hash值
print('New File MD5: ' + new_md5)
print("Old File MD5: " + old_md5)

# 如果新旧文件的MD5 hash值相同，打印消息并退出程序
if old_md5 == new_md5:
    print('The sinetxt has not changed!')
    exit(0)

# 如果新旧文件的MD5 hash值不同，将新的sinetxt.txt文件写入本地
with open('sinetxt.txt', 'wb') as f:
    f.write(new_file)
    f.close()

# 打开新的sinetxt.txt文件，并读取其中的每一行
with open('sinetxt.txt', 'r', encoding='utf-8') as f:
    for url in f.readlines():
        name = url.strip('\n')  # 去除行尾的换行符，得到图片的名字
        url = "https://tva1.sinaimg.cn/large/" + name  # 构造图片的URL

        # 如果本地不存在同名的图片文件，下载并保存图片
        if os.path.exists('images/' + name + '.jpg') == False:
            print("Downloading: " + name + '.jpg')  # 打印正在下载的图片的消息
            response = requests.get(url)  # 下载图片
            with open('images/' + name + ".jpg", 'wb') as f:
                f.write(response.content)  # 将图片保存到本地
                f.close()
            print("Saved: " + name + '.jpg')  # 打印图片已保存的消息
            # 调用函数，将指定的图片转换为webp格式，并保存在固定的目录中
            convert_image_to_webp('images/' + name + ".jpg")

# 打印所有图片下载完成的消息
print("Done!")
