from flask import Flask, request
import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    # id=[d['replyToken'] for d in user][0]
    # print(json_line)
    print("ผู้ใช้：", user)
    sendText(user, 'งง คืออะไรเค้างง')  # ส่งข้อความ งง
    return '', 200


def sendText(user, text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = '77/rUD66AxteA86L+M7a1f8KtwtcXXt98K9X9uPHNpVB6xftyxYXTOVJihjNFeOzQyOfPY6KO1BVUO974Jkjlm5FkO3JKRZkv9O/BLJLpFpCrdhkjGHLq6QFh0MaEBbM5ZZz3wb6eJtmQM8cCkz/EgdB04t89/1O/w1cDnyilFU='  # ใส่ ENTER_ACCESS_TOKEN เข้าไป

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = json.dumps({
        "replyToken": user,
        "messages": [{
            "type": "text",
            "text": text
        }]
    })

    # print("ข้อมูล：",data)
    r = requests.post(LINE_API, headers=headers, data=data)  # ส่งข้อมูล
    # print(r.text)


if __name__ == '__main__':
    app.run(debug=True)