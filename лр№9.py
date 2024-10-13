import os

def create_file(filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            while True:
                line = input("Введіть рядок (або натисніть Enter для завершення): ")
                if line == "":
                    break
                file.write(line + '\n')
        print(f"Файл {filename} успішно створено.")
    except IOError as e:
        print(f"Помилка при створенні файлу {filename}: {e}")

def process_files(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            content = infile.read()
            counter = 1
            index = 0
            while index < len(content):
                chunk = content[index:index+counter]
                outfile.write(chunk + '\n')
                index += counter
                counter = (counter % 10) + 1
        print(f"Файл {output_file} успішно створено на основі {input_file}.")
    except IOError as e:
        print(f"Помилка при обробці файлів: {e}")

def print_file_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"Вміст файлу {filename}:")
            for line in file:
                print(line.strip())
    except IOError as e:
        print(f"Помилка при читанні файлу {filename}: {e}")

def main():
    input_file = "TF12_1.txt"
    output_file = "TF12_2.txt"

    create_file(input_file)
    process_files(input_file, output_file)
    print_file_contents(output_file)

if __name__ == "__main__":
    main()