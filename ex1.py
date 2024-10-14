import requests
import re
import os

url = "https://gsom.spbu.ru/en/"
headers = {'Accept-Encoding': 'identity'}
r = requests.get(url, headers=headers)

parsed_site = r.text
counted_images = parsed_site.count(".png")
print(f"Number of PNG images: {counted_images}")

first_png_match = re.search(r'templates/[^\s]+?\.png', parsed_site, re.IGNORECASE)

print(first_png_match)
if first_png_match:
    first_png_url = first_png_match.group(0)
    print(f"First PNG link found: {first_png_url}")

img_response = requests.get(f"https://gsom.spbu.ru/{first_png_url}", headers=headers)
if img_response.status_code == 200:
    if not os.path.exists('images'):
        os.makedirs('images')

img_path = os.path.join('images', 'downloaded_image.png*')
with open(img_path, 'wb') as img_file:
    img_file.write(img_response.content)
print(f"Image saved as: {img_path}")