def start(): #fungsi ok
	print("="*50)
	print("="*10 + " "*7 + " Menghitung Luas"  + " "*7 + "="*10)
	print("="*22 + " Menu " + "="*22)
	nama = ['Segitiga','Lingkaran','Persegi','Persegi Panjang','Trapesium','Keluar']
	j=1
	for i in nama: #perulangan ok
		print("[%d]. %s" % (j,i))
		j+=1

	angka = int(input("Masukkan pilihannmu :"))

	if angka == 1: #pecabangan ok
		_main(nama[0],'alas','tinggi')
	elif angka == 2:
		_main(nama[1],'jari-jari')
	elif angka == 3:
		_main(nama[2],'sisi 1','sisi 2')
	elif angka == 4:
		_main(nama[3],'panjang','lebar')
	elif angka == 5:
		_main(nama[4],'sisi 1','sisi 2','tinggi')
	elif angka == 6:
		keluar()

def keluar():
	print("Thank You :)")
	exit()

def _main(tipe,s1,s2 = 'null', s3 = 'null'):
	nama = ['Segitiga','Lingkaran','Persegi','Persegi Panjang','Trapesium','Keluar']
	
	for i in range(0,len(nama)):
		if tipe == nama[i]:
			print("Menghitung Luas " +tipe)
			a = int(input("Masukkan nilai %s : " %(s1)))
			
			if s2 != 'null':
				b = int(input("Masukkan nilai %s : " %(s2)))

			if s2 != 'null' and s3 != 'null':
				c = int(input("Masukkan nilai %s : " %(s3)))

		
			if s2 == 'null' and s3 == 'null':
				print("Luas %s yaitu : " %(tipe) ,lingkaran(a), "\n"); #tipe data ok
			elif s3 == 'null':
				print("Luas %s yaitu : " %(tipe) ,duasisi(a,b,tipe), "\n");
			else:
				print("Luas %s yaitu : " %(tipe) ,trapesium(a,b,c), "\n");

	repeat = str(input("Ingin menghitung lagi?(Y/N) : "))
	if repeat == "Y" or repeat == 'y':
		start()
	else:
		keluar()

def duasisi(s1,s2,j):
	if j == "Segitiga":
		return s1*s2/2 #pemanggilan variable ok
	else:
		return s1*s2

def lingkaran(r):
	if r % 7 == 0:
		pi = 22/7
	else:
		pi = 3.14

	return pi*r**2

def trapesium(s1,s2, t):
	return (s1+s2)*t/2; 


start()