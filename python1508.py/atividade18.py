import tkinter as tk

j = tk.Tk()
j.geometry('1700x750')
text2 = tk.Label(j, text= 'Formulario', font= (25))
text2.grid(row=0, column=0, pady=10, padx=10)


Nome = tk.Label(j, text= 'Nome', font= (25))
Nome.grid(row=1, column=1, pady=10, padx=10)

i1 = tk.Entry (j, font= (25)) 
i1.grid (row=2, column=1, pady=10, padx=10)


j.mainloop ()
