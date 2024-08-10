import os
from PIL import Image, ImageFilter, ImageEnhance

def manipulate_image(input_path, output_path):
    try:
        # Memuat gambar
        image = Image.open(input_path)
        print("✅ Gambar berhasil dimuat")

        # Direktori output
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"✅ Direktori '{output_dir}' berhasil dibuat")

        # Operasi Cropping dengan validasi ukuran
        if image.width > 200 and image.height > 200:
            cropped_image = image.crop((10, 10, 200, 200))
            cropped_image_path = os.path.join(output_dir, 'cropped_result.jpg')
            cropped_image.save(cropped_image_path)
            print("✅ Cropping berhasil")
        else:
            raise ValueError("Gambar terlalu kecil untuk di-crop ke ukuran 200x200")

        # Operasi Resizing dengan rasio aspek yang dipertahankan
        resized_image = cropped_image.resize((100, 100), Image.Resampling.LANCZOS)
        resized_image_path = os.path.join(output_dir, 'resized_result.jpg')
        resized_image.save(resized_image_path)
        print("✅ Resizing berhasil")

        # Operasi Filtering
        filtered_image = resized_image.filter(ImageFilter.BLUR)
        filtered_image_path = os.path.join(output_dir, 'filtered_result.jpg')
        filtered_image.save(filtered_image_path)
        print("✅ Filtering berhasil")

        # Operasi Pengaturan Kecerahan
        enhancer = ImageEnhance.Brightness(filtered_image)
        bright_image = enhancer.enhance(1.5)
        bright_image_path = os.path.join(output_dir, 'bright_result.jpg')
        bright_image.save(bright_image_path)
        print("✅ Pengaturan kecerahan berhasil")

        # Operasi Penggabungan Gambar
        combined_image = Image.blend(filtered_image, bright_image, alpha=0.5)
        combined_image_path = os.path.join(output_dir, 'combined_result.jpg')
        combined_image.save(combined_image_path)
        print("✅ Penggabungan gambar berhasil")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # Jalur input dan output yang benar
    manipulate_image('images/example.jpg', 'images/result.jpg')
