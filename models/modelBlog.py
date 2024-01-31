from .entities.Blog import Blog


class ModelBlog:
    @classmethod
    def create_blog_post(cls, db, data):
        try:
            connect = db.connect()
            cursor = connect.cursor()
            sql = "INSERT INTO blog (id, title, content, image, user, date_of_creation, last_modification) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, data)
            connect.commit()
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
            connect.close()

