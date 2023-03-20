def printData(data):
	if(len(data)<1):
		print("=== Data Masih Kosong ===")
	else :
		print("=== Data Person ===")
		for item in data : 
			print(item[0],"-",item[1],"-",item[2])