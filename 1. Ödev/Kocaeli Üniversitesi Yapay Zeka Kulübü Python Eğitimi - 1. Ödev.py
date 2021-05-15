# 1. Kısım
number = input("Tek mi çift mi diye kontrol etmem için bir sayı giriniz ")
if(int(number)%2==0):
      print("Merhaba seçtiğiniz sayı {number0} \nVe seçtiğiniz {number0} sayısı tektir.".format(number0=number))
else:
      print("Merhaba seçtiğiniz sayı {number0} \nVe seçtiğiniz {number0} sayısı tektir.".format(number0=number))


# 2. Kısım
print("Sırayla 5 adet asal sayı giriniz")
for i in range (5):
  primenumber=int(input("Asal sayınızı giriniz."))
  if primenumber > 1:
   
   for i in range(2,primenumber):
       if (primenumber % i) == 0:
           print(primenumber," Asal Sayı Değildir.")
           break
   else:
       print(primenumber," Asal Sayıdır.")
 
  else:
   print(primenumber," Asal Sayı Değildir.")


#3. Kısım
first_str = "Ah5me4t"
result0 = ''.join([i for i in first_str if not i.isdigit()])
second_str = "M9eHm4eT"
result1 = ''.join([i for i in second_str if not i.isdigit()])
third_str = "Ha3K5a1n"
result2 = ''.join([i for i in third_str if not i.isdigit()])
print(result0,result1,result2,sep="-")
