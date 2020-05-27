def verificaPrimo(valor):
	for i in range(3, int(valor/2) ):
		if(valor%i==0):
			return False
	return True

def atualizaArquivoPrimos(valor):
	f = open("primos.txt", 'a')
	f.write(str(valor)+"\n")
	f.close()

def atualizaLastNumber(valor):
	f = open("lastNumber.txt", 'w')
	f.write(str(valor))
	f.close()

f=open('lastNumber.txt', 'r')
c=f.read()
f.close()
if c=="":
	c=1
else:
	c=int(str(c))+2

if c<=2:
	c=2
	f=open("primos.txt", 'w')
	f.write(str(c)+"\n")
	f.close()
	c=3

while True:
	if verificaPrimo(c):
		print("Primo encontrado: ", c)
		atualizaArquivoPrimos(c)
	atualizaLastNumber(c)	

	c+=2
	print("Avaliando numero: ", c)