def deleteData(database):
	statusDelete=True  
	while statusDelete: 
			id_person=input("Masukan id person yang akan dihapus = ")
			if id_person == "":
				statusDelete=True  
			else :
				statusDelete=False
				db=database.destory(id_person)
				if db > 0:
					print("Data berhasil dihapus")
				else :
					print("Tidak ada data yang dihapus")