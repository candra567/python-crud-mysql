def insertData(database):
	statusInsert=True 
	while statusInsert:
			first_name=input("Insert first name = ")
			last_name=input("Insert last name  =  ")
			if first_name =="" and last_name =="": 
				pass 
			else :
				try:
					db=database.insert((first_name,last_name))
					statusInsert=False
					if(db>0):
						print("Data berhasil ditambahkan")
				except Exception as e:
					print(e)