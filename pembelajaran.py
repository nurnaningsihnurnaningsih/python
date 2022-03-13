#STATMENT DAN VARIABLE
#variable = tempat menyimpan data sementara
#a = 5 
#b = 6.0
#c = "nilai saya"
#d = a+b
#print (a+b)
#print (c+str(d))
#======================================================
#Seleksi Kondisi
# memilih suatu kondisi yang terpenuhi
#n = int(input("masukan Nilai: ")) #menerima input dari keyboard, kemudian casting ke interger
#if(n > 0):
	#print("nilai: "+str(n))
#else:
	#print("nilai: "+str(0))
#======================================================
#input n = 0-100
#A: 85-100
#B: 70-84
#C: 60-69
#D:<60
#n= int(input("masukan nilai : "))
#if (>85 and n<=100)
	#print ("Nilai A")
#elif(n>=70 and n<=84):
	#print("Nilai B ")
#elif(n<=60 and n<=69):
	#print ("Nilai C")
#elif (n<=60 and n>0):
	#print ("Nilai D")
#else:
	#print ("salah")
#=======================================================
#perulangan
#n = int(input("nilai : "))
#i = 0 #variable bantu i, insialiasi =0
#while(i < n): #perintah pengulangan while 
    #print("nilai"+str(i))
    #i=i+1
#print("Selesai")
#======================================================
#menentukan faktor bilangan
#algoritma
#1. terima N, ubah jadi int
#2. buat perulangan dari 1...N
#3. setiap perulangan, akan di cek apakah N = 1 %0, jika iya maka i adalah faktor dari N
#n = int(input("Masukan Nilai: "))
#for i in range(1, n+1):
    #if(n%i==0):
        #print(str(i)+" adalah faktor dar "+str(n))

#buatlah program menentukan ganjil genap
#1. terima n, ubah jadi int
#2. buat perulangan 1...n
#3. setiap perulangan, akan dicek apakah 1 %2 ==0, jika iya maka i genap
#n = int(input("masukan nilai: "))
#i = 1
#while(i <= n): 
    #if(i%2==0): #% adalah modulo, sisa habis bagi
        #print(str(i)+ " adalah genap ")
    #else:
        #print(str(i)+ " adalah ganjil")
    #i=i+1
#===================================================

