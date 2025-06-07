from PIL import Image
import os

def convert_webp_to_jpg(root_dir='.'):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.webp'):
                webp_path = os.path.join(foldername, filename)
                jpg_path = os.path.splitext(webp_path)[0] + '.jpg'

                try:
                    with Image.open(webp_path) as img:
                        rgb_img = img.convert('RGB')  # 确保是 RGB 格式
                        rgb_img.save(jpg_path, 'JPEG')
                    print(f"✅ Converted: {webp_path} → {jpg_path}")
                except Exception as e:
                    print(f"❌ Failed to convert {webp_path}: {e}")

if __name__ == '__main__':
    convert_webp_to_jpg('.')
