from database_mysql import app
from util_print import printData
from title_text import printTitle
from insert_helper import insertData
from update_helper import updateData
from delete_helper import deleteData


printTitle()


statusPrompt=True  
while statusPrompt :
	inputUser=input("Masukan no pilihan : ").strip()
	if inputUser =="": 
		print("Maaf belum memasukan pilihan !")
	elif inputUser=="1":
		data=app.all()
		printData(data)
	elif inputUser=="2":
		insertData(app)
	elif inputUser =="3":
		updateData(app)
	elif inputUser == "4":
		deleteData(app)
	elif inputUser =="5":
		statusPrompt=False
		app.close()
	else :
		print("Maaf input anda tidak valid sampai jumpa lagi")
		statusPrompt=False
		app.close()
