import streamlit as st

# Inisialisasi halaman
if "page" not in st.session_state:
    st.session_state.page = "home"

# Fungsi pindah halaman
def goto(page):
    st.session_state.page = page

# ================================
# Halaman Home
# ================================
if st.session_state.page == "home":
    st.title("Aplikasi Multi-Fitur dengan Streamlit")
    st.write("Pilih salah satu fitur di bawah:")

    st.button("🔢 Kalkulator Sederhana", on_click=lambda: goto("kalkulator"))
    st.button("🌡️ Konversi Suhu", on_click=lambda: goto("suhu"))
    st.button("🔢 Deret Fibonacci", on_click=lambda: goto("fibonacci"))

# ================================
# Halaman Kalkulator
# ================================
elif st.session_state.page == "kalkulator":
    st.header("🔢 Kalkulator Sederhana")

    num1 = st.number_input("Masukkan angka pertama:", value=0.0, key="num1")
    num2 = st.number_input("Masukkan angka kedua:", value=0.0, key="num2")

    operator = st.selectbox("Pilih operator:", ["+", "-", "×", "÷"])

    if st.button("Hitung", key="hitung"):
        if operator == "+":
            hasil = num1 + num2
        elif operator == "-":
            hasil = num1 - num2
        elif operator == "×":
            hasil = num1 * num2
        elif operator == "÷":
            hasil = num1 / num2 if num2 != 0 else "Error: Pembagian dengan nol!"
        else:
            hasil = "Operator tidak valid"
        st.success(f"Hasil: {hasil}")

    st.button("⬅️ Kembali", on_click=lambda: goto("home"))

# ================================
# Halaman Konversi Suhu
# ================================
elif st.session_state.page == "suhu":
    st.header("🌡️ Konversi Suhu")

    suhu = st.number_input("Masukkan nilai suhu:", value=0.0, key="suhu")
    satuan = st.selectbox("Pilih satuan asal:", ["Celcius", "Reamur", "Fahrenheit"])

    if st.button("Konversi", key="konversi"):
        if satuan == "Celcius":
            reamur = (4/5) * suhu
            fahrenheit = (9/5) * suhu + 32
            st.write(f"Reamur: {reamur} °Re")
            st.write(f"Fahrenheit: {fahrenheit} °F")

        elif satuan == "Reamur":
            celcius = (5/4) * suhu
            fahrenheit = (9/4) * suhu + 32
            st.write(f"Celcius: {celcius} °C")
            st.write(f"Fahrenheit: {fahrenheit} °F")

        elif satuan == "Fahrenheit":
            celcius = (5/9) * (suhu - 32)
            reamur = (4/9) * (suhu - 32)
            st.write(f"Celcius: {celcius} °C")
            st.write(f"Reamur: {reamur} °Re")

    st.button("⬅️ Kembali", on_click=lambda: goto("home"))

# ================================
# Halaman Fibonacci
# ================================
elif st.session_state.page == "fibonacci":
    st.header("🔢 Deret Fibonacci")

    n = st.number_input("Masukkan jumlah deret Fibonacci:", min_value=1, step=1, key="n")

    def fibonacci(n):
        deret = [0, 1]
        while len(deret) < n:
            deret.append(deret[-1] + deret[-2])
        return deret[:n]

    if st.button("Generate", key="fibo"):
        hasil = fibonacci(n)
        st.write(f"Deret Fibonacci hingga {n} bilangan:")
        st.success(hasil)

    st.button("⬅️ Kembali", on_click=lambda: goto("home"))
