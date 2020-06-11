#https://bj.lianjia.com/ditiefang/li652s43139478/
import requests, time, json
from bs4 import BeautifulSoup

requests.adapters.DEFAULT_RETRIES = 5

def getHouseList():
    for i in range(1, 100):
        url = "https://bj.lianjia.com/ditiefang/li652s43139478/pg{}/".format(i)
        print(url)
        s = requests.session()
        s.keep_alive = False
        html = s.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.find_all(class_='sellListContent')
        if len(contents) == 0:
            break
        content = contents[0]
        lis = content.find_all("li")
        for li in lis:
            house = {}
            print(li)
            # id
            house["id"] = li.find_all("a")[0]["data-housecode"]
            # 首页图片
            house["img"] = li.find_all("a")[0].find_all(class_="lj-lazy")[0]["data-original"]
            # 信息
            info = li.find_all(class_="info")[0]
            # 优势
            house["good"] = info.find_all(class_="title")[0].find_all("a")[0].text
            positions = info.find_all(class_="positionInfo")[0].find_all("a")
            # 小区名称
            house["communityName"] = positions[0].text
            # 小区位置
            house["communityPos"] = positions[1].text
            # 小区信息
            houseInfo = info.find_all(class_='houseInfo')[0].text.split("|")
            print(houseInfo)
            # 房间数
            house["roomSize"] = str(houseInfo[0]).strip()
            # 总面积
            house["space"] = str(houseInfo[1]).strip()
            # 朝向
            house["orientation"] = str(houseInfo[2]).strip()
            # 装修类型
            house["fixType"] = str(houseInfo[3]).strip()
            # 楼层
            house["floor"] = str(houseInfo[4]).strip()
            # 建成时间
            house["buildTime"] = str(houseInfo[5]).strip()
            # 房屋类型
            house["buildType"] = str(houseInfo[6]).strip()
            print(json.dumps(house))
            singleHouse(house["id"])
            break
        break

def singleHouse(houseId):
    url = "https://bj.lianjia.com/ershoufang/{}.html".format(houseId)
    print(url)
    s = requests.session()
    s.keep_alive = False
    html = s.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

getHouseList()