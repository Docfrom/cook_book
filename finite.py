# Задача №3. Пукнт1

files = ["1.txt", "2.txt", "3.txt"]

file_data = []

for file_name in files:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        file_data.append(
            {"name": file_name, "line_count": len(lines), "content": lines}
        )

file_data.sort(key=lambda x: x["line_count"])

result_file_name = "result.txt"
with open(result_file_name, "w", encoding="utf-8") as result_file:
    for file_info in file_data:
        result_file.write(f"{file_info['name']}\n" f"{file_info['line_count']}\n")

        result_file.write("".join(file_info["content"]))

print(f"Итоговый файл сохранен как {result_file_name}")

# Задача №3. Пункт2

files = ['1.txt', '2.txt', '3.txt']
file_data = []

for file_len in files:
    with open(file_len, 'r', encoding='utf-8') as file:
        lines = len(file.readlines())
        file_data.append({'name': file_len, 'line_count': lines})

def print_file_info(file_data):
    for file_info in file_data:
        print(f"{file_info['name']}: {file_info['line_count']} строк")
print_file_info(file_data)