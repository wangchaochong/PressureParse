import time
import serial
from ParseTaiYa import ParseTaiYa
from ParseTaiYa2 import ParseTaiYa2
from log_handler import get_logging

# 实例化log对象
# logger = get_logging(file_name=r"C:\Users\Administrator\Desktop\胎压解析脚本\log.txt")


class SerialDate(object):
    def __init__(self, portx, bps, timeout):
        self.portx = portx
        self.bps = bps
        self.timeout = timeout

    def DOpenPort(self):
        try:
            # 打开串口，并得到串口对象
            self.ser = serial.Serial(self.portx, self.bps, timeout=self.timeout)
            # 判断是否打开成功
            if (self.ser.is_open == False):
                self.ser = -1
        except Exception as e:
            print("---异常---：", e)
        return self.ser

    def DColsePort(self):
        self.ser = self.DOpenPort()
        self.ser.close()

    def DReadPort(self,num):
        try:
            self.ser = self.DOpenPort()
            while (self.ser != -1):
                # time.sleep(0.2)
                try:
                    if self.ser.in_waiting:
                        recv = self.ser.readline(self.ser.in_waiting).decode("gb18030","ignore").strip()
                        log_data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        # logger.info(f"{log_data}{'  '}{recv}")
                        recv_data = recv.split(",")
                        # print(recv_data)
                        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), "  ", recv)
                        if len(recv_data) > 1:
                            if "ab04" in recv_data[1][:5]:
                                ParseTaiYa2().start(eval(recv_data[1]))
                            if "ab03" in recv_data[1][:5]:
                                ParseTaiYa2().start(eval(recv_data[1]))
                            if "ab02" in recv_data[1][:5]:
                                ParseTaiYa(eval(recv_data[1]))
                                # print(a[0])
                            if "ab06" in recv_data[1][:5]:
                                ParseTaiYa(eval(recv_data[1]))
                                # print(a[0])
                            if "AB11" in recv_data[1][:5]:
                                ParseTaiYa2().start(recv_data[1])
                            if "ab05" in recv_data[1][:5]:
                                ParseTaiYa2().start(eval(recv_data[1]))
                            if "ab09" in recv_data[1][:5]:
                                ParseTaiYa(eval(recv_data[1]))
                            if "AB0F" in recv_data[1][:5]:
                                ParseTaiYa2().start(recv_data[1])
                except Exception as e:
                    print("解析错误")
                    print(e)
                time.sleep(num)
                # continue

        except Exception as e:
            input(e)
            self.DReadPort(num)
        finally:
            self.DColsePort()


if __name__ == '__main__':
    a = 1
    if a == 0:
        ss = SerialDate("COM4", 9600, 0.5)
        ss.DReadPort(0.09)
    else:
        ss = SerialDate("COM4", 115200, 0.5)
        ss.DReadPort(0.22)


