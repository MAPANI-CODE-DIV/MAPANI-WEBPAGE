from src.database.mysql import get_connection

class ModelBlog:
    @classmethod
    def create_blog_post(cls,blog):
        try:
            connect = get_connection()
            cursor = connect.cursor()
            sql = """INSERT INTO `blog` (`id`, `title`, `content`, `image`, `username`, 
            `date_of_creation`, `last_modification`) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            data = (
                blog.id,
                blog.title,
                blog.content,
                blog.image,
                blog.username,
                blog.date_of_creation,
                blog.last_modification)
            cursor.execute(sql, data)
            connect.commit()
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()
            connect.close()

