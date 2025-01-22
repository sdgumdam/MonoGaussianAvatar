import os
import shutil
import sys
def get_image_number(filename):
    return ''.join(filter(str.isdigit, filename.split('_')[0]))

def copy_corresponding_images(folder_a, folder_b, folder_c):
    if not os.path.exists(folder_c):
        os.makedirs(folder_c)

    images_a = os.listdir(folder_a)
    images_b = os.listdir(folder_b)

    for image_a in images_a:
        number_a = get_image_number(image_a)
        for image_b in images_b:
            number_b = get_image_number(image_b)
            if number_a == number_b:
                shutil.copy(os.path.join(folder_b, image_b), os.path.join(folder_c, image_b))
                break

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python GetCorrepodingImage.py <number>")
        sys.exit(1)

    number = sys.argv[1]

    styledImageFolder = f'/root/autodl-tmp/styleData/output_{number}/'
    originalDataFolder = f'/root/autodl-tmp/monogaussianavatar/data/yufeng/yufeng/MVI_{number}/'
    styleTrainDataFolder = f'/root/autodl-tmp/monogaussianavatar/data/yufeng/yufeng/MVI_{number}_style/'

    if not os.path.exists(styleTrainDataFolder):
        os.makedirs(styleTrainDataFolder)

    subFolders = ['image','mask','semantic_color','semantic']

    for subFolder in subFolders:
        copy_corresponding_images(styledImageFolder, originalDataFolder+f'{subFolder}/', styleTrainDataFolder+f'{subFolder}/')