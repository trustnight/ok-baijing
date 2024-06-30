import os

def is_text_file(file_path):
    text_file_extensions = ['.txt', '.py', '.log', '.csv', '.json', '.xml', '.html', '.css', '.js']
    _, ext = os.path.splitext(file_path)
    return ext.lower() in text_file_extensions

def search_text_in_folder(folder_path, search_text):
    found_files = []
    search_text_lower = search_text.lower()  # 将搜索文本转换为小写
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_text_file(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                        if search_text_lower in file_content.lower():  # 将文件内容转换为小写并进行比较
                            found_files.append(file_path)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    return found_files

while True:
    folder_path = 'E:\\Desktop\\ok-baijing-1.3.28'  # 替换为你的文件夹路径
    search_text = input('要查找的内容：')

    found_files = search_text_in_folder(folder_path, search_text)

    if found_files:
        print(f"在如下文件里找到 '{search_text}':")
        for file in found_files:
            relative_path = os.path.relpath(file, folder_path)
            print(relative_path)
    else:
        print(f"没有文件包含 '{search_text}' 。")