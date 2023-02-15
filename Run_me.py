import threading
import tkinter as tk
from Main import start


def run_whole(thresh, limit, blnc, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10):
    start(thresh, limit, blnc, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)


def run(thresh, limit, blnc, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10):
    thread = threading.Thread(target=run_whole, daemon=True, args=(thresh, limit, blnc, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10))
    thread.start()


def finish(win):
    exit(0)
    win.destroy()


def window():
    thresh = float(EditText.get("1.0", tk.END))
    limit = float(EditText1.get("1.0", tk.END))
    settings.destroy()
    main = tk.Tk(className="td Ameritrade Python Bot -- Main")
    main.geometry("1900x1000")

    balance = tk.StringVar()
    text2 = tk.StringVar()
    m1 = tk.StringVar()
    m2 = tk.StringVar()
    m3 = tk.StringVar()
    m4 = tk.StringVar()
    m5 = tk.StringVar()
    m6 = tk.StringVar()
    m7 = tk.StringVar()
    m8 = tk.StringVar()
    m9 = tk.StringVar()
    m10 = tk.StringVar()

    balance.set("Available Balance: ")
    text2.set("Top 10 Movers:- ")
    m1.set("M1: ")
    m2.set("M2: ")
    m3.set("M3: ")
    m4.set("M4: ")
    m5.set("M5: ")
    m6.set("M6: ")
    m7.set("M7: ")
    m8.set("M8: ")
    m9.set("M9: ")
    m10.set("M10: ")

    label3 = tk.Label(main, textvariable=balance, font=("Times New Roman", "14"))
    label3.grid(padx=10, pady=10, row=1, column=2)

    label4 = tk.Label(main, textvariable=text2, font=("Times New Roman", "14"))
    label4.grid(padx=10, pady=50, row=3, column=2)

    label5 = tk.Label(main, textvariable=m1, font=("Times New Roman", "14"))
    label5.grid(padx=10, pady=10, row=5, column=3)

    label6 = tk.Label(main, textvariable=m2, font=("Times New Roman", "14"))
    label6.grid(padx=170, pady=10, row=5, column=103)

    label7 = tk.Label(main, textvariable=m3, font=("Times New Roman", "14"))
    label7.grid(padx=10, pady=50, row=105, column=3)

    label8 = tk.Label(main, textvariable=m4, font=("Times New Roman", "14"))
    label8.grid(padx=170, pady=50, row=105, column=103)

    label9 = tk.Label(main, textvariable=m5, font=("Times New Roman", "14"))
    label9.grid(padx=10, pady=50, row=205, column=3)

    label10 = tk.Label(main, textvariable=m6, font=("Times New Roman", "14"))
    label10.grid(padx=170, pady=50, row=205, column=103)

    label11 = tk.Label(main, textvariable=m7, font=("Times New Roman", "14"))
    label11.grid(padx=10, pady=50, row=305, column=3)

    label12 = tk.Label(main, textvariable=m8, font=("Times New Roman", "14"))
    label12.grid(padx=170, pady=50, row=305, column=103)

    label13 = tk.Label(main, textvariable=m9, font=("Times New Roman", "14"))
    label13.grid(padx=10, pady=50, row=405, column=3)

    label14 = tk.Label(main, textvariable=m10, font=("Times New Roman", "14"))
    label14.grid(padx=170, pady=50, row=405, column=103)

    start_button = tk.Button(main, text="START", font=("Times New Roman", "14"), command=lambda: run(thresh, limit,
                                                                                                       balance, m1, m2,
                                                                                                       m3, m4, m5, m6,
                                                                                                       m7, m8, m9, m10))
    start_button.grid(padx=10, pady=50, row=605, column=3)

    end_button = tk.Button(main, text="END", font=("Times New Roman", "14"), command=lambda: finish(main))
    end_button.grid(padx=170, pady=50, row=605, column=103)

    main.mainloop()


settings = tk.Tk(className="td Ameritrade Python Bot -- Settings")
settings.geometry("500x350")
text = tk.StringVar()
text1 = tk.StringVar()
text.set("Enter Threshold Value: ")
text1.set("Enter Minimum Value to buy: ")

label = tk.Label(settings, textvariable=text, font=("Times New Roman", "14"))
label.grid(padx=10, pady=10, row=1, column=2)

EditText = tk.Text(settings, width=10, height=2)
EditText.grid(padx=70, pady=10, row=1, column=4)

label1 = tk.Label(settings, textvariable=text1, font=("Times New Roman", "14"))
label1.grid(padx=10, pady=70, row=3, column=2)

EditText1 = tk.Text(settings, width=10, height=2)
EditText1.grid(padx=70, pady=70, row=3, column=4)

button = tk.Button(settings, text="Next", command=window, font=("Times New Roman", "14"))
button.grid(pady=50, row=4, column=3)

settings.mainloop()
