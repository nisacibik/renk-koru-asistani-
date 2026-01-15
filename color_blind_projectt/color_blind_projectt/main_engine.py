import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import time

def apply_kmeans_reduction(image_path, k=8):
    print(f"Resim yükleniyor... Hedef renk sayısı (k): {k}")

    original_img = Image.open(image_path)
    original_img = original_img.convert('RGB')
    w, h = original_img.size
    resize_ratio = 400 / w
    small_w, small_h = int(w * resize_ratio), int(h * resize_ratio)
    img_small = original_img.resize((small_w, small_h))

    image_array = np.array(img_small)
    pixel_list = image_array.reshape(-1, 3)

    print("Yapay zeka (K-Means) renkleri öğreniyor... (Bu işlem 5-10 saniye sürebilir)")
    start_time = time.time()
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(pixel_list)

    end_time = time.time()
    print(f"Öğrenme tamamlandı! Süre: {end_time - start_time:.2f} saniye.")


    labels = kmeans.labels_
    quantized_pixels = new_colors[labels]
    quantized_image_array = quantized_pixels.reshape((small_h, small_w, 3))

    result_img = Image.fromarray(quantized_image_array)
    result_img = result_img.resize((w, h), Image.NEAREST)
    result_img.show()
    result_img.save(f"kmeans_result_k{k}.jpg")
    print("✅ İşlem bitti! Sadeleştirilmiş resim kaydedildi.")

if __name__ == "__main__":
    apply_kmeans_reduction("images/elma.png", k=8)