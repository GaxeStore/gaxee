import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def create_pdf():
    buffer = io.BytesIO()
    
    p = canvas.Canvas(buffer, pagesize=letter)
    tes = 670
    p.drawString(235, 730, "GA XE CORPORATION")
    p.drawString(160, 715, "JL. BERSAMAMU TAK SEMULUS ITU NO. 2, MALANG")
    p.drawString(240, 700, "TELP. 081-2345-6789")
    p.drawString(20, 690, "------------------------------------------------------------------------------------------------------------------------------------------------")
    for item, count in st.session_state.count.items():
        if count > 0:
            if item in options_makan:
                harga = options_makan[item]["Harga"]
            elif item in options_minum:
                harga = options_minum[item]["Harga"]
            elif item in options_merchan:
                harga = options_merchan[item]["Harga"]
            p.drawString(50, tes, f"{item}: {count}")
            p.drawString(500, tes, f"{harga}")  
            tes -= 15
    tes -= 5
    p.drawString(20, tes, "------------------------------------------------------------------------------------------------------------------------------------------------")
    tes -= 15
    p.drawString(260, tes, f"TOTAL: {st.session_state.total}")
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer

if 'total' not in st.session_state:
    st.session_state.total = 0

if 'show_cart' not in st.session_state:
    st.session_state.show_cart = False


if 'milih' not in st.session_state:
    st.session_state.milih = []

if 'count' not in st.session_state:
    st.session_state.count = {  
        "Coklat Kunafa": 0,
        "Roti Bakar": 0,
        "Pencake": 0,
        "Brownies": 0,
        "Choco Lava": 0,
        "Golden Waffle": 0,
        "Paket Velvet Delight": 0,
        "Paket Golden Indulgence": 0,
        "Paket Arabian Touch": 0,
        "Hot Chocolate Classic": 0,
        "Chocolate Milkshake": 0,
        "Iced Mocha Supreme": 0,
        "Choco Float Bliss": 0,
        "Choco Banana Smoothie": 0,
        "Affogato Noir": 0,
        "Paket Choco Fusion": 0,
        "Paket Mocha Affair": 0,
        "Paket Banana Brezee": 0,
        "Tumbler Choco Luxe": 0,
        "Mug Velvet": 0,
        "Tote bag Chocoa Carry": 0,
        "Kaos Choco Vibe": 0,
        "Apron Choco Craft": 0,
        "Notebook Mocha Note": 0,
        "Paket Chocoa Starter": 0,
        "Paket Barista Set": 0,
        "Paket Choco Lifestle": 0
    }

options_makan = {
    "Coklat Kunafa": {"Harga": 28000, "gambar": "Asset/coklat.PNG"},
    "Roti Bakar": {"Harga": 20000, "gambar": "Asset/rokar.PNG"},  
    "Pencake": {"Harga": 24000, "gambar": "Asset/pencake.PNG"},
    "Brownies": {"Harga": 30000, "gambar": "Asset/brownies.PNG"},
    "Choco Lava": {"Harga": 28000, "gambar": "Asset/lava.PNG"},
    "Golden Waffle": {"Harga": 25000, "gambar": "Asset/waffle.PNG"},
    "Paket Velvet Delight": {"Harga": 42000, "gambar": "Asset/1a.PNG"},
    "Paket Golden Indulgence": {"Harga": 50000, "gambar": "Asset/1b.PNG"},
    "Paket Arabian Touch": {"Harga": 45000, "gambar": "Asset/arto.PNG"}
}

options_minum = {
    "Hot Chocolate Classic": {"Harga": 20000, "gambar": "Asset/ori.PNG"},
    "Chocolate Milkshake": {"Harga": 24000, "gambar": "Asset/choco.PNG"},  
    "Iced Mocha Supreme": {"Harga": 26000, "gambar": "Asset/ice.PNG"},
    "Choco Float Bliss": {"Harga": 25000, "gambar": "Asset/float.PNG"},
    "Choco Banana Smoothie": {"Harga": 26000, "gambar": "Asset/bnn.PNG"},
    "Affogato Noir": {"Harga": 28000, "gambar": "Asset/aff.PNG"},
    "Paket Choco Fusion": {"Harga": 46000, "gambar": "Asset/float1.PNG"},
    "Paket Mocha Affair": {"Harga": 52000, "gambar": "Asset/aff1.PNG"},
    "Paket Banana Brezee": {"Harga": 44000, "gambar": "Asset/bnn1.PNG"}
}

