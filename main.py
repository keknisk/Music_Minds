from PIL import Image
from flask import Flask, render_template

app = Flask(__name__)


# im1 = Image.open("static/images/album.jpg")
# im2 = Image.open("static/images/album2.jpg")
# im3 = Image.open("static/images/album3.jpg")



@app.route('/')
def home():
    im1 = Image.open("static/images/album.jpg")
    im2 = Image.open("static/images/album2.jpg")
    im3 = Image.open("static/images/album3.jpg")

    return render_template('index.html', image = im1)






app.run(debug=True)