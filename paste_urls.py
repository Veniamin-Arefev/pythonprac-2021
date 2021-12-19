# Created by Veniamin_arefev
import sys
import subprocess
import os
import os.path

test_folder_name = "tests"
url_file_name = "URLS"

excluded_tasks = {"20210916": ["1", "2", "3"], "20211014": ["2"]}

prefix_to_write = ["https://github.com/Uberariy/pythonprac/tree/main",
                   "https://github.com/stamplevskiyd/pythonprac-2021/tree/main",
                   "https://git.cs.msu.ru/s02190141/pythonprac-2021/-/tree/main"]

print(sys.argv)

main_url = sys.argv[1:][0]

subprocess.run(["git", "clone", main_url, "main_repo"])

dirs = [i for i in os.listdir("main_repo") if os.path.isdir(i) and str.isdigit(i)]
for homework_dir in dirs:  # each folder in one homework
    cur_path = "main_repo" + os.sep + homework_dir
    ex_numbers = [i for i in os.listdir(cur_path) if
                  os.path.isdir(cur_path + os.sep + i) and str.isdigit(i)]
    for ex_number in ex_numbers:
        if homework_dir in excluded_tasks:
            if ex_number in excluded_tasks[homework_dir]:
                continue
        # print(f"try to open:  {cur_path}{os.sep}{ex_number}{os.sep}{url_file_name}")
        with open(f"{cur_path}{os.sep}{ex_number}{os.sep}{url_file_name}", mode='w', encoding="utf-8") as urls_file:
            text = [f"{i}/{homework_dir}/{ex_number}/{test_folder_name}" for i in prefix_to_write]
            urls_file.write("\n".join(text))
