import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox, colorchooser
import os, sys
from core import data, model
from ui import plot
import matplotlib.pyplot as plt

BG       = "#0F1117"   # near-black background
SURFACE  = "#1A1D27"   # card / frame surface
BORDER   = "#2A2D3E"   # subtle separator
ACCENT   = "#20C9C0"   # purple accent
ACCENT2  = "#23FFFB"   # lighter purple for hover / secondary text
TEXT     = "#E8E8F0"   # primary text
SUBTEXT  = "#B4B4B5"   # secondary / muted text
SUCCESS  = "#23FD36"   # teal for positive metrics
WARNING  = "#FF6B6B"   # red for errors

FONT_TITLE  = ("Segoe UI", 22, "bold")
FONT_SUB    = ("Segoe UI", 11)
FONT_LABEL  = ("Segoe UI", 10, "bold")
FONT_SMALL  = ("Segoe UI", 9)
FONT_MONO   = ("Consolas", 10)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Linear Regression App")
        self.resizable(True, True)
        self.state("zoomed")
        self.configure(bg=BG)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._build_styles()
        self._build_header()
        self._build_body()
        self._build_file_section()

    def _build_styles(self):
        s = ttk.Style(self)
        s.theme_use("clam")

        s.configure(".",
            background=BG, foreground=TEXT,
            font=FONT_SUB, borderwidth=0, relief="flat")

        s.configure("Title.TLabel",
            font=FONT_TITLE, foreground=TEXT, background=BG)

        s.configure("Sub.TLabel",
            font=FONT_SUB, foreground=SUBTEXT, background=BG)

        s.configure("Field.TLabel",
            font=FONT_LABEL, foreground=ACCENT2, background=SURFACE)

        s.configure("Metric.TLabel",
            font=FONT_MONO, foreground=SUCCESS, background=SURFACE)

        s.configure("Card.TLabel",
            font=FONT_LABEL, foreground=TEXT, background=SURFACE)

        s.configure("Primary.TButton",
            font=FONT_LABEL, foreground="white", background=ACCENT,
            padding=(16, 8), relief="flat", borderwidth=0)
        s.map("Primary.TButton",
            background=[("active", ACCENT2), ("disabled", BORDER)],
            foreground=[("disabled", SUBTEXT)])

        s.configure("Ghost.TButton",
            font=FONT_SMALL, foreground=ACCENT2, background=SURFACE,
            padding=(10, 6), relief="flat", borderwidth=0)
        s.map("Ghost.TButton",
            background=[("active", BORDER)],
            foreground=[("active", TEXT)])

        s.configure("Danger.TButton",
            font=FONT_SMALL, foreground=WARNING, background=SURFACE,
            padding=(10, 6), relief="flat", borderwidth=0)
        s.map("Danger.TButton",
            background=[("active", BORDER)])

        s.configure("Custom.TRadiobutton",
            font=FONT_SUB, foreground=TEXT, background=SURFACE,
            indicatorcolor=ACCENT)
        s.map("Custom.TRadiobutton",
            foreground=[("active", ACCENT2)],
            background=[("active", SURFACE)])

        s.configure("TEntry",
            fieldbackground=BORDER, foreground=TEXT,
            insertcolor=TEXT, padding=(8, 6))

        s.configure("Treeview",
            background=SURFACE, foreground=TEXT,
            fieldbackground=SURFACE, rowheight=30,
            font=FONT_SMALL, borderwidth=0)
        s.configure("Treeview.Heading",
            background=BORDER, foreground=ACCENT2,
            font=FONT_LABEL, relief="flat")
        s.map("Treeview",
            background=[("selected", ACCENT)],
            foreground=[("selected", "white")])

    def _build_header(self):
        header = tk.Frame(self, bg=SURFACE, pady=0)
        header.pack(fill="x")

        tk.Frame(header, bg=ACCENT, height=3).pack(fill="x")

        inner = tk.Frame(header, bg=SURFACE, padx=28, pady=14)
        inner.pack(fill="x")
        inner.columnconfigure(1, weight=1)

        tk.Label(inner, text="Linear Regression App",
                 font=FONT_TITLE, fg=TEXT, bg=SURFACE).grid(row=0, column=0, sticky="w")

        tk.Label(inner, text="Visualise & predict from any CSV",
                 font=FONT_SMALL, fg=SUBTEXT, bg=SURFACE).grid(row=1, column=0, sticky="w")

        ttk.Button(inner, text="↺  Restart", style="Danger.TButton",
                   command=self.restart_app).grid(row=0, column=2, sticky="e", rowspan=2)

        tk.Frame(self, bg=BORDER, height=1).pack(fill="x")

    def _build_body(self):
        wrapper = tk.Frame(self, bg=BG)
        wrapper.pack(fill="both", expand=True)

        canvas = tk.Canvas(wrapper, bg=BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.body = tk.Frame(canvas, bg=BG)
        self.body_window = canvas.create_window((0, 0), window=self.body, anchor="nw")

        def _on_resize(event):
            canvas.itemconfig(self.body_window, width=event.width)
        def _on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind("<Configure>", _on_resize)
        self.body.bind("<Configure>", _on_frame_configure)
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def _card(self, parent, title=None):
        """Returns a framed card widget with optional title."""
        outer = tk.Frame(parent, bg=BORDER, padx=1, pady=1)
        outer.pack(fill="x", padx=28, pady=8)
        inner = tk.Frame(outer, bg=SURFACE, padx=20, pady=16)
        inner.pack(fill="x")
        if title:
            tk.Label(inner, text=title, font=FONT_LABEL,
                     fg=ACCENT2, bg=SURFACE).pack(anchor="w", pady=(0, 10))
        return inner

    def _section_label(self, text):
        row = tk.Frame(self.body, bg=BG, padx=28)
        row.pack(fill="x", pady=(18, 4))
        tk.Label(row, text=text, font=FONT_SMALL,
                 fg=SUBTEXT, bg=BG).pack(side="left")
        tk.Frame(row, bg=BORDER, height=1).pack(side="left", fill="x",
                                                 expand=True, padx=(10, 0), pady=7)

    def _build_file_section(self):
        self._section_label("STEP 1 — LOAD DATA")
        card = self._card(self.body, "Choose a CSV file")

        self.release = tk.StringVar(value="0")

        radio_row = tk.Frame(card, bg=SURFACE)
        radio_row.pack(fill="x", pady=(0, 12))

        ttk.Radiobutton(radio_row, text="Browse from PC",
                        variable=self.release, value="0",
                        style="Custom.TRadiobutton",
                        command=self.check_selection).pack(side="left", padx=(0, 24))
        ttk.Radiobutton(radio_row, text="Paste file path",
                        variable=self.release, value="1",
                        style="Custom.TRadiobutton",
                        command=self.check_selection).pack(side="left")

        self.action_row = tk.Frame(card, bg=SURFACE)
        self.action_row.pack(fill="x")

        self.btn_choose_file = ttk.Button(self.action_row, text="Browse…",
                                          style="Primary.TButton",
                                          command=self.pick_csv)

        self.entry_path    = ttk.Entry(self.action_row)
        self.validate_path = ttk.Button(self.action_row, text="Load",
                                        style="Primary.TButton",
                                        command=self.check_whether_csv)

        self.check_selection()

    def check_selection(self):
        for w in self.action_row.winfo_children():
            w.pack_forget()
        if self.release.get() == "0":
            self.btn_choose_file.pack(side="left")
        else:
            self.entry_path.pack(side="left", fill="x", expand=True, padx=(0, 8))
            self.validate_path.pack(side="left")

    def restart_app(self):
        self.destroy()
        os.execv(sys.executable, [sys.executable] + sys.argv)

    def pick_csv(self):
        file_path = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv_path = file_path
            self.check_whether_csv()

    def check_whether_csv(self):
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
        self._disable_file_widgets()
        self.show_preview()
        return True

    def _disable_file_widgets(self):
        self.radio_from_pc  = None   
        self.btn_choose_file.state(["disabled"])
        self.entry_path.state(["disabled"])
        self.validate_path.state(["disabled"])

    def show_preview(self):
        self.data_handler.load_data()
        dropped = self.data_handler.missing_values()
        if dropped:
            messagebox.showwarning(
                "Missing values",
                f"{dropped} row(s) with missing values were removed.")

        df = self.data_handler.df
        preview = df.iloc[:3, :]
        cols = list(preview.columns)
        filename = os.path.basename(self.csv_path)

        self._section_label("STEP 2 — SELECT COLUMNS")

        prev_card = self._card(self.body, f"Preview — {filename}")

        tree = ttk.Treeview(prev_card, columns=cols, show="headings", height=3)
        col_width = max(120, 700 // len(cols))
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=col_width, anchor="center")
        for _, row in preview.iterrows():
            tree.insert("", "end", values=list(row))
        tree.pack(fill="x")

        col_card = self._card(self.body, "Define features and target")

        grid = tk.Frame(col_card, bg=SURFACE)
        grid.pack(fill="x")
        grid.columnconfigure(1, weight=1)
        grid.columnconfigure(3, weight=1)

        tk.Label(grid, text="Feature column(s) x",
                 font=FONT_LABEL, fg=ACCENT2, bg=SURFACE).grid(
            row=0, column=0, sticky="w", padx=(0, 8))
        tk.Label(grid, text="Use ';' to separate qome features",
                 font=FONT_SMALL, fg=SUBTEXT, bg=SURFACE).grid(
            row=1, column=0, sticky="w", padx=(0, 8))

        self.entry_x_columns = ttk.Entry(grid)
        self.entry_x_columns.grid(row=0, column=1, rowspan=2, sticky="ew",
                                   padx=(0, 24), ipady=4)

        tk.Label(grid, text="Target column y",
                 font=FONT_LABEL, fg=ACCENT2, bg=SURFACE).grid(
            row=0, column=2, sticky="w", padx=(0, 8))

        self.entry_y_column = ttk.Entry(grid)
        self.entry_y_column.grid(row=0, column=3, rowspan=2, sticky="ew",
                                  padx=(0, 16), ipady=4)

        self.confirm_button_columns = ttk.Button(
            grid, text="Confirm", style="Primary.TButton",
            command=self.check_columns_exists)
        self.confirm_button_columns.grid(row=0, column=4, rowspan=2, padx=(8, 0))

    def check_columns_exists(self):
        y       = self.entry_y_column.get().strip()
        x_input = self.entry_x_columns.get().strip()

        if not x_input or not y:
            messagebox.showerror("Error", "Please fill both fields.")
            return

        x_cols = [col.strip() for col in x_input.split(";")]


        valid_cols = list(self.data_handler.df.columns)
        for col in x_cols + [y]:
            if col not in valid_cols:
                messagebox.showerror("Error", f"Column '{col}' not found in dataset.")
                return

        if len(x_cols) > 10:
            messagebox.showerror("Error", "The number of selected features is above 7.")
            return
        self.x_cols = x_cols
        self.y_col  = y
        string_cols = self.data_handler.check_string_columns()

        for col in self.x_cols + [self.y_col]:
            if col in string_cols:
                messagebox.showerror(
                    "Error",
                    f"Column '{col}' contains text values and cannot be used for regression.")
                return

        self.entry_x_columns.state(["disabled"])
        self.entry_y_column.state(["disabled"])
        self.confirm_button_columns.state(["disabled"])
        self.training_model()
        self.after(500, self.show_results_graphic)

    def training_model(self):
        self.tmodel = model.Analyser()
        self.y_column, self.X = self.data_handler.get_columns(self.y_col,self.x_cols)

        self.report = self.tmodel.training(
            self.X,
            self.y_column
        )

    def show_results_graphic(self):
        self.plotter = plot.Plotter()

        self._section_label("STEP 3 — RESULTS")

        metrics_card = self._card(self.body, "Model metrics")

        metrics_row = tk.Frame(metrics_card, bg=SURFACE)
        metrics_row.pack(fill="x")

        metrics = [
            ("MSE", f"{self.report['MSE']:.4f}"),
            ("R² score", f"{self.report['R2']:.4f}"),
        ]


        for i, coef in enumerate(self.report["coefficients"], start=1):
            metrics.append((f"Coef {i}", f"{coef:.4f}"))
        

        metrics.append(("Intercept", f"{self.report['intercept']:.4f}"))

        for label, value in metrics:
            cell = tk.Frame(metrics_row, bg=BORDER, padx=1, pady=1)
            cell.pack(side="left", padx=(0, 8), pady=4)
            inner = tk.Frame(cell, bg=SURFACE, padx=14, pady=10)
            inner.pack()
            tk.Label(inner, text=label, font=FONT_SMALL,
                     fg=SUBTEXT, bg=SURFACE).pack(anchor="w")
            tk.Label(inner, text=value, font=("Consolas", 14, "bold"),
                     fg=SUCCESS, bg=SURFACE).pack(anchor="w")

        self.colour_1 = "#6C63FF"
        self.colour_2 = "#4ECDC4"
        self.colour_3 = "#FF6B6B"

        colours_card = self._card(self.body, "Graph colours")

        def pick_colour(title, attr, swatch):
            current = getattr(self, attr)
            result  = colorchooser.askcolor(title=title, initialcolor=current)
            if result[1]:
                setattr(self, attr, result[1])
                swatch.configure(bg=result[1])

        def make_picker(parent, label_text, attr, default):
            col_frame = tk.Frame(parent, bg=SURFACE)
            col_frame.pack(side="left", padx=(0, 24))

            tk.Label(col_frame, text=label_text, font=FONT_SMALL,
                     fg=SUBTEXT, bg=SURFACE).pack(anchor="w")

            row = tk.Frame(col_frame, bg=SURFACE)
            row.pack(anchor="w", pady=(4, 0))

            swatch = tk.Frame(row, bg=default, width=24, height=24,
                              relief="flat", cursor="hand2")
            swatch.pack(side="left", padx=(0, 8))
            swatch.pack_propagate(False)

            ttk.Button(row, text="Pick", style="Ghost.TButton",
                       command=lambda: pick_colour(label_text, attr, swatch)
                       ).pack(side="left")

        picker_row = tk.Frame(colours_card, bg=SURFACE)
        picker_row.pack(fill="x")
        if len(self.x_cols) <= 2:
            make_picker(
                picker_row,
                "Regression line" if len(self.x_cols) == 1 else "Regression plane",
                "colour_1",
                self.colour_1
            )

            make_picker(
                picker_row,
                "Training data",
                "colour_2",
                self.colour_2
            )

            make_picker(
                picker_row,
                "Testing data",
                "colour_3",
                self.colour_3
            )

        else:
            make_picker(
                picker_row,
                "Prediction points",
                "colour_2",
                self.colour_2
            )

            make_picker(
                picker_row,
                "Ideal line",
                "colour_1",
                self.colour_1
            )
        action_card = self._card(self.body)

        btn_row = tk.Frame(action_card, bg=SURFACE)
        btn_row.pack(fill="x", pady=(0, 12))

        self.show_graphic_button = ttk.Button(
            btn_row, text="Show graph", style="Primary.TButton",
            command=self.graph_building)
        self.show_graphic_button.pack(side="left")

        tk.Frame(action_card, bg=BORDER, height=1).pack(fill="x", pady=(0, 12))

        pred_row = tk.Frame(action_card, bg=SURFACE)
        pred_row.pack(fill="x")
        pred_row.columnconfigure(0, weight=1)

        tk.Label(pred_row, text="Predict a value",
                 font=FONT_LABEL, fg=ACCENT2, bg=SURFACE).grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, 6))

        self.prediction_entry = ttk.Entry(pred_row)
        self.prediction_entry.grid(row=1, column=0, sticky="ew", ipady=4, padx=(0, 8))

        ttk.Button(pred_row, text="Predict", style="Ghost.TButton",
                   command=self.do_predict).grid(row=1, column=1, padx=(0, 16))

        self.prediction_label = tk.Label(
            pred_row, text="—", font=("Consolas", 13, "bold"),
            fg=SUCCESS, bg=SURFACE)
        self.prediction_label.grid(row=1, column=2, sticky="w")

    def do_predict(self):
        raw = self.prediction_entry.get().strip()

        try:
            parts = [p.strip() for p in raw.split(";")]
            values = [float(p) for p in parts]

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter valid numeric values."
            )
            return

        if len(values) != len(self.x_cols):
            messagebox.showerror(
                "Error",
                f"This model expects {len(self.x_cols)} value(s), "
                f"but you've inserted {len(values)}."
            )
            return

        result = self.tmodel.predict(values)
        self.prediction_label.config(text=f"{result:.4f}")
    def graph_building(self):
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