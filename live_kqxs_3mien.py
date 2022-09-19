import imp
import requests
import json
import time
import base64
from datetime import date

TELEGRAM_BOT_TOKEN = "5794737725:AAEOhcTllr08CN-RbGDKbd3UsvRedcbbJUE"
TELEGRAM_CHANNEL = "@kqxs3mien"

URL_KQXS_MIEN_NAM = "http://api.xoso.me/app/json-kq-miennam?ngay_quay={}"
URL_KQXS_MIEN_TRUNG = "http://api.xoso.me/app/json-kq-mientrung?ngay_quay={}"
URL_KQXS_MIEN_BAC = "http://api.xoso.me/app/json-kq-mienbac?ngay_quay={}"

def sendMSG(kqxs):

    msg = kqxs
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=html&text={}".format(TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL, msg)
    headers = {}
    response = requests.get(
        url, headers=headers)
    kq = response.text

def getLotoDAU(key, ketquaJson):

    loto = ""
    json_array = ketquaJson[key]
    for item in json_array:
        if (len(loto)):
            loto = loto + ","
        loto = loto + " {}{}".format(key, str(item))
    return loto

def getLotoDUOI(key, ketquaJson):

    loto = ""
    json_array = ketquaJson[key]
    for item in json_array:
        if (len(loto)):
            loto = loto + ","
        loto = loto + " {}{}".format(str(item), key)
    return loto  

def getKQXS(kqxs_vung):

    today = str(date.today())
    headers = {}

    if (kqxs_vung == "GET_KQXS_MIEN_NAM"):
        response = requests.get(
            URL_KQXS_MIEN_NAM.format(today), headers=headers)
        kq = response.text
        print(kq)
        return kq

    elif (kqxs_vung == "GET_KQXS_MIEN_TRUNG"):
        response = requests.get(
        URL_KQXS_MIEN_TRUNG.format(today), headers=headers)
        kq = response.text
        print(kq)
        return kq

    else:
        response = requests.get(
            URL_KQXS_MIEN_BAC.format(today), headers=headers)
        kq = response.text
        print(kq)
        return kq

def getData(kqxs_vung):
    
    ketqua = getKQXS(kqxs_vung)
    json_array = json.loads(ketqua)

    if (kqxs_vung == "GET_KQXS_MIEN_BAC"):
        sendData(kqxs_vung, json_array)

    else:
        for item in json_array:
            sendData(kqxs_vung, item)

