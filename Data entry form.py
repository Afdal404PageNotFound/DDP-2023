import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Diterima":
        # Info Pengguna
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        gender = gender_combobox.get()
        
        if firstname and lastname:
            age = age_spinbox.get()
            domicile = domicile_combobox.get()
            
            # Info Pendaftaran
            registration_status = reg_status_var.get()
            numsemesters = numsemesters_spinbox.get()
            
            print("Nama Depan: ", firstname, "Nama Belakang: ", lastname, "Jenis Kelamin: ", gender)
            print("Umur: ", age, "Domisili: ", domicile)
            print("Status Pendaftaran: ", registration_status, "Semester: ", numsemesters)
            print("------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Nama depan dan nama belakang diperlukan.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="Anda belum menyetujui syarat dan ketentuan.")

window = tkinter.Tk()
window.title("Formulir Pendaftaran")

frame = tkinter.Frame(window)
frame.pack()

# Menyimpan Info Pengguna
user_info_frame =tkinter.LabelFrame(frame, text="Informasi Pengguna")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="Nama Depan")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Nama Belakang")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

gender_label = tkinter.Label(user_info_frame, text="Jenis Kelamin")
gender_combobox = ttk.Combobox(user_info_frame, values=["", "Laki-laki", "Perempuan"])
gender_label.grid(row=2, column=0)
gender_combobox.grid(row=3, column=0)

age_label = tkinter.Label(user_info_frame, text="Umur")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=1)
age_spinbox.grid(row=3, column=1)

domicile_label = tkinter.Label(user_info_frame, text="Domisili")
domicile_combobox = ttk.Combobox(user_info_frame, values=["Indonesia", "Luar Negeri"])
domicile_label.grid(row=4, column=0)
domicile_combobox.grid(row=5, column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Menyimpan Info Pendaftaran
registration_frame = tkinter.LabelFrame(frame)
registration_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(registration_frame, text="Status Pendaftaran")

reg_status_var = tkinter.StringVar(value="Belum Terdaftar")
registered_check = tkinter.Checkbutton(registration_frame, text="Sedang Terdaftar",
                                       variable=reg_status_var, onvalue="Terdaftar", offvalue="Belum Terdaftar")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numsemesters_label = tkinter.Label(registration_frame, text="Semester")
numsemesters_spinbox = tkinter.Spinbox(registration_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=1)
numsemesters_spinbox.grid(row=1, column=1)

for widget in registration_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Menyetujui Syarat dan Ketentuan
terms_frame = tkinter.LabelFrame(frame, text="Syarat & Ketentuan")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Belum Disetujui")
terms_check = tkinter.Checkbutton(terms_frame, text= "Saya menyetujui syarat dan ketentuan.",
                                  variable=accept_var, onvalue="Diterima", offvalue="Belum Disetujui")
terms_check.grid(row=0, column=0)

# Tombol
button = tkinter.Button(frame, text="Masukkan data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
