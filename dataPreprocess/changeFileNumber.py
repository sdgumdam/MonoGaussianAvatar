import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('_vtoonify_t.jpg'):
            new_name = filename.replace('_vtoonify_t.jpg', '.jpg')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

if __name__ == "__main__":
    directory = '/root/autodl-tmp/monogaussianavatar/data/yufeng/yufeng/MVI_1814_style/image/'
    rename_files(directory)