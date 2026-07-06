while True:
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码:")

    if username == "" or password == "":
        print("用户名或密码为空，请重新输入！")
        continue
    if username == "admin" and password == "123456":
        print("登录成功！进入B站首页！")
        break
    elif username == "bengtie" and password == "123123":
        print("登录成功！进入B站首页！")
        break
    elif username == "wz" and password == "456456":
        print("登录成功！进入B站首页！")
        break
    else:
        print("用户名或密码错误！请重新输入！")