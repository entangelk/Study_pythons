s1,s2,s3,s4,s5 = 1,'',2,'',3
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))

s2=s1
s1=""
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))

s4=s3
s3=''
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))

s3=s5
s5=''
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))

s1=s3
s3=''
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))

s3=s4
s4=''
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))

s4=s2
s2=''
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))

s5=s4
s4=''
print("{} {} {} {} {}" .format(s1,s2,s3,s4,s5))