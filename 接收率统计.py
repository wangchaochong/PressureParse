# data = "ab087e1f0152600202000000030000000400000005000000060000000700000008000000090000000a0000000b0000000c0000000d0000000e0000000f000000100000001100000012000000130000001400000015000000160000009752600298000000990000009a0000009b0000009c0000009d0000009e0000009f0000008f"
#

def parse_data(data):
    # data = "01526002"
    wheel_idx = int(data[:2],16)
    # 帧接收率
    receive1 = int(data[2:4],16)
    # 包接收率
    receive2 = int(data[4:6],16)
    # 接收总包数
    total_num = int(data[6:8],16)
    print("{0:>3}号轮的帧接收率:{1:^2}% 包接收率:{2:^2}% 接收总包数:{3}".format(wheel_idx, receive1, receive2, total_num*100))


if __name__ == '__main__':
    while True:
        data3 = input("请输入数据:")
        data1 = data3[6:]
        data2 = data1[2:]
        # print(data2)
        wheel_num = int(data1[:2], 16)
        result = [data2[i:i+8] for i in range(0,len(data2),8)][:-1]
        print("总共{}条数据".format(wheel_num))
        for i in result:
            parse_data(i)

