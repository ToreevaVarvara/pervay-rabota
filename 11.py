import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тореева Варвара Андреевна")
        self.create_tabs()

    def create_tabs(self):
        self.tab_control = ttk.Notebook(self.root)

        # Первая вкладка: Калькулятор
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Калькулятор')
        self.create_calculator(self.tab1)

        # Вторая вкладка: Чекбоксы
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='Чекбоксы')
        self.create_checkboxes(self.tab2)

        # Третья вкладка: Работа с текстом
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text='Работа с текстом')
        self.create_text_work(self.tab3)

        self.tab_control.pack(expand=1, fill='both', padx=10, pady=10) 

    def create_calculator(self, tab):
        self.num1 = tk.DoubleVar()
        self.num2 = tk.DoubleVar()
        self.result = tk.StringVar()

        tk.Entry(tab, textvariable=self.num1).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(tab, textvariable=self.num2).grid(row=0, column=2, padx=5, pady=5)

        self.operation = tk.StringVar(value='+')
        operations = ['+', '-', '*', '/']
        tk.OptionMenu(tab, self.operation, *operations).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(tab, text='Вычислить', command=self.calculate).grid(row=1, columnspan=3, pady=5)
        tk.Label(tab, textvariable=self.result).grid(row=2, columnspan=3)

    def calculate(self):
        try:
            n1 = self.num1.get()
            n2 = self.num2.get()
            op = self.operation.get()
            if op == '+':
                res = n1 + n2
            elif op == '-':
                res = n1 - n2
            elif op == '*':
                res = n1 * n2
            elif op == '/':
                res = n1 / n2
            self.result.set(res)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def create_checkboxes(self, tab):
        self.checkbox_var1 = tk.BooleanVar()
        self.checkbox_var2 = tk.BooleanVar()
        self.checkbox_var3 = tk.BooleanVar()

        tk.Checkbutton(tab, text='Первый', variable=self.checkbox_var1).pack(anchor='w', padx=5, pady=5)
        tk.Checkbutton(tab, text='Второй', variable=self.checkbox_var2).pack(anchor='w', padx=5, pady=5)
        tk.Checkbutton(tab, text='Третий', variable=self.checkbox_var3).pack(anchor='w', padx=5, pady=5)

        tk.Button(tab, text='Проверить выбор', command=self.check_selection).pack(pady=5)

    def check_selection(self):
        selected_options = []
        if self.checkbox_var1.get():
            selected_options.append('первый вариант')
        if self.checkbox_var2.get():
            selected_options.append('второй вариант')
        if self.checkbox_var3.get():
            selected_options.append('третий вариант')

        if selected_options:
            messagebox.showinfo("Выбор", "Вы выбрали: " + ", ".join(selected_options))
        else:
            messagebox.showinfo("Выбор", "Ничего не выбрано")

    def create_text_work(self, tab):
        tk.Button(tab, text='Загрузить текст из файла', command=self.load_text_file).pack(pady=5)
        self.text_area = tk.Text(tab, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both', padx=5, pady=5)

    def load_text_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END) 
                self.text_area.insert(tk.END, content)  

if __name__ == "__main__":
    root = tk.Tk()
