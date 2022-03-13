# 檢查檔案在不在
import os #operating system作業系統

products = []

def read_file(filename):
	# 檢查檔案在不在
	if os.path.isfile(filename):
		print('Yeah!找到檔案了!')
	# 讀取檔案
	# 若無檔案則無法讀取檔案
		with open(filename, 'r') as f:
			# with open('products.csv', 'r', encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
	else:
		print('找不到檔案......')
	return products

# 輸入商品
def input_product(products):
	print('q=離開')
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		products.append([name, price])
	print(products)
	return products

# 寫入檔案
def write_file(filename):
	with open(filename, 'w') as f:
		# with open('products.csv', 'w', encoding='utf-8') as f:
		# encoding:為了修正亂碼問題, 用utf-8通用的編碼語言
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

products = read_file('products.csv')
products = input_product(products)
write_file('products.csv')