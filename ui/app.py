import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
import os
from core import data, model
import sys
from ui import plot
import matplotlib.pyplot as plt


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Linear Regression App")
        self.resizable(True, True)
        self.state("zoomed")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        self.style = ttk.Style()
        self.style.configure("TLabel",            font=('Roboto', 30, 'bold'),    foreground="navy")
        self.style.configure("CSVTitle.TLabel",   font=('Roboto', 18, 'italic'),  foreground="#B25050")
        self.style.configure("Custom.TRadiobutton", font=('Helvetica', 10, 'bold'), foreground="black")
        self.style.configure("Custom.TButton",    font=('Helvetica', 12, 'bold'), padding=(10, 10))
        self.style.configure("Custom2.TButton",   font=('Aptos', 13))
        self.style.configure("Custom2.TLabel",    font=('Aptos', 16, 'bold'),     foreground="navy")
        self.style.configure("Custom3.TButton",   font=('Aptos', 16, 'bold'),     padding=(40, 40))
        self.style.configure("Custom3.TLabel",    font=('Aptos', 12, 'bold'),     foreground="#2D0606")

        ttk.Label(self, text="Linear Regression App", style="TLabel",
                  justify="center", anchor="center").pack(fill="x")
        ttk.Button(self, text="↺ Restart",
                   command=self.restart_app).pack(anchor="ne", padx=10, pady=5)

        self.main_container = tk.Frame(self)
        self.main_container.pack(fill="x", padx=20, pady=20)
        self.main_container.columnconfigure(1, weight=1, minsize=460)
        self.main_container.columnconfigure(0, weight=1)
        self.main_container.rowconfigure(0, weight=1)
        self.radio_container = tk.Frame(self.main_container)
        self.radio_container.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.release = tk.StringVar()

        self.radio_from_pc = ttk.Radiobutton(
            self.radio_container, text="Load a csv from your PC",
            variable=self.release, value="0",
            style="Custom.TRadiobutton", command=self.check_selection)
        self.radio_from_pc.pack(anchor="w", pady=5)

        self.radio_from_path = ttk.Radiobutton(self.radio_container, text="Directly paste a csv path",
        variable=self.release, value="1",style="Custom.TRadiobutton", command=self.check_selection)

        self.radio_from_path.pack(anchor="w", pady=5)

        self.btn_choose_file = ttk.Button(self.main_container, text="Choose a csv :",
                                          style="Custom.TButton", command=self.pick_csv)
        self.entry_path  = ttk.Entry(self.main_container, style="Custom.TButton")
        self.validate_path = ttk.Button(self.main_container, text="Confirm",
                                        style="Custom.TButton", command=self.check_whether_csv)

        self.release.set("0")
        self.check_selection()

 

        

    def check_selection(self):
        """Show or hide widgets based on the selected file input mode."""
        if self.release.get() == "0":
            self.entry_path.grid_remove()
            self.validate_path.grid_remove()
            self.btn_choose_file.grid(row=0, column=1, padx=10)
        else:
            self.btn_choose_file.grid_remove()
            self.entry_path.grid(row=0, column=1, sticky="ew", padx=10)
            self.validate_path.grid(row=0, column=2, padx=5)

    def restart_app(self):
        """Restart the application from scratch."""
        self.destroy()
        os.execv(sys.executable, [sys.executable] + sys.argv)

    def pick_csv(self):
        """Open a file dialog and load the selected CSV file."""
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier CSV",
            filetypes=[("CSV Files", "*.csv")]
        )
        if file_path:
            self.csv_path = file_path
            self.check_whether_csv()


    def check_whether_csv(self):
        """Validate the CSV path and load the data if it is valid."""
        if self.release.get() == "0":
            if not hasattr(self, "csv_path") or not self.csv_path:
                messagebox.showerror("Error", "Please choose a CSV file first.")
                return False
        else:
            path = self.entry_path.get().strip()
            if not path:
                messagebox.showerror("Error", "Please paste a CSV path first.")
                return False
            if not os.path.exists(path):
                messagebox.showerror("Error", "This path does not exist.")
                return False
            if not path.lower().endswith(".csv"):
                messagebox.showerror("Error", "The file must be a .csv file.")
                return False
            self.csv_path = path

        self.data_handler = data.DataHandler(self.csv_path)
        self.disable_all()
        self.show_preview()
        return True

    def disable_all(self):
        """Lock the file selection widgets once a file has been loaded."""
        self.radio_from_pc.state(["disabled"])
        self.radio_from_path.state(["disabled"])
        self.btn_choose_file.state(["disabled"])
        self.entry_path.state(["disabled"])
        self.validate_path.state(["disabled"])


    def show_preview(self):
        """Display a preview of the CSV and the column selection inputs."""

        self.data_handler.load_data()
        self.data_handler.missing_values()
        df       = self.data_handler.df
        preview  = df.iloc[:3, :]
        cols     = list(preview.columns)
        filename = os.path.basename(self.csv_path)

        ttk.Label(self, text=f"Preview : {filename}",
                  style='CSVTitle.TLabel').pack(pady=(20, 3))

        tree = ttk.Treeview(self, columns=cols, show="headings", height=3)
        col_width = max(150, 600 // len(cols))
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=col_width, anchor="center")
        for _, row in preview.iterrows():
            tree.insert("", "end", values=list(row))
        tree.pack(padx=20, pady=10)

        self.columns_frame = tk.Frame(self)
        self.columns_frame.pack(padx=20, pady=10, anchor="w")

        self.label_x_columns = ttk.Label(
            self.columns_frame,
            text="Feature column(s) (x) (\";\" as a delimiter if 2 parameters) :",
            style='Custom2.TLabel')
        self.label_x_columns.grid(row=0, column=0, padx=(20, 5))

        self.entry_x_columns = ttk.Entry(self.columns_frame, style="Custom2.TButton")
        self.entry_x_columns.grid(row=0, column=1, padx=(0, 20))

        self.label_y_column = ttk.Label(self.columns_frame, text="Target column (y) :",
                                        style="Custom2.TLabel")
        self.label_y_column.grid(row=0, column=2, padx=(100, 5))

        self.entry_y_column = ttk.Entry(self.columns_frame, style="Custom2.TButton")
        self.entry_y_column.grid(row=0, column=3, padx=(0, 20))

        self.confirm_button_columns = ttk.Button(
            self.columns_frame, text="Confirm",
            style="Custom2.TButton", command=self.check_columns_exists)
        self.confirm_button_columns.grid(row=0, column=4, padx=100)


    def check_columns_exists(self):
        """Validate the chosen columns (existence, count, and data type)."""
        y       = self.entry_y_column.get().strip()
        x_input = self.entry_x_columns.get().strip()

        if not x_input or not y:
            messagebox.showerror("Error", "Please fill both fields.")
            return

        x_cols = [col.strip() for col in x_input.split(";")]
        if len(x_cols) > 2:
            messagebox.showerror("Error", "Maximum 2 feature columns (x).")
            return

        valid_cols = list(self.data_handler.df.columns)
        for col in x_cols + [y]:
            if col not in valid_cols:
                messagebox.showerror("Error", f"Column '{col}' not found in dataset.")
                return

        self.x_cols = x_cols
        self.y_col  = y

        string_cols = self.data_handler.check_string_columns()

        for col in self.x_cols + [self.y_col]:
            if col in string_cols:
                messagebox.showerror(
                    "Error",
                    f"Column '{col}' contains string values and cannot be used for regression."
                )
                return
        self.disable_all2()
        self.training_model()
        self.after(500, self.show_results_graphic)

    def disable_all2(self):
        """Lock the column selection widgets once confirmed."""
        self.entry_x_columns.state(["disabled"])
        self.entry_y_column.state(["disabled"])
        self.confirm_button_columns.state(["disabled"])

    def training_model(self):
        """Train the regression model on the selected columns."""
        self.tmodel = model.Analyser()

        if len(self.x_cols) == 1:
            self.y_column, self.x_column = self.data_handler.get_columns(
                self.y_col, self.x_cols[0])
            self.report = self.tmodel.training(self.x_column, self.y_column)

        elif len(self.x_cols) == 2:
            self.y_column, self.x_column, self.x_column2 = self.data_handler.get_columns(
                self.y_col, self.x_cols[0], x_2=self.x_cols[1])
            self.report = self.tmodel.training(
                self.x_column, self.y_column, x_column_2=self.x_column2)


    def show_results_graphic(self):
        """Display metrics, colour pickers, and the graph button."""
        self.plotter = plot.Plotter()

        # row 0 : metrics
        self.results_frame = tk.Frame(self)
        self.results_frame.columnconfigure(tuple(range(5)), weight=1)
        self.results_frame.pack(padx=20, pady=10, fill="x", expand=True)
        self.mse_label = ttk.Label(self.results_frame, style="Custom3.TLabel",
                                   text=f"MSE : {self.report['MSE']:.4f}")
        self.mse_label.pack(side="left", padx=20)

        self.r_2_label = ttk.Label(self.results_frame, style="Custom3.TLabel",
                                   text=f"r_2 score : {self.report['R2']:.4f}")
        self.r_2_label.pack(side="left", padx=20)

        self.coef1_label = ttk.Label(self.results_frame, style="Custom3.TLabel",
                                     text=f"coef : {self.report['coef1']:.4f}")
        self.coef1_label.pack(side="left", padx=20)

        coef2_text = (f"coef 2 : {self.report['coef2']:.4f}"
                      if self.report['coef2'] is not None else "coef 2 : none")
        self.coef2_label = ttk.Label(self.results_frame, style="Custom3.TLabel",
                                     text=coef2_text)
        self.coef2_label.pack(side="left", padx=20)

        self.intercept_label = ttk.Label(self.results_frame, style="Custom3.TLabel",
                                         text=f"Intercept : {self.report['intercept']:.4f}")
        self.intercept_label.pack(side="left", padx=20)

        self.colour_1 = "#6CC4FE"  
        self.colour_2 = "#FF0000"  
        self.colour_3 = "#FFD900"  

        def pick_colour(title, attr, preview_label):
            current = getattr(self, attr)
            result  = colorchooser.askcolor(title=title, initialcolor=current)
            if result[1]:
                setattr(self, attr, result[1])
                preview_label.configure(background=result[1])

        def make_picker(parent, label_text, attr, default_colour, col):
            """Creates a label + preview square + button in one grid column group."""
            ttk.Label(parent, style="Custom3.TLabel",
                      text=label_text).grid(row=0, column=col*3, padx=(20, 5), pady=10)

            preview = tk.Label(parent, background=default_colour, width=3, relief="solid")
            preview.grid(row=0, column=col*3 + 1, padx=(0, 5))

            ttk.Button(parent, text="Pick", style="Custom2.TButton",
                       command=lambda: pick_colour(label_text, attr, preview)
                       ).grid(row=0, column=col*3 + 2, padx=(0, 30))

        self.colours_frame = tk.Frame(self)
        for i in range(9):
            self.colours_frame.columnconfigure(i, weight=1)
        self.colours_frame.pack(fill="x", padx=20, pady=20)        
        self.columns_frame.columnconfigure(1, weight=1)
        self.columns_frame.columnconfigure(3, weight=1)

        make_picker(self.colours_frame, "Colour of the slope",           "colour_1", self.colour_1, 0)
        make_picker(self.colours_frame, "Colour of the training values",  "colour_2", self.colour_2, 1)
        make_picker(self.colours_frame, "Colour of the testing values",   "colour_3", self.colour_3, 2)

        self.show_graphic_button = ttk.Button(
            self, style="Custom2.TButton",
            text="Show graph", command=lambda: self.graph_building())
        self.show_graphic_button.pack(pady=20)


    def graph_building(self):
        """Build and show the regression plot, or warn if one is already open."""
        if hasattr(self, "current_fig") and plt.fignum_exists(self.current_fig.number):
            messagebox.showwarning("Warning", "Please close the current graph first.")
            return

        def on_close(event):
            self.show_graphic_button.state(["!disabled"])

        self.current_fig = self.plotter.plot(
            self.report,
            self.report["R2"],
            len(self.x_cols),
            on_close=on_close,
            train_colour=self.colour_2,
            test_colour=self.colour_3,
            slope_colour=self.colour_1,
            x_label=self.x_cols[0],
            x2_label=self.x_cols[1] if len(self.x_cols) == 2 else "x2",
            y_label=self.y_col
        )
        self.show_graphic_button.state(["disabled"])


app = App()
app.mainloop()