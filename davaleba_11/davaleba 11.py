# დავალება 1
def create_numbered_file():
    with open('1000_lines.txt', 'w', encoding='utf-8') as file:
        for i in range(1, 1001):
            file.write(f"Line {i}: This is line number {i}\n")


    # წაკითხვა და ხაზების დათვლა
    with open('1000_lines.txt', 'r', encoding='utf-8') as file:
        lines = len(file.readlines())
        print(f"Number of lines in file: {lines}")

create_numbered_file()


# დავალება 2
def create_numbered_text_file():
    numbers_text = {
        2: "ორი",
        8: "რვა",
        10: "ათი",
        13: "ცამეტი",
        17: "ჩვიდმეტი"
    }

    with open('task2.txt', 'w', encoding='utf-8') as file:
        for i in range(1, 18):
            if i in numbers_text:
                file.write(f"{numbers_text[i]}\n")
            else:
                file.write("\n")

create_numbered_text_file()

# დავალება 3
def merge_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r', encoding='utf-8') as f1, \
            open(file2_path, 'r', encoding='utf-8') as f2, \
            open(output_path, 'w', encoding='utf-8') as output:
        output.write(f1.read())
        output.write(f2.read())

    # წაკითხვა და დაბეჭდვა
    with open(output_path, 'r', encoding='utf-8') as file:
        print(file.read())

merge_files('1000_lines.txt', 'task2.txt', 'merged.txt')

# დავალება 4
def find_palindrome_lines(file_path):
    def is_palindrome(text):
        text = text.lower().strip()
        return text == text[::-1]

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines) - 1):
            if is_palindrome(lines[i]) and is_palindrome(lines[i + 1]):
                print(f"Palindrome pair found:\n{lines[i]}{lines[i + 1]}")

find_palindrome_lines('1000_lines.txt')

# დავალება 5
def split_file_into_chunks(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = 10
    for i in range(0, len(lines), chunk_size):
        chunk = lines[i:i + chunk_size]
        with open(f'chunk_{i // chunk_size + 1}.txt', 'w', encoding='utf-8') as output:
            output.writelines(chunk)

split_file_into_chunks('task2.txt')

# დავალება 6
def remove_empty_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # ცარიელი ხაზების ამოშლა
    non_empty_lines = [line for line in lines if line.strip()]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(non_empty_lines)

remove_empty_lines('task2.txt', 'stripped.txt')

