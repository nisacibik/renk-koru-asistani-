# 👁️ Yapay Zeka Destekli Renk Körlüğü Asistanı

Bu proje, özellikle **Döteranopi** (Kırmızı-Yeşil renk körlüğü) yaşayan bireylerin, dijital görsellerdeki renk farklarını daha net algılayabilmesi için geliştirilmiş bir yardımcı araçtır.

## 🚀 Projenin Amacı
Renk körü bireyler için birbirine çok yakın görünen renkleri (özellikle kırmızı ve yeşil), görüntü işleme ve makine öğrenmesi teknikleriyle ayrıştırarak görsel erişilebilirliği artırmak.

## 🛠️ Teknik Özellikler
Proje üç ana aşamadan oluşmaktadır:
1.  **Renk Körlüğü Simülasyonu:** Görüntüyü LMS renk uzayına dönüştürerek renk körü birinin görüşünü taklit eder.
2.  **K-Means Renk Sadeleştirme:** Görüntüdeki karmaşıklığı azaltmak için renkleri `k=8` kümesine indirger.
3.  **Dinamik Renk İyileştirme:** HSV uzayında maskeleme yaparak kırmızının parlaklığını artırır, yeşili ise koyulaştırarak kontrast farkı yaratır.

## 📦 Kullanılan Teknolojiler
* **Python**
* **Streamlit** (Web arayüzü)
* **OpenCV** (Görüntü işleme ve renk uzayı dönüşümleri)
* **Scikit-learn** (K-Means algoritması)
* **NumPy** (Matris işlemleri)
* **Pillow** (Görüntü yönetimi)

## 💻 Kurulum ve Çalıştırma

1. Projeyi klonlayın:
   ```bash
   git clone [https://github.com/nisacibik/renk-koru-asistani.git](https://github.com/nisacibik/renk-koru-asistani.git)
