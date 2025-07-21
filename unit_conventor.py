import tkinter as tk
from tkinter import ttk, messagebox

def convert():
    try:
        val = float(entry_value.get())
        unit = combo_units.get()

        if unit == "متر به فوت":
            result = val * 3.28084
        elif unit == "فوت به متر":
            result = val / 3.28084
        elif unit == "کیلوگرم به پوند":
            result = val * 2.20462
        elif unit == "پوند به کیلوگرم":
            result = val / 2.20462
        elif unit == "سانتی‌گراد به فارنهایت":
            result = (val * 9/5) + 32
        elif unit == "فارنهایت به سانتی‌گراد":
            result = (val - 32) * 5/9
        else:
            result = "واحد نامعتبر"
        
        label_result.config(text=f"نتیجه: {round(result, 4)}")
    except ValueError:
        messagebox.showerror("خطا", "لطفاً یک عدد معتبر وارد کنید.")

window = tk.Tk()
window.title("مبدل واحد")
window.geometry("300x250")

tk.Label(window, text="مقدار را وارد کنید:").pack(pady=5)
entry_value = tk.Entry(window)
entry_value.pack(pady=5)

tk.Label(window, text="نوع تبدیل را انتخاب کنید:").pack(pady=5)
combo_units = ttk.Combobox(window, values=[
    "متر به فوت",
    "فوت به متر",
    "کیلوگرم به پوند",
    "پوند به کیلوگرم",
    "سانتی‌گراد به فارنهایت",
    "فارنهایت به سانتی‌گراد"
])
combo_units.pack(pady=5)
combo_units.current(0)

tk.Button(window, text="تبدیل", command=convert).pack(pady=10)

label_result = tk.Label(window, text="نتیجه:")
label_result.pack(pady=10)

window.mainloop()