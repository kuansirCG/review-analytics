# 讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		count += 1 # count = count +1
		if count % 1000 == 0: # 1000的倍數
			print (len(data))

print ('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print ('每筆留言平均長度是', sum_len/len(data))