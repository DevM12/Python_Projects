with open('my_file.txt') as file:
    data = file.read()
    data = data.replace('world', ' Sheesh')
    clean_lines = [line[:-1] if line.endswith("\\") else line for line in data]
with open('my_file.txt', 'w') as file:
    file.write(data)
print(file)