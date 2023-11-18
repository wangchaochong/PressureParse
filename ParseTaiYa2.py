


class ParseTaiYa2(object):
    def Test_mode_data(self,data):
        sn = data[6:14]
        version_num1 = int(data[14:16], 16)
        version_num2 = int(data[16:18], 16)
        battery_value = int(data[18:22], 16)
        nb_signal = int(data[22:24], 16)
        radio_433_signal = -int(data[26:28], 16)
        print("SN:{},版本号:{}.{},电池电量:{}mv,NB信号值:{},433信号值:{}".format(sn,version_num1,version_num2,battery_value,nb_signal,radio_433_signal))

    # 胎压解析
    def parse_data2(self, data2):
        # data = "0a6c1480010142"
        wheel_idx = data2[:2]
        axle = int(wheel_idx[0])+1
        wheel_num = int(wheel_idx[1])+1
        alarm_time = int(data2[2:4], 16)
        presure = int(data2[4:8], 16) / 100
        tempture = int(data2[8:10], 16) - 50
        if presure == 655.35 and tempture == 205:
            print("{0:>2}轴{1}号轮失联".format(axle,wheel_num), end=" ")
        else:
            print("{0:>2}轴{1}号轮胎压{2:>2}bar, 温度{3:>2}℃,报警次数{4}".format(axle, wheel_num, presure, tempture, alarm_time),end=" ")

        status = bin(int(data2[10:14], 16)).replace("b","")
        for i in range(len(status)):
            list1 = []
            num = "0000000000000000"
            if (num + status)[::-1][0] == "1":
                list1.append("胎压报警")
            if (num + status)[::-1][1] == "1":
                list1.append("高温报警")
            if (num + status)[::-1][2] == "1":
                list1.append("漏气报警")
            if (num + status)[::-1][3] == "1":
                list1.append("同轴压差报警")
            if (num + status)[::-1][4] == "1":
                list1.append("无信号报警")
            if (num + status)[::-1][5] == "1":
                list1.append("低电报警")
            if (num + status)[::-1][6] == "1":
                list1.append("轮毂占用")
            if (num + status)[::-1][6] == "0":
                list1.append("轮毂清除")
            if (num + status)[::-1][7] == "1":
                list1.append("传感器绑定")
            if (num + status)[::-1][7] == "0":
                list1.append("传感器未绑定")
        print("{}".format(str("|".join(list1)), end=""))

        if data2[14:18].lower() != "ffff":
            axle_tempture = int(data2[14:18], 16) - 200
            print("轴温{0:>3}℃".format(axle_tempture,end=""))

        axle_staus = bin(int(data2[18:20], 16)).replace("b","")
        for i in range(len(axle_staus)):
            list = []
            num = "0000000000000000"
            if (num + axle_staus)[::-1][0] == "1":
                list.append("轴温报警")
            if (num + axle_staus)[::-1][1] == "1":
                list.append("同轴温差报警")
            if (num + axle_staus)[::-1][2] == "1":
                list.append("无信号报警")
            if (num + axle_staus)[::-1][3] == "0":
                list.append("轴温未匹配")
            if (num + axle_staus)[::-1][3] == "1":
                list.append("轴温匹配")
        print("轴温报警状态:  {}".format(str("|".join(list)), end=" "))



    # 轴温解析
    def Axle_Date(self, data3):
        Axle_text = {1: "挂车1轴左侧",
                     2: "挂车1轴右侧",
                     3: "挂车2轴左侧",
                     4: "挂车2轴右侧",
                     5: "挂车3轴左侧",
                     6: "挂车3轴右侧"}
        wheel_idx = int(data3[:2], 16)
        tempture = int(data3[2:6], 16) - 60
        print("{}轮,{}℃".format(Axle_text[wheel_idx], tempture))

    def parse_data(self, data2):
        # data = "0a6c1480010142"
        wheel_idx = int(data2[:2], 16)
        presure = int(data2[2:4], 16) / 10
        tempture = int(data2[4:6], 16) - 55
        status = bin(int(data2[6:10], 16))
        bag_number = int(data2[10:12], 16)
        signal = int(data2[12:14], 16)
        relay_id = data2[-4:]
        # data = {1: "挂车1轴左外", 2: "挂车1轴左内", 3: "挂车1轴右内", 4: "挂车1轴右外", 5: "挂车2轴左外", 6: "挂车2轴左内", 7: "挂车2轴右内", 8: "挂车2轴右外",9: "挂车3轴左外", 10: "挂车3轴左内",
        #         11: "挂车3轴右内", 12: "挂车3轴右外", 201: "S1", 202: "S2", 203: "S3", 204: "S4"}

        if presure == 25.3 and tempture == -8:
            print(end="")
        elif presure == 25.3 and tempture == -3:
            print(end="")
        else:
            print("{0:>2}号轮胎压{1:>2}bar, 温度{2:>2}℃, 包序号{3:>2},{4:>3}db,中继器ID后4位:{5}".format(wheel_idx, presure, tempture,
                                                                                           bag_number, signal,
                                                                                           relay_id),
                  end=" ")
        for i in range(len(status)):
            list = []
            num = "0000000000000000"
            if (num + status)[::-1][0] == "1":
                list.append("传感器失联")
                break
            if (num + status)[::-1][1] == "1":
                list.append("高温报警")
            if (num + status)[::-1][2] == "1":
                list.append("胎压报警")
            if (num + status)[::-1][3] == "1":
                list.append("漏气报警")
            if (num + status)[::-1][4] == "1":
                list.append("压差报警")
            if (num + status)[::-1][5] == "1":
                list.append("低电报警")
            if (num + status)[::-1][6] == "1":
                list.append("胎压重置")
            if (num + status)[::-1][7] == "1":
                list.append("传感器故障")
            if (num + status)[::-1][12] == "1":
                list.append("中继转发")
            if (num + status)[::-1][13] == "1":
                list.append("轮胎加气了")
            if (num + status)[::-1][14] == "1":
                list.append("低频触发数据是{}".format(signal))
            if (num + status)[::-1][15] == "1":
                list.append("停车胎压数据")
        if len(list) == 0:
            print()
        else:
            print("{0:>2}号轮{1:<50}".format(wheel_idx, str("|".join(list))))

    # 中继器状态
    def Parse_relay_status(self, data4):
        num = "00000000"
        status_data = num + bin(int(data4, 16))[2:]
        for i in range(len(status_data)):
            list = []
            battery_sataus = "".join(status_data[::-1][1:3][::-1])
            # print(battery_sataus)
            if status_data[::-1][0] == "1":
                list.append("中继器失联")
            if status_data[::-1][3] == "1":
                list.append("外接电源")
            if status_data[::-1][3] == "0":
                list.append("电池供电")
            if status_data[::-1][4] == "1":
                list.append("喷淋开启")
            if status_data[::-1][5] == "1":
                list.append("定时数据")
            if status_data[::-1][6] == "1":
                list.append("心跳数据")
            if status_data[::-1][7] == "1":
                list.append("控制器脱落")

            if battery_sataus == "00":
                list.append("电池未充电")
            if battery_sataus == "01":
                list.append("电池正在充电")
            if battery_sataus == "10":
                list.append("电池充电故障")
        return list

    # # BMS状态
    # def Parse_BMS(self,data5):
    #     for i in range(len(data5)):
    #         list = []
    #         num = "0000000000000000"
    #         if (num + data5)[::-1][0] == "1":
    #             list.append("1")
    #         if (num + data5)[::-1][1] == "1":
    #             list.append("2")
    #         if (num + data5)[::-1][2] == "1":
    #             list.append("3")
    #         if (num + data5)[::-1][3] == "1":
    #             list.append("4")
    #         if (num + data5)[::-1][4] == "1":
    #             list.append("5")
    #         if (num + data5)[::-1][5] == "1":
    #             list.append("6")
    #         if (num + data5)[::-1][6] == "1":
    #             list.append("7")
    #         if (num + data5)[::-1][7] == "1":
    #             list.append("8")
    #         if (num + data5)[::-1][8] == "1":
    #             list.append("9")
    #         if (num + data5)[::-1][9] == "1":
    #             list.append("10")
    #     if '9' in list:
    #         list.remove('1')
    #         list.remove('2')
    #     if '10' in list:
    #         list.remove('1')
    #         list.remove('4')
    #     return list
    #
    # status_data = {"1": "1充气管路故障",
    #                "2": "2挂车气源部分漏气",
    #                "3": "3牵引车手控阀或者挂车阀故障",
    #                "4": "4挂车行车制动失效或者部分失效",
    #                "5": "5车辆行驶行驶",
    #                "6": "6车辆正常制动",
    #                "7": "7充气管路充气不及时",
    #                "8": "3牵引车手控阀或者2挂车气源部分漏气",
    #                "9": "1充气故障和2挂车气源部分漏气",
    #                "10": "1充气管路故障+4挂车行车制动失效或者部分失效"}

   # 关闭模式解析
    def Parse_Close_Model(self, data):
        for i in range(len(data)):
            list = []
            num = "0000000000000000"
            if (num + data)[::-1][0] == "1":
                list.append("光敏关闭模式")
            if (num + data)[::-1][1] == "1":
                list.append("低电关闭模式")
            if (num + data)[::-1][2] == "1":
                list.append("低功耗模式")
            if (num + data)[::-1][3] == "1":
                list.append("蓝牙球阀开")
            if (num + data)[::-1][3] == "0":
                list.append("蓝牙球阀关")
            if (num + data.replace("b",""))[::-1][4:6][::-1] == "00":
                list.append("球阀关闭状态")
            if (num + data.replace("b",""))[::-1][4:6][::-1] == "01":
                list.append("球阀开启状态")
            if (num + data.replace("b",""))[::-1][4:6][::-1] == "10":
                list.append("球阀转换状态")
            if (num + data.replace("b",""))[::-1][4:6][::-1] == "11":
                list.append("球阀未知状态")
        return list

    # 解析下行数据
    def Parse_police_parameter(self, data):
        axle_num = int(data[:2],16)
        low_pressure_police = int(data[2:4], 16) / 10
        high_pressure_police = int(data[4:6], 16) / 10
        high_temperature_ploice = int(data[-2:], 16) - 50
        print("第{}轴,{}--{}bar,温度{}℃".format(axle_num, low_pressure_police, high_pressure_police, high_temperature_ploice))

    def Pares_sensor_parameter(self, data):
        wheel_num = int(data[:2],16)
        sensor_id = data[2:]
        print("第{0:<3}轮，传感器id：{1}".format(wheel_num, sensor_id))

    def Pares_gps_icon_status(self, data):
        num = "00000000"
        status_data = num + bin(data)[2:]
        list = []
        for i in range(len(status_data)):
            list = []
            if status_data[::-1][0] == "1":
                list.append("gps图标开")
            if status_data[::-1][0] == "0":
                list.append("gps图标关")
            if status_data[::-1][1] == "1":
                list.append("重置丢包统计")
            if status_data[::-1][2] == "0":
                # 打开会有滴的声音，界面闪烁，R3设备
                list.append("失联报警打开")
            if status_data[::-1][2] == "1":
                list.append("失联报警关闭")
            # if status_data[::-1][3] == "1":
            #     list.append("电磁阀开")
            # if status_data[::-1][3] == "0":
            #     list.append("电磁阀关")
        return list

    def Down_Parse(self, str):
        pressure_upload_num = int(str[6:10],16)
        gps_upload_num = int(str[10:14],16)
        gps_location_num = int(str[14:16],16)
        print("胎压上报频次：{}s".format(pressure_upload_num))
        print("gps上报频次：{}s".format(gps_upload_num))
        print("运动模式gps定位频率:{}次".format(gps_location_num))

        all_axle_num = int(str[20:22],16)
        str1 = str[22:]
        police_parameter = [str1[i:i + 8] for i in range(0, len(str1), 8)][:all_axle_num]
        for police_data in police_parameter:
            self.Parse_police_parameter(police_data)

        all_wheel_num = int(str1[8 * all_axle_num:][:2], 16)
        str2 = str1[8 * all_axle_num + 2:]
        sensor_parameter = [str2[i:i + 10] for i in range(0, len(str2), 10)][:all_wheel_num]
        for sensor_data in sensor_parameter:
            self.Pares_sensor_parameter(sensor_data)

        str3 = str2[10 * all_wheel_num:]
        # gps图标开关
        gps_icon_switch = int(str3[:2], 16)
        gps_icon_status = self.Pares_gps_icon_status(gps_icon_switch)
        # 失联时间
        missing_time = int(str3[2:4], 16)
        # 附加轮
        append_wheel_num = int(str3[4:6], 16)
        str4 = str3[6:]
        append_wheel_parameter = [str4[i:i + 10] for i in range(0, len(str4), 10)][:append_wheel_num]
        for append_wheel_data in append_wheel_parameter:
            if len(str3) == 10:  # R5G
                pass
            else:
                self.Pares_sensor_parameter(append_wheel_data)

        str5 = str4[10 * append_wheel_num:]
        # location_cycle = int(str5[:4], 16)
        print("gps状态：{}".format(gps_icon_status))
        print("传感器、中继器失联时间：{}分钟".format(missing_time))
        if len(str3) == 10: #R5G
            location_cycle = int(str3[4:8], 16)
            print("定位周期：{}分钟".format(location_cycle))

        if len(str5) == 6: #R3E/R5A
            heartbeat_cycle = int(str5[:4], 16)
            print("心跳周期：{}分钟".format(heartbeat_cycle))

        if len(str5) == 12: #R9A
            location_cycle = int(str5[:4], 16)
            heartbeat_cycle = int(str5[4:8], 16)
            print("定位周期：{}分钟，心跳周期：{}分钟".format(location_cycle, heartbeat_cycle))

        if len(str5) == 16: #R90
            location_cycle = int(str5[:4], 16)
            heartbeat_cycle = int(str5[4:8], 16)
            print("定位周期：{}分钟，心跳周期：{}分钟".format(location_cycle, heartbeat_cycle))
            switch_on_value = int(str5[10:12], 16)
            switch_off_value = int(str5[12:14], 16)
            if switch_on_value == 0:
                print("喷淋功能关闭")
            else:
                print("喷淋开始阈值：{}℃".format(switch_on_value))
                print("喷淋结束阈值：{}℃".format(switch_off_value))

    def Parse_Pressure(self, str):
        all_wheel_num = int(str[6:8],16)
        str1 = str[8:]
        pressure_data = [str1[i:i + 18] for i in range(0, len(str1), 18)][:all_wheel_num]
        for data in pressure_data:
            self.parse_data(data)
        # 关闭模式
        close_data = bin(int(str1[18 * all_wheel_num:][:2], 16))
        close_model = self.Parse_Close_Model(close_data)
        str2 = str1[18 * all_wheel_num + 2:]
        gps_data = str2[:30]
        speed = int(gps_data[16:18], 16)
        str3 = str2[30:]
        if len(str3) == 16:
            # ABS供电电压
            power = int(str3[4:8], 16)
            # 电池电压
            battery = int(str3[8:12], 16)
            # 状态标识位
            status_flag = str3[12:14]  # 没有转成16进制
            # 状态标识位
            sign = self.Parse_relay_status(status_flag)
            print("速度{}km/h,状态：{},模式:{}".format(speed, sign, close_model))
            print("车载电压:{}mv,电池电压:{}mv".format(power, battery))

        if len(str3) == 12:  # R5A
            # ABS供电电压
            power = int(str3[:4], 16)
            # 电池电压
            # battery = int(str3[4:8], 16)
            # 状态标识位
            status_flag = str3[8:10]  # 没有转成16进制
            # 状态标识位
            sign = self.Parse_relay_status(status_flag)
            print("速度{}km/h,状态：{},模式:{}".format(speed, sign, close_model))
            print("车载电压:{}mv".format(power))

    def Parse_Pressure2(self, str):
        agreement_num = int(str[6:8],16)
        car_model_num = int(str[8:10],16)
        unit = int(str[10:12],16)
        if agreement_num == 0:
            print("设备编号:R3E")
        if agreement_num == 1:
            print("设备编号:R3Z")
        if car_model_num == 0:
            print("车型：牵引车")
        if car_model_num == 1:
            print("车型：挂车/公交车")
        if car_model_num == 2:
            print("车型：牵引车+挂车")
        all_wheel_num = int(str[12:14],16)
        str1 = str[14:]
        pressure_data = [str1[i:i + 20] for i in range(0, len(str1), 20)][:all_wheel_num]
        for data in pressure_data:
            self.parse_data2(data)


    def start(self, data1):
        if ("ab04" in data1) or ("ab03" in data1):
           self.Parse_Pressure(data1)

        if "ab0f" in data1.lower():
           self.Parse_Pressure2(data1)

        if data1[:4] == "ab05":
            new_list = data1[8:]
            result = [new_list[i:i + 6] for i in range(0, len(new_list), 6)][:-1]
            for i in result:
                self.Axle_Date(i)

        if "ab11"in data1.lower():
            self.Down_Parse(data1)

        if "ab09" in data1[0:4]:
            self.Test_mode_data(data1)


if __name__ == '__main__':
    aa = ParseTaiYa2()
    # aa.start("AB0F7D0002010C30000000320040FFFF0031000000320040FFFF0032000000320040FFFF0033000000320040FFFF0040000000320040FFFF0041000000320040FFFF0042000000320040FFFF0043000000320040FFFF0050000000320040FFFF0051000000320040FFFF0052000000320040FFFF0053000000320040FFFF001E")
    # aa.start("ab0419000400000000000000000000000000000000000a340bbb8043")
    while True:
        data = input("请输入：").strip()
        aa.start(data)


