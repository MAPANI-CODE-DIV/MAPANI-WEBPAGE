import os
from flask import (
    Flask,
    send_from_directory,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    session,
)
from flask_wtf.csrf import CSRFProtect
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)


from config import config
from datetime import datetime
from flaskext.mysql import MySQL
from flask_wtf.csrf import CSRFProtect
from models.entities.User import User
from models.entities.Blog import Blog
from models.modelUser import ModelUser
from models.modelBlog import ModelBlog

# Models

# Entities

app = Flask(__name__)
db = MySQL(app)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


# Load configuration
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_id(db, id)


# Site Routes
@app.route("/")
def home():
    return render_template("site/index.html")


@app.route("/about")
def about():
    return render_template("site/about.html")


@app.route("/blog")
def blog():
    return render_template("site/blog.html")


# Site Files Access
@app.route("/css/<cssfile>")
def css_link(cssfile):
    return send_from_directory(os.path.join("statics/site/css"), cssfile)


@app.route("/<path:path>/<fontfile>")
def font_link(path, fontfile):
    return send_from_directory(os.path.join("statics/site/fonts", path), fontfile)


@app.route("/scss/<scssfile>")
def scss_link(scssfile):
    return send_from_directory(os.path.join("statics/site/scss"), scssfile)


@app.route("/js/<jsfile>")
def js_link(jsfile):
    return send_from_directory(os.path.join("statics/site/js"), jsfile)


# Admin Routes
@app.route("/admin/")
def admin():
    return render_template("admin/base.html")


@app.route("/admin/blog")
def admin_blog():
    return render_template("admin/blog.html")


@app.route("/admin/blog/save", methods=["POST"])
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
        
    ModelBlog.create_blog_post(db, data)

    return render_template("admin/blog.html")


@app.route("/protected")
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login_save():
    print(db)

    if request.method == "POST":
        user = User(
            0,
            "",
            "",
            "",
            request.form["email"],
            request.form["password"],
            "",
            "",
            "",
        )
        print(request.form["password"])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)

                return redirect(url_for("home"))
            else:
                flash("Invalid Password")
                return render_template("admin/login.html")
        else:
            flash("User not Found")
            return render_template("admin/login.html")
    else:
        return render_template("admin/login.html")


@app.route("/admin/index")
def admin_index():
    return render_template("admin/login.html")


# Admin Files Access
@app.route("/admin/dist/<path:path>/<admindistfile>")
def admindist_link(path, admindistfile):
    return send_from_directory(os.path.join("statics/admin/dist", path), admindistfile)


@app.route("/admin/plugins/<path:path>/<adminpluginfile>")
def adminplugin_link(path, adminpluginfile):
    return send_from_directory(
        os.path.join("statics/admin/plugins", path), adminpluginfile
    )


# Images
@app.route("/images/<path:path>/<imagefile>")
def image_link(path, imagefile):
    return send_from_directory(os.path.join("statics/images", path), imagefile)


if __name__ == "__main__":
    app.config.from_object(config["development"])
    csrf.init_app(app)
    db.init_app(app)
    app.run()
