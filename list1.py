data = []
with open('reviews.txt.crdownload', 'r') as f:
	for line in f:
		data.append(line)

good = []
for d in data :
	if 'good' in d :
		good.append(d)
print('總共有', len(good), '筆資料符合good')


#快寫法 list comprehension
#      運算   變數  清單     條件
good = [d for d in data if 'good' in d]
print(good)

		



	