import os

def show(*dirs):
    for d in dirs:
        print(f"当前目录: {d}")
        print("子目录:")
        for n in os.listdir(d):
            if os.path.isdir(os.path.join(d,n)):
                print(f"<DIR>        {n}")
        print("文件:")
        for n in os.listdir(d):
            if not os.path.isdir(os.path.join(d,n)):
                print(n)

# 调用，传入多个目录
if __name__ == '__main__':
    show("F:/桌面文件预留/", "F:/DemoVideo/")
