# 讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		count += 1 # count = count +1
		if count % 1000 == 0: # 1000的倍數
			print (len(data))

print (len(data))

print (data[0])
print ('--------------')
print (data[1])
