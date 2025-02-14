def circumference(r):
    return 2 * 3.14159 * r
    
    
def area(r):
    return 3.14159 * (2**r)
  

redius = int(input("Enter the Radius: "))

result1 = circumference(redius)
result2 = area(redius)

print(f"the circumference of the circle is = {result1}")
print(f"the area of the circle is = {result2}")






