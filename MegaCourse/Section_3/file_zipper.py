from datetime import datetime

data_list = ["file1.txt", "file2.txt", "file3.txt"]

def file_append(data):
    target_file_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
    with open(target_file_name, "w") as target_file:
        for source_file_path in data:
            with open(source_file_path) as source_file:
                target_file.write(source_file.read() + "\n")

file_append(data_list)
