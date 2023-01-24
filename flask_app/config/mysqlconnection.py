import pymysql.cursors
# a cursor is the object we use to interact with the database


class MySQLConnection:
# this class will give us an instance of a connection to our database

    def __init__(self, db):
    # constructor for class
    # change the user and password as needed
        connection = pymysql.connect(host = 'dbs-do-user-13382922-0.b.db.ondigitalocean.com',
                                    user = 'rootroot', 
                                    password = 'AVNS_GRC_TNpvv8fmBgYEiA0', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    ssl_ca='/home/coder/template-app/ca-certificate.crt',
                                    port='25060',
                                    autocommit = True)
        self.connection = connection
		# this connection = connection from constructor

    
    def query_db(self, query, data=None):
	# query="UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s,
	# email=%(email)s, password=%(password)s WHERE id=%(id)s"
	# return connectToMySQL(cls.db).query_db(query,data)
	
        with self.connection.cursor() as cursor:
		# this instance of cursor object set AS cursor variable

            try:
			# check to see if query=""
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query, data)

                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid

                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database 
                    result = cursor.fetchall()
                    return result

                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()

            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False

            finally:
                # close the connection
                self.connection.close() 

# connectToMySQL receives the database we're using and uses it to create an 
def connectToMySQL(db):
    return MySQLConnection(db)