from flask import request
from datetime import datetime
import database as db


def blogData():
    _actualDate = datetime.now()
    _title = request.form["txtTitle"]
    _content = request.form["txtContent"]
    print(_content)
    _image = request.files["txtImage"]
    sql = "INSERT INTO `blog` (`id_`, `title_`, `content_`, `image_`, `user_`, `date_of_creation_`) VALUES (NULL,%s,%s,%s,'@pepe',%s);"
    data = (_title, _content, _image.filename, _actualDate)
    connect = db.database.connect()
    cursor = connect.cursor()
    cursor.execute(sql, data)
    connect.commit()
    
db.database.init_app(db.db)
    
