# -->format waktu sekarang
# import datetime
# now=datetime.datetime.now()
# print("saat ini adalah :",now)
# print("""
# senin
# ARSITEKTUR KOMPUTER
# 07:30 - 10:00
# HYR-Hardiansya Saiyar.ST.M,Kom
#"""")
# -->format waktu sekarang dengan sesuai keinginan
from datetime import *
skrng= datetime.now()
tglskrng=str(skrng.day) + '/' + str(skrng.month)+ '/' + str(skrng.year)
print('tanggal sekarang :', tglskrng)

#penggunaan dunction today
from datetime import  *
tody=datetime.today()
print('saat ini adalah:',tody)

#jam menit detik
from datetime import *
sek=datetime.now()
print('\nsaat ini adalah  : ',sek)
print('sekarang tahun   :',sek.year)
print('sekarang bulan   :',sek.month)
print('sekarang tanggal :',sek.day,'\n')
print('sekarang jam     :',sek.hour)
print('sekarang menit   :',sek.minute)
print('sekarang detik   :',sek.second)


