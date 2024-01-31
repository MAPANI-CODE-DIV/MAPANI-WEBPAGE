import os

from flask import send_from_directory, render_template, Blueprint


site_ = Blueprint("site_blueprint", __name__, template_folder='templates')


@site_.route("")
def home():
    return render_template("site/index.html")


@site_.route("about")
def about():
    return render_template("site/about.html")


@site_.route("blog")
def blog():
    return render_template("site/blog.html")


# Site Files Access
@site_.route("css/<cssfile>")
def css_link(cssfile):
    return send_from_directory(os.path.join("statics/site/css"), cssfile)


@site_.route("<path:path>/<fontfile>")
def font_link(path, fontfile):
    return send_from_directory(os.path.join("statics/site/fonts", path), fontfile)

@site_.route("js/<jsfile>")
def js_link(jsfile):
    return send_from_directory(os.path.join("statics/site/js"), jsfile)

@site_.route("/images/<path:path>/<imagefile>")
def image_link(path, imagefile):
    return send_from_directory(os.path.join("statics/images", path), imagefile)
