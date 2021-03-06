import os
from flask import Flask, render_template, url_for, redirect, flash, request, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__) #'__name__'= __main__ this is that flask knows where to look for static, template, etc. files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
@app.route("/mainPage")
def mainPage():
    return render_template("mainPageTemplates/mainPageV1.5.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        print("post request called")
        if request.files:
            file = request.files['file']
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_filename(file.filename)))
            print("file saved")
            return redirect(request.url)
        else:
            print('No Files Uploaded to Server!')
    return render_template("upload/upload.html")


@app.route("/uploads/<path:path>")
def send_file(path):
        #print('uploads', path)
        return send_from_directory('uploads',path)

@app.route("/development")
def contextMenu():
    return render_template("development/addRemoveNodesAndEdges2.html")

@app.route("/mainPage(2)")
def mainPage2():
    return render_template("mainPageTemplates/mainPageV1.3(2).html")

@app.route("/mainPage(3)")
def mainPage3():
    return render_template("mainPageTemplates/mainPageV1.3.html")


if __name__ == "__main__":
    app.run(debug = True)