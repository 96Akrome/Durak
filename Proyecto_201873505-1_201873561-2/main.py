import os,time 

os.system('clear')
start_screen = ['start1.txt','start2.txt']
frames = []

for s in start_screen:
	with open(s,"r",encoding = "utf8") as f:
		frames.append(f.readlines())
for i in range(10):
	for fr in frames:
		print("".join(fr))
		time.sleep(1)
		os.system('clear')
