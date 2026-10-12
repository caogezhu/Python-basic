import time
from datetime import datetime

# 输入任务名称和番茄时长（分钟）
task_name = input("请输入任务名称：")
minute = int(input("请输入番茄时间(分钟)："))
total_sec = minute * 60

# 计算结束时间
end_time = datetime.fromtimestamp(time.time() + total_sec)
print(f"任务：{task_name}，预计结束时间：{end_time.strftime('%H:%M:%S')}")
print("番茄钟开始！")

# while循环倒计时
now_sec = total_sec
while now_sec > 0:
    m = now_sec // 60
    s = now_sec % 60
    print(f"剩余时间：{m:02d}:{s:02d}")
    time.sleep(1)
    now_sec -= 1

# 倒计时结束提醒
print("⏰ 时间到！该休息啦！")


# import time
#
# print("Download ...")
#
# # total 一共20小段
# total = 20
# for n in range(total + 1):
#     # n 代表现在完成了几段，从0，1，2 ... 20
#     ok = "=" * n
#     no = " " * (total - n)
#     jin_du_tiao = "[" + ok + no + "]"
#     baifenbi = int(n / total * 100)
#
#     print(f"\r{jin_du_tiao} {baifenbi}%", end="")
#     time.sleep(0.2)
# print()
