#عمل تجربة لمحاسبة الصنايعي بالمتر الواحد
#سنأخذ منه الطول
str_Length = input("Please type Lenght : \n")
#العرض
str_width = input("Please type width : \n")
#تكلفة المتر الواحد
str_price = input("How much for 1 meter? : \n")
#سنحفظهم علي هيئة ارقام عشريه
Length = float(str_Length)
width = float(str_width)
price = float(str_price)
#نستخرج المساحه (الطول*العرض)
area = Length * width
total_price = area * price
str_area = str(area)
str_total_price = str(total_price)
print("the total area is: " + str_area)
print("Give the guy : $" + str_total_price )
