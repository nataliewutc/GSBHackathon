from flask import Flask, render_template, request
import os


app = Flask(__name__)

picFolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        if request.form.get("Chair"):
            pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'chair1.jpg')
            return render_template('index.html', user_image = pic1)
        elif request.form.get("Yoga mat"):
            pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'mat.jpg')
            return render_template('index.html', user_image = pic2)
    elif request.method == "GET":
        blank = os.path.join(app.config['UPLOAD_FOLDER'], 'blank.jpg')
        return render_template('index.html', user_image = blank)

if __name__ == "__main__":
    app.run()
