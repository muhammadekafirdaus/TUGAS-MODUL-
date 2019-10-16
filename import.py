import geometri2D
def main():
	p = 10
	l = 8 
	luas = geometri2D.luasPersegiPanjang(p,l)
	kel = geometri2D.kelilingPersegiPanjang(p,l)
	print("PERSEGI PANJANG")
	print("Panjang\t: ",p)
	print("Lebar\t: ",l)
	print("Luas\t: ",luas)
	print("keliling\t: ",kel)

	jarijari=3

	luas = geometri2D.luasLingkaran(jarijari)
	kel = geometri2D.kelilingLingkaran(jarijari)

	print("\nLINGKARAN")
	print("Jari-jari\t: ",jarijari)
	print("Luas\t: ",luas)
	print("keliling\t: ",kel)
if __name__ == '__main__':
	main()