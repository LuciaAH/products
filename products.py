
products = []

# 讀取檔案
# 若無檔案則無法讀取檔案
with open('products.csv', 'r') as f:
		# with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])

print('q=離開')
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

# 寫入檔案
with open('products.csv', 'w') as f:
		# with open('products.csv', 'w', encoding='utf-8') as f:
		# encoding:為了修正亂碼問題, 用utf-8通用的編碼語言
	# f.write('商品,價格\n')
	# 若新建檔案, 加上商品, 價格, 若已建立則可移除
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
