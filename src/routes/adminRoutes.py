import os
from flask import (
    send_from_directory,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    Blueprint,
)
from datetime import datetime
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)

from src.models.entities.Blog import Blog
from src.models.modelBlog import ModelBlog
from src.services.AuthUser import authenticate_user



admin_ = Blueprint("admin_blueprint", __name__, template_folder='templates')




@admin_.route("/")
def admin():
    return render_template("admin/base.html")

@admin_.route("/login", methods=["GET", "POST"])
def login():
    success, message = authenticate_user()
    if success:
        return redirect(url_for("admin_blueprint.admin"))
    elif message=="Void":
        return render_template("admin/login.html")
    else:
        flash(message)
        return render_template("admin/login.html")
 
    

@admin_.route("/blog")
@login_required
def admin_blog():
    return render_template("admin/blog.html")


@admin_.route("/blog/save", methods=["POST"])
@login_required
def admin_blog_save():
    data = Blog(
        None,
        request.form["txtTitle"],
        request.form["txtContent"],
        request.files["txtImage"].filename,
        current_user.username,
        datetime.now(),
        datetime.now(),
    )
    ModelBlog.create_blog_post(data)
    return redirect(url_for("admin_blueprint.admin"))


@admin_.route("/index")
def admin_index():
    return render_template("admin/login.html")


# Admin Files Access
@admin_.route("/dist/<path:path>/<admindistfile>")
def admindist_link(path, admindistfile):
    return send_from_directory(os.path.join("statics/admin/dist", path), admindistfile)


@admin_.route("/plugins/<path:path>/<adminpluginfile>")
def adminplugin_link(path, adminpluginfile):
    return send_from_directory(
        os.path.join("statics/admin/plugins", path), adminpluginfile
    )


@admin_.route("/images/<path:path>/<imagefile>")
def image_link(path, imagefile):
    return send_from_directory(os.path.join("statics/admin/images", path), imagefile)
