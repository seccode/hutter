import tqdm

if __name__=="__main__":
	b=open("b","r").read()
	B=len(b)
	del b

	ds=[
	"0",
	"01",
	"1000",
	"0100",
	"0010",
	"0001",
	"0011",
	"1001",
	"10000",
	"01000",
	"00100",
	"00010",
	"00001",
	"11000",
	"01100",
	"00110",
	"00011",
	"10100",
	"01010",
	"00101",
	"100000",
	"010000",
	"001000",
	"000100",
	"000010",
	"000001",
	"100100",
	"010010",
	"001001",
	"101000",
	"010100",
	"001010",
	"000101",
	"110000",
	"011000",
	"001100",
	"000110",
	"000011",
	"1000000",
	"0100000",
	"0010000",
	"0001000",
	"0000100",
	"0000010",
	"0000001",
	"1100000",
	"0110000",
	"0011000",
	"0001100",
	"0000110",
	"0000011",
	]
	v=[0]*B
	for d in tqdm.tqdm(ds):
		print(d)
		x=d*int(B/len(d))
		c=0
		for i in tqdm.tqdm(range(len(x))):
			v[i]+=x[i]
			if x[i]==b[i]:
				c+=1
		print(c/B)

	D=len(ds)
	acc=0
	for i in range(B):
		v[i]/=D
		if (v[i]>0.5 and b[i]=="1") or (v[i]<0.5 and b[i]=="0"):
			acc+=1
	print(acc/B)
