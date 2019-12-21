10 i=i+1
20 if i=1 then load "data1",8,1

100 i=49152
110 sign=peek(i)
120 i=i+1
130 if sign=0 then goto 400
140 if sign=43 then sign=1
150 if sign=45 then sign=-1
160 n=0

200 d=peek(i)
210 i=i+1
220 if d=10 then goto 300
230 n=n*10+(d-48)
240 goto 200

300 n=n*sign
310 sum=sum+n
320 print "n="+str$(n)+"  sum="+str$(sum)
330 goto 110

400 print
410 print "solution="+str$(sum)
