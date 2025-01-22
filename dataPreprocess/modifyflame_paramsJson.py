import json
import os

def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def save_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

def get_image_prefixes(image_folder):
    prefixes = set()
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            prefix = os.path.splitext(filename)[0]
            prefixes.add(f'./image/{prefix}')
    return prefixes

def filter_flames(json_data, prefixes):
    filtered_flames = [frame for frame in json_data['frames'] if frame['file_path'] in prefixes]
    json_data['frames'] = filtered_flames
    return json_data

def main(json_path, image_folder, output_json_path):
    json_data = load_json(json_path)
    prefixes = get_image_prefixes(image_folder)

    filtered_data = filter_flames(json_data, prefixes)
    save_json(filtered_data, output_json_path)

if __name__ == "__main__":
    json_path = '/root/autodl-tmp/monogaussianavatar/data/yufeng/yufeng/MVI_1810/flame_params.json'
    image_folder = '/root/autodl-tmp/monogaussianavatar/data/yufeng/yufeng/MVI_1810_style/image/'
    output_json_path = '/root/autodl-tmp/monogaussianavatar/data/yufeng/yufeng/MVI_1810_style/flame_params.json'
    main(json_path, image_folder, output_json_path)