import mysql.connector
class Database():
	def __init__(self):
		self.host="127.0.0.1"
		self.user="root"
		self.password="root"
		self.database="py_crud"
		self.conn=None  
		self.cursor=None
	def connect(self):
		self.conn=mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
		self.cursor=self.conn.cursor()
	def all(self):
		self.cursor.execute("SELECT * FROM table_person")
		return self.cursor.fetchall()
	def find(self,id):
	    self.cursor.execute(f"SELECT * FROM table_person WHERE id_person={id}")	
	    return self.cursor.fetchall()
	def insert(self,data):
		self.cursor.execute("INSERT INTO table_person (first_name,last_name) VALUES (%s,%s)",data)
		self.conn.commit()
		return self.cursor.lastrowid
	def destory(self,id):
		self.cursor.execute(f"DELETE FROM table_person WHERE id_person={id}")
		self.conn.commit()
		return self.cursor.rowcount
	def update(self,data):
		self.cursor.execute("UPDATE table_person SET first_name=%s,last_name=%s WHERE id_person =%s",data)
		self.conn.commit()
		return self.cursor.rowcount
	def close(self):
		self.conn.close()
	



app=Database()
app.connect()