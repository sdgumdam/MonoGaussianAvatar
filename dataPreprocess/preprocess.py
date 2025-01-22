import os
from PIL import Image

def scale_images(input_folder, output_folder, size=(512, 512)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('_vtoonify_t.jpg')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.resize(size, Image.ANTIALIAS)
            img.save(os.path.join(output_folder, filename))

if __name__ == "__main__":
    input_folder = '/root/autodl-tmp/styleData/results_sub1_1812/'
    output_folder = '/root/autodl-tmp/styleData/output_1812/'
    scale_images(input_folder, output_folder)