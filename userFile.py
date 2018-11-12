from connection import connection

class UserModel:
    def getstring(username):
        return 'User model return value %s' % username


    def usernamepasswordmatch(username, password):
        with connection.cursor() as cur:
            rows_count = cur.execute("select * from user where username = '" + username + "' and password = '" + password + "' LIMIT 0,1")
            cur.close()
            return rows_count

    def CheckUserExsist(username, password):
        with connection.cursor() as cur:
            cur.execute(
                "select * from user where username = '" + username + "' and password = '" + password + "'")
            data = cur.fetchone()
            cur.close()
            return data
