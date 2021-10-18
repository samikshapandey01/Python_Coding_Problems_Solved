#2(a)
import re
string_1="An email was sent from student@sjsu.edu to inquiries@gmail.com"
print(f"String: {string_1}")
y = re.findall('\w+@([a-zA-Z]+)\.[a-zA-Z]{3}', string_1)
print(f"Domain names: {y}")

#2(b)
string_2="An email was went by emily to rob yesterday afternoon"
print(f"\nString: {string_2}")
y2=re.findall('\\b[aeiouAEIOU][a-zA-Z]+\\b',string_2)
print(f"Words starting with vowels: {y2}")

#2(c)
print(f"\nString: {string_2}")
y3=re.findall('\\b[a-zA-Z]{5,7}\\b',string_2)
print(f"Words between 5-7 alphabet long: {y3}")

#2(d)
s  = "Hello my cell numbers are 408-123-4567 , 123-459-6789, 1234567800, (123) 456-7890, 123 459 6780 1#32#32456789 70309907222361"
print(f"\nString: {s}")
y4=re.findall('\\b\d{3}-\d{3}-\d{4}\\b|\\b\d{10}\\b|\(\d{3}\) ?\d{3}-\d{4}\\b',s)
print(f"All Phone numbers in desired format: {y4}")