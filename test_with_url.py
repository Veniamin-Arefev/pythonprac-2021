# Created by Veniamin_arefev
import sys
import subprocess
import os
import os.path

test_folder_name = "tests"

excluded_tasks = {"20210916": ["1", "2", "3"], "20211014": ["2"]}

print(sys.argv)

checker_url, main_url, target_url = sys.argv[1:]
print(checker_url, main_url, target_url)

subprocess.run(["git", "clone", main_url, "main_repo"])
subprocess.run(["git", "clone", target_url, "target_repo"])

dirs = [i for i in os.listdir("main_repo") if os.path.isdir(i) and str.isdigit(i)]
for homework_dir in dirs:  # each folder in one homework
    cur_path = "main_repo" + os.sep + homework_dir
    ex_numbers = [i for i in os.listdir(cur_path) if
                  os.path.isdir(cur_path + os.sep + i) and str.isdigit(i)]
    for ex_number in ex_numbers:
        if homework_dir in excluded_tasks:
            if ex_number in excluded_tasks[homework_dir]:
                continue
        executable = \
            [i for i in os.listdir(cur_path + os.sep + ex_number) if i.endswith('.py')][0]
        argums = ["python", checker_url, "main_repo" + os.sep + homework_dir + os.sep + ex_number + os.sep + executable,
                  "target_repo" + os.sep + homework_dir + os.sep + ex_number + os.sep + test_folder_name]
        # print(*argums)
        print(f"Testing {homework_dir} dir task number {ex_number}")
        subprocess.run(argums)
