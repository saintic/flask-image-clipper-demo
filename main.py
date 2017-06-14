# coding: utf8

import os, base64
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
#文件上传文件夹, 相对于项目根目录, 请勿改动static/部分
IMAGE_FOLDER     = 'static'
UPLOAD_FOLDER    = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

#对头像图片上传进行响应
@app.route('/upload/', methods=['POST','OPTIONS'])
def upload():
    if request.form.get("action") == "add":
        data = request.form.get("picStr")
        imgdata=base64.b64decode(data)
        imgfile=os.path.join(UPLOAD_FOLDER, "test.jpg")
        file=open(imgfile, 'wb')
        file.write(imgdata)  
        file.close()
        return jsonify(imgfile=imgfile)

if __name__ == "__main__":
    app.run(debug=True)