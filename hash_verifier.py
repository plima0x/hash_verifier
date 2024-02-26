#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import hashlib


def get_hash_algorithms():
    hash_alg_list = list(hashlib.algorithms_guaranteed)
    hash_alg_list.sort()
    return hash_alg_list


def get_file_content(base_file: str) -> bytes:
    with open(base_file, mode="rb") as f:
        file_content = f.read()
    return file_content


def generate_hash(byte_obj: bytes, hash_alg: str) -> str:
    m = hashlib.new(hash_alg)
    m.update(byte_obj)
    obj_hash = m.hexdigest()
    return obj_hash


class HashVerifier:
    def __init__(self):
        self.root = Tk()
        # Variables that will store text that can be changed during the application.
        self.file_path_var = StringVar()
        self.current_hash_alg = StringVar()
        self.calc_hash_var = StringVar()
        self.compare_hash_var = StringVar()
        self.result_label_var = StringVar()

    def create_window(self):

        # Creating the window.
        self.root.title("Hash Verifier")

        self.root.resizable(FALSE, FALSE)
        s = ttk.Style()
        s.theme_use("clam")

        # Creating the main frame.
        main_frame = ttk.Frame(self.root, padding=10, borderwidth=1, relief="solid")

        main_frame.grid(column=0, row=0, sticky=(W, E))
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        main_frame_title = ttk.Label(main_frame, text="Hash the file")
        main_frame_title.grid(column=1, row=1, sticky=N)

        # Creating the file label
        file_label = ttk.Label(main_frame, text="File path:")
        file_label.grid(column=0, row=2, sticky=(W))

        # Creating the entry that will have the file path.
        file_entry = ttk.Entry(main_frame, width=40, textvariable=self.file_path_var)
        file_entry.grid(column=1, row=2, sticky=(W, E))

        # Creating the button to browse for the file that will be used to calculate the hash.
        browser_file_btn = ttk.Button(main_frame, text="Browse", cursor="hand2", command=self.get_file_by_dialog)
        browser_file_btn.grid(column=2, row=2)

        # Creating the calculated hash label.
        calc_hash_label = ttk.Label(main_frame, text="Hash calculated:")
        calc_hash_label.grid(column=0, row=3, sticky=W)

        # Creating the entry that will have the calculated hash.
        calc_hash_entry = ttk.Entry(main_frame, width=40, textvariable=self.calc_hash_var)
        calc_hash_entry.grid(column=1, row=3, sticky=(W, E))

        # Creating the combobox that will have all the hash algorithms that can be selected.
        hash_alg_list = ttk.Combobox(main_frame, width=10, height=5, textvariable=self.current_hash_alg)
        hash_alg_list["values"] = get_hash_algorithms()

        # Hash algorithm that will be displayed initially.
        self.current_hash_alg.set("sha256")

        # The user will not be able to modify the combobox.
        hash_alg_list.state(["readonly"])
        hash_alg_list.grid(column=2, row=3, sticky=E)

        # Creating the button that will call the method to calculate the hash.
        btn_calc_hash = ttk.Button(main_frame, text="Calculate the hash", cursor="hand2", width=20,
                                   command=self.hash_file_by_field)
        btn_calc_hash.grid(column=1, row=4)

        # Creating the label to store the text 'Hash to compare:'
        compare_hash_label = ttk.Label(main_frame, text="Hash to compare:")
        compare_hash_label.grid(column=0, row=5, sticky=W)

        # Creating the entry that will have the hash that will be used to compare with the calculated hash of the
        # file.
        compare_hash_entry = ttk.Entry(main_frame, width=40, textvariable=self.compare_hash_var)
        compare_hash_entry.grid(column=1, row=5, sticky=(W, E))

        # Creating the button that will call the method to compare the hashes.
        verify_btn = ttk.Button(main_frame, text="Verify", cursor="hand2", command=self.compare_two_hashes)
        verify_btn.grid(column=2, row=5, sticky=W)

        # Creating the label that will display the result of the comparison.
        result_label = ttk.Label(main_frame, textvariable=self.result_label_var)
        result_label.grid(column=0, columnspan=3, row=6, sticky=(N))

        # Setting the padding of all elements in the frame.
        for main_frame_child in main_frame.winfo_children():
            main_frame_child.grid_configure(padx=8, pady=8)

        # Start the event loop.
        self.root.mainloop()

    def get_file_by_dialog(self, *args):

        file_path = filedialog.askopenfilename()
        self.file_path_var.set(file_path)

    def hash_file_by_field(self, *args):
        self.result_label_var.set("")
        if not self.file_path_var.get():
            messagebox.showinfo(message="Please, select the file path")
            return

        bin_file_content = get_file_content(self.file_path_var.get())
        # self.progress_bar.start()
        calculated_hash = generate_hash(bin_file_content, self.current_hash_alg.get())
        # self.progress_bar.stop()
        self.calc_hash_var.set(calculated_hash)

    def compare_two_hashes(self):
        calculated_hash = self.calc_hash_var.get()
        hash_to_compare = self.compare_hash_var.get()

        if not calculated_hash:
            messagebox.showinfo(message="Please, calculate the file hash")
            return
        elif not hash_to_compare:
            messagebox.showinfo(message="Please, enter the hash to compare")
            return

        if calculated_hash == hash_to_compare:
            self.result_label_var.set("The hashes are equal")
        else:
            self.result_label_var.set("The hashes are different")
