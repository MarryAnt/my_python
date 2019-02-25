s = "У лукоморья 123 дуб зеленый 456"
print(s.find("я"))
print(s.count("у"))
if s.isalpha() == 0:
    print(s.upper())
if len(s) >= 4:
    print(s.lower())
print(s.replace(s[0],"О"))
