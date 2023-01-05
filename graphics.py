import tkinter as tk
import hebrew_arabic_transliteration
from translation_map import translations, clusters, sofit_forms


def main():

    transformations = translations
    c = clusters
    s = sofit_forms

    def handle_click():
        text_to_convert = entry1.get(1.0, tk.END)
        converted_text =\
            hebrew_arabic_transliteration.process_words(
                text_to_convert,
                transformations,
                c,
                s)
        
        entry2.delete(1.0, tk.END)
        entry2.insert(1.0, converted_text)


    window = tk.Tk()

    entry1 = tk.Text(width=100, height=20, font=("Arial", 16))
    entry1.pack(fill=tk.X, padx=10, pady=10)

    button1 = tk.Button(
        master=window,
        text="Transliterate",
        width=25,
        height=5,
        command=handle_click
    )
    button1.pack(fill=tk.X, padx=10, pady=10)
    button1.bind(handle_click)

    entry2 = tk.Text(width=100, height=20, font=("Arial", 16))
    entry2.pack(fill=tk.X, padx=10, pady=10)

    window.mainloop()


main()
