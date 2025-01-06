'''Этот скрипт собирает все файлы с указанным расширением из указанной директории проекта (и её подкаталогов),
за исключением папки .venv (или других указанных).
Для каждого найденного файла скрипт добавляет его содержимое в файл вывода (project_summary.txt).
В вывод добавляются разделители с указанием относительного пути к файлу. В итоге скрипт создаёт текстовый файл,
который содержит весь исходный код проекта, игнорируя определённые папки.'''

import os


def collect_files(project_path, output_file):
    exclude_dirs = {'.venv'}  # Укажите папки, которые нужно исключить

    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                if file.endswith(('.py')):  # Укажите нужные расширения Например: '.py', '.html', '.css', '.js' и т.д.
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, project_path)
                    out.write(f"\n\n{'=' * 80}\n")
                    out.write(f"Файл: {relative_path}\n")
                    out.write(f"{'=' * 80}\n")
                    with open(file_path, 'r', encoding='utf-8') as f:
                        out.write(f.read())
    print(f"Все файлы собраны в {output_file}")


project_directory = os.getcwd() # Автоматическое получение текущей директории, откуда запускается скрипт
# или укажите вручную путь к проекту Например:  project_directory = '/home/user/myproject'
output_filename = 'project_summary.txt'

collect_files(project_directory, output_filename)