options_merchan = {
    "Tumbler Choco Luxe": {"Harga": 120000, "gambar": "Asset/tumbler.PNG"},
    "Mug Velvet": {"Harga": 90000, "gambar": "Asset/mug.PNG"},  
    "Tote bag Chocoa Carry": {"Harga": 75000, "gambar": "Asset/totebag.PNG"},
    "Kaos Choco Vibe": {"Harga": 150000, "gambar": "Asset/baju.PNG"},
    "Apron Choco Craft": {"Harga": 130000, "gambar": "Asset/apron.PNG"},
    "Notebook Mocha Note": {"Harga": 85000, "gambar": "Asset/notebook.PNG"},
    "Paket Chocoa Starter": {"Harga": 180000, "gambar": "Asset/tumbler1.PNG"},
    "Paket Barista Set": {"Harga": 200000, "gambar": "Asset/barista.PNG"},
    "Paket Choco Lifestle": {"Harga": 320000, "gambar": "Asset/baju1.PNG"}
}


kategori = st.sidebar.radio("Pilih Kategori", ["Beranda","Makanan", "Minuman", "Merchandise"])

if kategori == "Beranda":
    col1, col2, col3 = st.columns([1,7,1])
    with col2:
        st.image("Asset/welcome.png")

if kategori == "Makanan":
    st.title("Makanan")
    index = 0
    for row in range(3):
        cols = st.columns(3) 
        for col in range(3):
            if index < len(options_makan):  
                option, details = list(options_makan.items())[index]
                with cols[col]: 
                    st.image(details["gambar"], caption=option)

                    if st.button(f"Tambah {option} 1"):
                        st.session_state.milih.clear()
                        st.session_state.total += details['Harga']
                        st.session_state.count[option] += 1 
                        st.sidebar.write(option, st.session_state.count[option])

                    if st.button(f"Kurang {option} 1"):
                        if st.session_state.count[option] > 0:
                            st.session_state.total -= details['Harga']
                            st.session_state.count[option] -= 1 
                            st.sidebar.write(option, st.session_state.count[option])
                            st.session_state.milih.clear()
                        elif st.session_state.count[option] == 0:
                            st.error("Masih pesan 0")
                index += 1

elif kategori == "Minuman":
    st.title("Minuman")
    index = 0
    for row in range(3):
        cols = st.columns(3) 
        for col in range(3):
            if index < len(options_minum):  
                option, details = list(options_minum.items())[index]
                with cols[col]: 
                    st.image(details["gambar"], caption=option)

                    if st.button(f"Tambah {option} 1"):
                        st.session_state.milih.clear()
                        st.session_state.total += details['Harga']
                        st.session_state.count[option] += 1 
                        st.sidebar.write(option, st.session_state.count[option])

                    if st.button(f"Kurang {option} 1"):
                        if st.session_state.count[option] > 0:
                            st.session_state.total -= details['Harga']
                            st.session_state.count[option] -= 1 
                            st.sidebar.write(option, st.session_state.count[option])
                            st.session_state.milih.clear()
                        elif st.session_state.count[option] == 0:
                            st.error("Masih pesan 0")
                index += 1

elif kategori == "Merchandise":
    st.title("Merchandise")
    index = 0
    for row in range(3):
        cols = st.columns(3) 
        for col in range(3):
            if index < len(options_merchan):  
                option, details = list(options_merchan.items())[index]
                with cols[col]: 
                    st.image(details["gambar"], caption=option)

                    if st.button(f"Tambah {option} 1"):
                        st.session_state.milih.clear()
                        st.session_state.total += details['Harga']
                        st.session_state.count[option] += 1 
                        st.sidebar.write(option, st.session_state.count[option])

                    if st.button(f"Kurang {option} 1"):
                        if st.session_state.count[option] > 0:
                            st.session_state.total -= details['Harga']
                            st.session_state.count[option] -= 1 
                            st.sidebar.write(option, st.session_state.count[option])
                            st.session_state.milih.clear()
                        elif st.session_state.count[option] == 0:
                            st.error("Masih pesan 0")
                index += 1




if st.sidebar.button("Lihat Belanjaan"):
    st.session_state.show_cart = True 
    st.session_state.milih.clear()
    for item, count in st.session_state.count.items():
        if count > 0:
            if item in options_makan:
                harga = options_makan[item]["Harga"]
            elif item in options_minum:
                harga = options_minum[item]["Harga"]
            elif item in options_merchan:
                harga = options_merchan[item]["Harga"]

            st.session_state.milih.append(f"{item} x{count} : {harga}")

if st.session_state.show_cart and st.session_state.milih:
    if st.sidebar.button("Buat Pesanan"):
        pdf_buffer = create_pdf()
        st.sidebar.download_button(
            label="Download Struk",
            data= pdf_buffer,
            file_name="Struk Ga Xe.pdf",
            mime="application/pdf"
        )

if st.session_state.show_cart and st.session_state.milih:
    st.sidebar.write("Pilihan Anda:")
    for selected in st.session_state.milih:
        st.sidebar.write(selected)

st.sidebar.write("Total: ", st.session_state.total)