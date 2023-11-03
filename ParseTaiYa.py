import requests


def ParseTaiYa(str):
    try:
        url = "https://toro.qcql.cn/api/web/device/cmd"
        data = {"data": str}
        res = requests.post(url=url, json=data)
        print(res.json()["data"])
    except:
        print("接口超时")


if __name__ == '__main__':
    ParseTaiYa("ab021716010b340000898604d80922202497041c03677757612a")
