import random

a=0
b=0
for i in range(1,101):
    a+=i**2

for j in range(1,101):
    b+=j


b_sonuc=b**2

print(f"{b_sonuc-a}")

