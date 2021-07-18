import time
iseconds = int(time.time())

passed_y = iseconds//(60*60*24*360)
passed_m = iseconds//(60*60*24*30)
passed_d = iseconds//(60*60*24)

y = 1970 + passed_y
m = 1 + passed_m - passed_y*12
d = 1 + passed_d - passed_y*360 - (m-1)*30

print(str(y)+'/'+str(m)+'/'+str(d))