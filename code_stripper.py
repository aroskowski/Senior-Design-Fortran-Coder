import os
import re

def strip_comments(code):
    comment_pattern = re.compile(r'!.*?$|(?<!\w)C.*?$|(?<!\w)D.*?$', re.MULTILINE)
    code_without_comments = re.sub(comment_pattern, '', code)
    return code_without_comments

def process_file(file_path, dataset_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code_content = file.read()
        code_without_comments = strip_comments(code_content)
        dataset_file_path = os.path.join(dataset_path, f"{os.path.basename(file_path)}_stripped.f90")
        with open(dataset_file_path, 'w', encoding='utf-8') as dataset_file:
            dataset_file.write(code_without_comments)
        comments_file_path = os.path.join(dataset_path, f"{os.path.basename(file_path)}_comments.txt")
        with open(comments_file_path, 'w', encoding='utf-8') as comments_file:
            comments_file.write(code_content)

def main():
    directory_path = '/home/knuchol1/CS425/cs425-env/CS402/fortran-utils/src'
    dataset_path = '/home/knuchol1/CS425/cs425-env/CS402/datasets/dataset1'
    os.makedirs(dataset_path, exist_ok=True)
    code_files = [file for file in os.listdir(directory_path) if file.endswith('.f90')]

    for code_file in code_files:
        code_file_path = os.path.join(directory_path, code_file)
        process_file(code_file_path, dataset_path)

if __name__ == "__main__":
    main()
