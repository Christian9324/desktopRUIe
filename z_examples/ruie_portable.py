from PIL import Image, ImageTk
import customtkinter as ckt
import res.theme.Strings as strings
import res.theme.Colors as colors
import res.theme.Dimens as dimen
import time

ckt.set_appearance_mode("light")
ckt.set_default_color_theme("res/theme/custom_theme.json")

stringAuxTitle = " "
window_splash = ckt.CTk()
window_splash.geometry("1280x720")
# window.title(f"{stringAuxTitle*158}Reporte Único de Información Electronico")
window_splash.title(" Reporte Único de Información Electronico")
window_splash.iconbitmap("res/drawable/logo.ico")

frame = ckt.CTkFrame(master=window_splash)
frame.pack(pady=0, padx=60, fill="both", expand=True)

label_1 = ckt.CTkLabel(
    frame,
    text=strings.txtSplash_label1,
    font=("Montserrat bold", dimen.TS_ss_bienvenida),
    text_color=(colors.white, colors.rojo),
).pack(pady=30, padx=20)

label_2 = ckt.CTkLabel(
    frame,
    text=strings.txtSplash_label2,
    font=("Montserrat", dimen.TS_ss_layout),
    text_color=(colors.white, colors.rojo),
).pack(pady=12, padx=20, )

label_3 = ckt.CTkLabel(
    frame,
    text=strings.txtSplash_label3,
    font=("Montserrat", dimen.TS_ss_layout),
    text_color=(colors.white, colors.rojo),
).pack(padx=20, )

label_4 = ckt.CTkLabel(
    frame,
    text=strings.txtSplash_label4,
    font=("Montserrat bold", dimen.TS_ss_layout + 2),
    text_color=(colors.marron, colors.rojo),
).pack(pady=12, padx=20, )

imageEscudo = ckt.CTkLabel(
    frame,
    text="",
    image=ckt.CTkImage(light_image=Image.open("res/drawable/inami.png"), size=(177, 250)),
).pack(pady=33)

progressbar = ckt.CTkProgressBar(frame, orientation="horizontal")
progressbar.pack(pady=10)
progressbar.start()

label_5 = ckt.CTkLabel(
    frame,
    text=strings.txtSplash_label5,
    font=("Montserrat ", dimen.TS_ss_layout - 5),
    text_color=(colors.marron, colors.rojo),
).pack(pady=50)

def main():
    window_splash.destroy()
    window_main = ckt.CTk()
    window_main.geometry("1280x720")
    # window.title(f"{stringAuxTitle*158}Reporte Único de Información Electronico")
    window_splash.title(" Reporte Único de Información Electronico")
    window_splash.iconbitmap("res/drawable/logo.ico")


window_splash.mainloop()


