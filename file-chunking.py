'''
Best practice to load large files
'''

def chunk_file():
    with open("file_dummy.txt", "r") as f:
        while content := f.read(1024):
            '''
            := can be used to assign variables within loop or conditions
            '''
            yield content

def load_file():
    for chunk in chunk_file():
        print(chunk)

load_file()