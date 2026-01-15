
import numpy as np
from PIL import Image

def simulate_deuteranopia(image_path):
    print(f"Simülasyon hazırlanıyor: {image_path}...")
    img = Image.open(image_path)
    img = img.convert('RGB')
    rgb_array = np.array(img, dtype=float)
    rgb_to_lms = np.array([
        [17.8824, 43.5161, 4.11935],
        [3.45565, 27.1554, 3.86714],
        [0.0299566, 0.184309, 1.46709]
    ])
    lms_blind_matrix = np.array([
        [1, 0, 0],              
        [0.494207, 0, 1.24827], 
        [0, 0, 1]               
    ])

    try:
        lms_to_rgb = np.linalg.inv(rgb_to_lms)
    except np.linalg.LinAlgError:
        print("Matris hatası! Numpy sürümünü kontrol et.")
        return

    lms_image = np.dot(rgb_array, rgb_to_lms.T)
    simulated_lms = np.dot(lms_image, lms_blind_matrix.T)
    final_rgb = np.dot(simulated_lms, lms_to_rgb.T)
    final_rgb = np.clip(final_rgb, 0, 255).astype('uint8')

    result_img = Image.fromarray(final_rgb)
    result_img.show()
    save_name = image_path.replace(".jpg", "_simulasyon.jpg").replace(".png", "_simulasyon.jpg")
    result_img.save(save_name)
    print(f"✅ Simülasyon bitti! Şu dosya oluşturuldu: {save_name}")

if __name__ == "__main__":
   simulate_deuteranopia("corrected_output.jpg")