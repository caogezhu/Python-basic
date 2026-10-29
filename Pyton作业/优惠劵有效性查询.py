# 定义检查优惠券有效性的函数
def check_coupon(coupon_code):
    # 预设有效的优惠券代码（可以自己增删）
    valid_codes = {"BOOK20", "READ50", "NEW10", "AUTUMN30"}
    if coupon_code in valid_codes:
        return True
    else:
        return False

# 键盘读取输入
user_input = input("请输入优惠券代码：")

# 调用函数进行校验
if check_coupon(user_input):
    print("优惠券有效")
else:
    print("优惠券无效")
