# 2520  is the smallest number that can be divided by each of the numbers from 
#  1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 
# 1 to 20 ?
import math

def find_smallest_multiple():
    result = 1
    for i in range(1, 21):
        result = (result * i) // math.gcd(result, i)
    return result
#  Her bir adımda yeni bir sayı eklenerek EKOK güncellenir ve sonunda 1'den 20'ye kadar olan tüm sayılara tam bölünebilen en küçük sayı elde edilmiş olur.
result = find_smallest_multiple()
print(result)

