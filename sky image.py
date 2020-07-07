import numpy as np

def hms2dec(hms) :
	h = hms[0].split("h")
	m = hms[1].split("m")
	try:
		s = hms[2].split("s")
		return 15*(float(h[0]) + float(m[0])/60 + float(s[0])/3600)
	except:
		s = 0
		return 15*(float(h[0]) + float(m[0])/60 + float(s)/3600)

def dms2dec(d,m,s) :
	return (d/abs(d))*(abs(d) + m/60 + s/3600)

def angular_dist(r1, d1, r2, d2) :
	r1 = np.radians(r1)
	r2 = np.radians(r2)
	d1 = np.radians(d1)
	d2 = np.radians(d2)
	a = np.sin((d1-d2)/2)**2
	b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
	d = 2*np.arcsin(np.sqrt(a + b))
	return np.degrees(d)


f = open("Messier-objects-details-Sheet1-2.csv")
data = list()
for i,line in enumerate(f) :
	if i == 0 :	continue
	d = line.strip().split(",")
	ra = hms2dec(d[3].split())
	data.append( [ int(d[0]), d[1], d[2], ra, float(d[4]), float(d[5]) ] )
print(data)
