import os
from flask import Flask, send_from_directory, render_template, redirect
from config import config
from modules.callData import blogData


app = Flask(__name__)

#Site Routes
@app.route("/")
def home():
    return render_template("site/index.html")


@app.route("/about")
def about():
    return render_template("site/about.html")


@app.route("/blog")
def blog():
    return render_template("site/blog.html")

#Site Files Access
@app.route("/css/<cssfile>")
def css_link(cssfile):
    return send_from_directory(os.path.join("templates/site/css"), cssfile)


@app.route("/images/<imagefile>")
def image_link(imagefile):
    return send_from_directory(os.path.join("templates/site/images"), imagefile)


@app.route("/<path:path>/<fontfile>")
def font_link(path, fontfile):
    return send_from_directory(os.path.join("templates/site/fonts", path), fontfile)


@app.route("/scss/<scssfile>")
def scss_link(scssfile):
    return send_from_directory(os.path.join("templates/site/scss"), scssfile)


@app.route("/js/<jsfile>")
def js_link(jsfile):
    return send_from_directory(os.path.join("templates/site/js"), jsfile)

#Admin Routes
@app.route("/admin/")
def admin():
    return render_template("admin/base.html")


@app.route("/admin/blog")
def admin_blog():
    return render_template("admin/blog.html")


@app.route("/admin/blog/save", methods=["POST"])
def admin_blog_save():
    blogData()
    return redirect("/admin/blog")


@app.route("/admin/index")
def admin_index():
    return render_template("admin/starter.html")

#Admin Files Access
@app.route("/admin/dist/js/<adminjsfile>")
def adminjs_link(adminjsfile):
    return send_from_directory(os.path.join("templates/admin/dist/js"), adminjsfile)


@app.route("/admin/dist/css/<admincssfile>")
def admincss_link(admincssfile):
    return send_from_directory(os.path.join("templates/admin/dist/css"), admincssfile)


@app.route("/admin/dist/img/<adminimgfile>")
def adminimg_link(adminimgfile):
    return send_from_directory(os.path.join("templates/admin/dist/img"), adminimgfile)


@app.route("/admin/plugins/<path:path>/<adminpluginfile>")
def adminplugin_link(path, adminpluginfile):
    return send_from_directory(
        os.path.join("templates/admin/plugins", path), adminpluginfile
    )


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()
