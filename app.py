import os
from flask import Flask, send_from_directory
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("site/index.html")


@app.route("/about")
def about():
    return render_template("site/about.html")


@app.route("/blog")
def blog():
    return render_template("site/blog.html")


@app.route("/youtube")
def youtube():
    return render_template("site/youtube.html")


@app.route("/css/<cssfile>")
def css_link(cssfile):
    return send_from_directory(os.path.join("templates/site/css"), cssfile)


@app.route("/images/<imagefile>")
def image_link(imagefile):
    return send_from_directory(os.path.join("templates/site/images"), imagefile)


@app.route("/icomoon/<icomoonfile>")
def icomoon_link(icomoonfile):
    return send_from_directory(
        os.path.join("templates/site/fonts/icomoon"), icomoonfile
    )


@app.route("/flaticon/<flaticonfile>")
def flaticon_link(flaticonfile):
    return send_from_directory(
        os.path.join("templates/site/fonts/flaticon"), flaticonfile
    )


@app.route("/ionicons/<ioniconsfile>")
def ionicons_link(ioniconsfile):
    return send_from_directory(
        os.path.join("templates/site/fonts/ionicons"), ioniconsfile
    )


@app.route("/iconic/<iconicfile>")
def iconic_link(iconicfile):
    return send_from_directory(
        os.path.join("templates/site/fonts/open-iconic"), iconicfile
    )


@app.route("/typefonts/<typefontfile>")
def typefont_link(typefontfile):
    return send_from_directory(
        os.path.join("templates/site/fonts/typefonts"), typefontfile
    )


@app.route("/webfonts/<webfontsfile>")
def webfonts_link(webfontsfile):
    return send_from_directory(
        os.path.join("templates/site/fonts/webfonts"), webfontsfile
    )


@app.route("/scss/<scssfile>")
def scss_link(scssfile):
    return send_from_directory(os.path.join("templates/site/scss"), scssfile)


@app.route("/js/<jsfile>")
def js_link(jsfile):
    return send_from_directory(os.path.join("templates/site/js"), jsfile)


if __name__ == "__main__":
    app.run(host="192.168.68.115", debug=True)
