products = []
print('q=離開')
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

with open('products.csv', 'w') as f:
		# with open('products.csv', 'w', encoding='utf-8') as f:
		# encoding:為了修正亂碼問題, 用utf-8通用的編碼語言
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
