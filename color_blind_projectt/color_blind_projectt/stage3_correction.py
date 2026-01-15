import cv2  # Görüntü işleme kütüphanesi
import numpy as np

def apply_color_correction(image_path):
    print(f"--- SENİN GÖREVİN BAŞLADI: Renk Düzeltme ---")
    print(f"İşlenen dosya: {image_path}")
    
    # 1. Resmi Oku
    img = cv2.imread(image_path)
    
    if img is None:
        print("HATA: Resim bulunamadı! Lütfen 'kmeans_result_k8.jpg' dosyasının oluştuğundan emin ol.")
        return
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask_red1 | mask_red2
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    hsv[:, :, 2] = np.where(mask_red == 255, np.minimum(hsv[:, :, 2] + 60, 255), hsv[:, :, 2])
    hsv[:, :, 2] = np.where(mask_green == 255, np.maximum(hsv[:, :, 2] - 60, 0), hsv[:, :, 2])

    corrected_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    save_name = "corrected_output.jpg"
    cv2.imwrite(save_name, corrected_img)
    
    print("-" * 30)
    print(f"✅ İŞLEM BAŞARILI!")
    print(f"Oluşturulan dosya: {save_name}")
    print("Kırmızılar parlatıldı, yeşiller koyulaştırıldı.")
    print("-" * 30)

if __name__ == "__main__":
    apply_color_correction("kmeans_result_k8.jpg")