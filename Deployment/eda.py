import os
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# Fungsi untuk menampilkan distribusi kategori
def plot_category_distribution(data_dir):
    """
    Membuat plot distribusi jumlah gambar per kategori.
    Args:
        data_dir (str): Path ke folder dataset.
    """
    categories = os.listdir(data_dir)
    counts = [len(os.listdir(os.path.join(data_dir, category))) for category in categories]

    st.write("### Distribusi Gambar per Kategori")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(categories, counts, color=['#FFB6C1', '#ADD8E6', '#FFDEAD', '#DDA0DD'])
    ax.set_title("Distribusi Gambar per Kategori")
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Jumlah Gambar")
    st.pyplot(fig)
    
    st.write('''
             Dari grafik batang (bar chart) dan diagram pie (pie chart), terlihat bahwa distribusi data untuk setiap kategori (Bus, Car, Motorcycle, dan Truck) adalah seimbang, masing-masing memiliki jumlah gambar yang sama, yaitu 100 gambar atau 25% dari total dataset.
             ''')

# Fungsi untuk menampilkan contoh gambar
def show_sample_images(data_dir):
    """
    Menampilkan contoh gambar dari setiap kategori.
    Args:
        data_dir (str): Path ke folder dataset.
    """
    categories = os.listdir(data_dir)
    st.write("### Contoh Gambar dari Setiap Kategori")
    cols = st.columns(len(categories))

    for col, category in zip(cols, categories):
        img_path = os.path.join(data_dir, category, os.listdir(os.path.join(data_dir, category))[0])
        img = Image.open(img_path)
        with col:
            st.image(img, caption=category, use_column_width=True)
            
    # Menambahkan deskripsi untuk setiap kategori kendaraan
    st.write("Karakteristik masing-masing kategori kendaraan :")

    # Deskripsi untuk setiap kategori kendaraan
    st.write('---')
    
    # **1. Bus**
    st.write("**1. Bus**")
    st.write("**Ukuran dan Bentuk**:")
    st.write("   - Biasanya besar dan panjang, dengan bentuk persegi panjang yang menonjol.")
    st.write("   - Memiliki jendela yang berbaris di sisi kendaraan.")
    st.write("**Ciri Khas**:")
    st.write("   - Pintu besar, biasanya di bagian samping atau depan.")
    st.write("   - Beberapa bus memiliki warna yang mencolok (namun hal ini tergantung pada tipe bus, seperti bus sekolah atau bus transportasi umum).")
    st.write("**Fitur Visual**:")
    st.write("   - Ban besar dengan jumlah lebih dari 4 (biasanya 6 atau lebih).")
    st.write("   - Bagian depan lebar dengan kaca besar.")

    st.write('---')

    # **2. Car**
    st.write("**2. Car**")
    st.write("**Ukuran dan Bentuk**:")
    st.write("   - Lebih kecil dibanding bus atau truck.")
    st.write("   - Memiliki dua atau empat pintu, serta satu bagasi.")
    st.write("**Ciri Khas**:")
    st.write("   - Kap depan yang rendah dan kaca depan dengan sudut lebih landai.")
    st.write("   - Tersedia dalam berbagai warna dan desain.")
    st.write("**Fitur Visual**:")
    st.write("   - Ban kecil (biasanya 4 buah).")
    st.write("   - Tidak memiliki fitur tambahan besar seperti trailer atau bak terbuka.")

    st.write('---')

    # **3. Motorcycle**
    st.write("**3. Motorcycle**")
    st.write("**Ukuran dan Bentuk**:")
    st.write("   - Kendaraan kecil dengan dua roda.")
    st.write("   - Memiliki desain minimalis dibandingkan dengan kategori yang lain.")
    st.write("**Ciri Khas**:")
    st.write("   - Rangka kecil dengan kursi untuk satu atau dua orang.")
    st.write("   - Dilengkapi setang kemudi dan tidak memiliki kabin.")
    st.write("**Fitur Visual**:")
    st.write("   - Terdapat dua ban (depan dan belakang).")
    st.write("   - Memiliki knalpot yang menonjol dan lampu depan kecil.")

    st.write('---')

    # **4. Truck**
    st.write("**4. Truck**")
    st.write("**Ukuran dan Bentuk**:")
    st.write("   - Ukurannya besar, tetapi lebih bervariasi dibanding bus.")
    st.write("   - Biasanya memiliki bak terbuka di belakang untuk membawa barang.")
    st.write("**Ciri Khas**:")
    st.write("   - Dilengkapi kabin depan untuk pengemudi.")
    st.write("**Fitur Visual**:")
    st.write("   - Ban besar (biasanya lebih dari 4).")
    st.write("   - Bak terbuka atau kontainer yang terlihat jelas di bagian belakang.")
             
# Fungsi untuk menampilkan distribusi ukuran gambar
def plot_image_size_distribution(data_dir):
    """
    Membuat histogram distribusi ukuran gambar (width dan height).
    Args:
        data_dir (str): Path ke folder dataset.
    """
    img_sizes = []
    categories = os.listdir(data_dir)

    for category in categories:
        category_path = os.path.join(data_dir, category)
        for img_name in os.listdir(category_path):
            img_path = os.path.join(category_path, img_name)
            img = Image.open(img_path)
            img_sizes.append(img.size)

    st.write("### Distribusi Ukuran Gambar (Width dan Height)")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist([size[0] for size in img_sizes], bins=20, alpha=0.7, label='Width', color='blue')
    ax.hist([size[1] for size in img_sizes], bins=20, alpha=0.7, label='Height', color='orange')
    ax.set_title("Distribusi Ukuran Gambar")
    ax.set_xlabel("Pixels")
    ax.set_ylabel("Frekuensi")
    ax.legend(loc='upper right')
    st.pyplot(fig)
    
    # Insight terkait distribusi ukuran gambar
    st.write("1. **Mayoritas Gambar Berukuran Kecil**:")
    st.write("   - Sebagian besar gambar memiliki ukuran (lebar dan tinggi) di bawah **2000 piksel**.")
    st.write("2. **Ada Beberapa Gambar Berukuran Besar**:")
    st.write("   - Beberapa gambar memiliki resolusi tinggi hingga **4000–8000 piksel**.")
    st.write("3. **Ukuran Gambar Bervariasi**:")
    st.write("   - Gambar memiliki ukuran yang tidak seragam (beragam lebar dan tinggi).")

# Fungsi utama untuk menjalankan aplikasi Streamlit
def run():
    """
    Fungsi utama untuk menjalankan aplikasi Streamlit.
    """
    st.title("EDA - Vehicle Dataset")
    st.write("Aplikasi ini melakukan eksplorasi data awal (EDA) pada dataset kendaraan.")

    # Path ke dataset
    data_dir = "vehicle_dataset/Dataset"  # Pastikan path dataset benar

    if os.path.exists(data_dir):
        st.success(f"Dataset ditemukan di: `{data_dir}`")
        plot_category_distribution(data_dir)
        show_sample_images(data_dir)
        plot_image_size_distribution(data_dir)
    else:
        st.error(f"Folder dataset `{data_dir}` tidak ditemukan. Periksa kembali path.")

# Panggil fungsi `run()` ketika script dijalankan
if __name__ == "__main__":
    run()