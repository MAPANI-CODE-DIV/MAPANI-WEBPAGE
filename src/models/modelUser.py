from .entities.User import User
from src.database.mysql import get_connection

class ModelUser:

    @classmethod
    def login(self, user):
        try:
            connect= get_connection()
            cursor= connect.cursor()
            sql="""SELECT id, firstname, lastname, username, email, password, created_at, 
            updated_at, role FROM user WHERE email = '{}'""".format(user.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], row[3], row[4], User.check_password(row[5], user.password), row[6], row[7], row[8])
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_id(self, id):
        try:
            connect= get_connection()
            cursor= connect.cursor()
            sql="""SELECT id, firstname, lastname, username, email, created_at, 
            updated_at, role FROM user WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user=User(row[0], row[1], row[2], row[3], row[4], None, row[5], row[6], row[7])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
