from flask import Flask
from flask import send_file
from flask import render_template
from markupsafe import Markup
import os
import get_volume
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    message = "Red 19 Zine"
    return render_template('index.html', message=message)


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')


@app.route('/upcoming_events')
def upcoming_events():
    return render_template("upcoming_events.html")


@app.route('/latest_volume')
def latest_volume():
    return render_template("latest_volume.html")


@app.route('/previous_volumes')
def previous_volumes():
    volume_numbers = get_volume.get_volumes()[0][1]
    message = ""

    for volume_number in volume_numbers:
        message += f"<h3><a href=\"volumes/{volume_number}\"> Volume {volume_number} </a></h3>\n"

    return render_template("previous_volumes.html", message=Markup(message))


@app.route('/volumes/<int:volume_number>')
def volume(volume_number):
    pics = [str(volume_number) + '/' + pic for pic in get_volume.get_volumes()[volume_number][2]]
    return render_template("volume.html", pics=pics)


@app.route('/get_image')
def get_image():
    filename = "static/volumes/1/0001.jpg"
    return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(debug=True)