def sendData(kqxs_vung, item):

    provinceName = item["provinceName"]
    lotData = item["lotData"]
    dau = item["dau"]
    duoi = item["duoi"]
    tuong_thuat = item["tuong_thuat"]

    db = "Đặc biệt: <b>{}</b>".format(str(lotData["DB"]).replace("'", "").replace("[", "").replace("]", ""))
    g1 = "Giải nhất: <b>{}</b>".format(str(lotData["1"]).replace("'", "").replace("[", "").replace("]", ""))
    g2 = "Giải nhì: <b>{}</b>".format(str(lotData["2"]).replace("'", "").replace("[", "").replace("]", ""))
    g3 = "Giải ba: <b>{}</b>".format(str(lotData["3"]).replace("'", "").replace("[", "").replace("]", ""))
    g4 = "Giải tư: <b>{}</b>".format(str(lotData["4"]).replace("'", "").replace("[", "").replace("]", ""))
    g5 = "Giải năm: <b>{}</b>".format(str(lotData["5"]).replace("'", "").replace("[", "").replace("]", ""))
    g6 = "Giải sáu: <b>{}</b>".format(str(lotData["6"]).replace("'", "").replace("[", "").replace("]", ""))
    g7 = "Giải bảy: <b>{}</b>".format(str(lotData["7"]).replace("'", "").replace("[", "").replace("]", ""))
    g8 = ""

    text_kq = db + "\n" + g1 + "\n" + g2 + "\n" + g3 + "\n" + g4 + "\n" + g5 + "\n" + g6 + "\n" + g7

    if (kqxs_vung != "GET_KQXS_MIEN_BAC"):
        g8 = "Giải tám: <b>{}</b>".format(str(lotData["8"]).replace("'", "").replace("[", "").replace("]", ""))
        text_kq = text_kq + "\n" + g8 

    d0 = "0: <b>{}</b>".format(getLotoDAU("0", dau))
    d1 = "1: <b>{}</b>".format(getLotoDAU("1", dau))
    d2 = "2: <b>{}</b>".format(getLotoDAU("2", dau))
    d3 = "3: <b>{}</b>".format(getLotoDAU("3", dau))
    d4 = "4: <b>{}</b>".format(getLotoDAU("4", dau))
    d5 = "5: <b>{}</b>".format(getLotoDAU("5", dau))
    d6 = "6: <b>{}</b>".format(getLotoDAU("6", dau))
    d7 = "7: <b>{}</b>".format(getLotoDAU("7", dau))
    d8 = "8: <b>{}</b>".format(getLotoDAU("8", dau))
    d9 = "9: <b>{}</b>".format(getLotoDAU("9", dau))

    text_loto_dau = d0 + "\n" + d1 + "\n" + d2 + "\n" + d3 + "\n" + d4 + "\n" + d5 + "\n" + d6 + "\n" + d7 + "\n" + d8 + "\n" + d9 

    d0 = "0: <b>{}</b>".format(getLotoDUOI("0", duoi))
    d1 = "1: <b>{}</b>".format(getLotoDUOI("1", duoi))
    d2 = "2: <b>{}</b>".format(getLotoDUOI("2", duoi))
    d3 = "3: <b>{}</b>".format(getLotoDUOI("3", duoi))
    d4 = "4: <b>{}</b>".format(getLotoDUOI("4", duoi))
    d5 = "5: <b>{}</b>".format(getLotoDUOI("5", duoi))
    d6 = "6: <b>{}</b>".format(getLotoDUOI("6", duoi))
    d7 = "7: <b>{}</b>".format(getLotoDUOI("7", duoi))
    d8 = "8: <b>{}</b>".format(getLotoDUOI("8", duoi))
    d9 = "9: <b>{}</b>".format(getLotoDUOI("9", duoi))

    text_loto_duoi = d0 + "\n" + d1 + "\n" + d2 + "\n" + d3 + "\n" + d4 + "\n" + d5 + "\n" + d6 + "\n" + d7 + "\n" + d8 + "\n" + d9 
        
    today = date.today()
    text_date = today.strftime("%d/%m/%Y")

    if (kqxs_vung == "GET_KQXS_MIEN_NAM"):
        text_title = "Kết quả xổ số <b>{}</b> đài <b>{}</b> ngày <b>{}</b>".format("Miền Nam", provinceName, text_date)

    elif (kqxs_vung == "GET_KQXS_MIEN_TRUNG"):
        text_title = "Kết quả xổ số <b>{}</b> đài <b>{}</b> ngày <b>{}</b>".format("Miền Trung", provinceName, text_date)

    else:
        text_title = "Kết quả xổ số <b>{}</b> ngày <b>{}</b>".format("Miền Bắc", text_date)

    text_send_msg = "{}\n\n<b>{}</b>\n{}\n\n<b>{}</b>\n{}\n\n<b>{}</b>\n{}".format(text_title, "KẾT QUẢ", text_kq, "ĐẦU", text_loto_dau, "ĐUÔI", text_loto_duoi)

    print(text_title)
    print(text_send_msg)
    sendMSG(text_send_msg)

def cloudFuntionCall(event, context):

    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    if (pubsub_message == "GET_KQXS_MIEN_NAM"):
        print("lay ket qua xo so mien NAM")

    elif (pubsub_message == "GET_KQXS_MIEN_TRUNG"):
        print("lay ket qua xo so mien TRUNG")

    else:
        print("lay ket qua xo so mien BAC")
    getData(pubsub_message)

if __name__ == "__main__":
    getData()