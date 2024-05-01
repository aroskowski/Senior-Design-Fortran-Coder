import os

def concatenate_files(directory_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name in os.listdir(directory_path):
            if file_name.endswith('_stripped.f90') or file_name.endswith('_comments.txt'):
                file_path = os.path.join(directory_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    output.write(content)
                    output.write('\n')  
def main():
    dataset_path = '/home/knuchol1/CS425/cs425-env/CS402/datasets'
    output_file = '/home/knuchol1/CS425/cs425-env/CS402/datasetsoutput_file.txt'
    concatenate_files(dataset_path, output_file)

if __name__ == "__main__":
    main()
