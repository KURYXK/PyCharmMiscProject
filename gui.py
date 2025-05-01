import tkinter as tk
from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto

def indit_gui():
    kolcsonzo = Autokolcsonzo("Pótkerék Autókölcsönző")
    kolcsonzo.autok_felvetele(Szemelyauto("AAAA-123", "Személyautó", 5000))
    kolcsonzo.autok_felvetele(Teherauto("AAAB-456", "Teherautó", 10000))
    kolcsonzo.autok_felvetele(Szemelyauto("AAAC-789", "Személyautó", 7000))

    kolcsonzo.foglalas("AAAA-123", "2025-05-05")
    kolcsonzo.foglalas("AAAA-123", "2025-05-06")
    kolcsonzo.foglalas("AAAB-456", "2025-05-05")
    kolcsonzo.foglalas("AAAC-789", "2025-05-05")

    app = tk.Tk()
    app.title("Pótkerék autókölcsönző")

    tk.Label(app, text="Rendszám (ABCD-012):").grid(row=0, column=0)
    rendszam_mezo = tk.Entry(app)
    rendszam_mezo.grid(row=0, column=1)

    tk.Label(app, text="Dátum (ÉÉÉÉ-HH-NN):").grid(row=1, column=0)
    datum_mezo = tk.Entry(app)
    datum_mezo.grid(row=1, column=1)

    # Bérelhető autók listája
    tk.Label(app, text="Bérelhető autók listája:").grid(row=2, column=0, columnspan=2)
    autok_mezo = tk.Text(app, height=3, width=40, state="disabled")
    autok_mezo.grid(row=3, column=0, columnspan=2)

    # Foglalt időpontok
    tk.Label(app, text="Foglalt időpontok:").grid(row=4, column=0, columnspan=2)
    berlesek_mezo = tk.Text(app, height=10, width=40, state="disabled")
    berlesek_mezo.grid(row=5, column=0, columnspan=2)

    # Üzenetek
    tk.Label(app, text="Üzenetek:").grid(row=6, column=0, columnspan=2)
    uzenet_mezo = tk.Text(app, height=2, width=40, state="disabled")
    uzenet_mezo.grid(row=7, column=0, columnspan=2)

    def frissit_autok_mezo():
        autok_mezo.config(state="normal")
        autok_mezo.delete("1.0", "end")
        for auto in kolcsonzo.autok:
            autok_mezo.insert("end", f"Rendszám: {auto.rendszam}, Típus: {auto.tipus}\n")
        autok_mezo.config(state="disabled")

    def frissit_berlesek_mezo():
        berlesek_mezo.config(state="normal")
        berlesek_mezo.delete("1.0", "end")
        for berles in kolcsonzo.berlesek:
            berlesek_mezo.insert("end", f"Rendszám: {berles.auto.rendszam}, Dátum: {berles.datum}\n")
        berlesek_mezo.config(state="disabled")

    def uzenet_kiiras(uzenet):
        uzenet_mezo.config(state="normal")
        uzenet_mezo.delete("1.0", "end")
        uzenet_mezo.insert("end", uzenet)
        uzenet_mezo.config(state="disabled")

    def foglalas():
        rendszam = rendszam_mezo.get()
        datum = datum_mezo.get()
        uzenet_kiiras(kolcsonzo.foglalas(rendszam, datum))
        frissit_berlesek_mezo()

    def lemondas():
        rendszam = rendszam_mezo.get()
        datum = datum_mezo.get()
        uzenet_kiiras(kolcsonzo.lemondas(rendszam, datum))
        frissit_berlesek_mezo()

    tk.Button(app, text="Foglalás", command=foglalas).grid(row=8, column=0)
    tk.Button(app, text="Lemondás", command=lemondas).grid(row=8, column=1)
    tk.Button(app, text="Kilépés", command=app.destroy).grid(row=9, column=0, columnspan=2)

    # Kezdeti frissítések
    frissit_autok_mezo()
    frissit_berlesek_mezo()

    app.mainloop()

# Program indítása
if __name__ == "__main__":
    indit_gui()
