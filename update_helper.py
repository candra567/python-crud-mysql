def updateData(database):
	statusUpdate=True 
	while statusUpdate:
			first_name=input("Masukan first name = ")
			last_name=input("Masukan last name  =  ")
			id_person=input("Masukan id yang akan diedit = ")
			if first_name =="" and last_name =="" and id_person=="": 
				pass 
			else :
				try:
					db=database.update((first_name,last_name,id_person))
					if(db>0):
						print("Data berhasil diperbarui")
						statusUpdate=False
					else :
						print("Tidak ada data yang diperbarui")
				except Exception as e:
					print(e)