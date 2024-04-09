import json

def name_extractor(file_path):
    # Split the filePath based on '/'
    parts = file_path.split('/')
    
    # Get the last part of the path
    file_name_with_extension = parts[-1]
    
    # Remove the ".png" extension
    file_name_without_extension = file_name_with_extension.replace('.png', '')
    
    return file_name_without_extension

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        print('File created', file_path, 'and content written successfully.')

file_path = 'valid.json'

with open(file_path, 'r') as file:
    data = file.read()

json_data = json.loads(data)

for key in json_data:
    img_name = name_extractor(key)
    img_num = img_name.split('.')[0]

    print(img_num)
    vehicles = json_data[key]['vehicles']
    array = []
    for vehicle in vehicles:
        x1 = int(vehicle['AABB']['x1'])/2464
        y1 = int(vehicle['AABB']['y1'])/2056
        x2 = int(vehicle['AABB']['x2'])/2464
        y2 = int(vehicle['AABB']['y2'])/2056
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        width = x2 - x1
        height = y2 - y1
        array.append(f"0 {mid_x} {mid_y} {width} {height}")

    write_to_file("valid/" + img_name + '.txt', '\n'.join(array))