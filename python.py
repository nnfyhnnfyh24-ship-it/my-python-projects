import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import random
import time

# Developer: Project OS Customization
class OSProject:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom OS Simulator") # GUI Interface
        self.root.geometry("800x600")
        
        # Memory Management Initial State
        self.memory_capacity = 1024 
        self.memory_used = 0
        
        # Process Management Initial State
        self.processes = []
        
        # File System Initial State
        self.files = ["boot.sys", "config.txt"]

        self.create_gui()

    def create_gui(self):
        # GUI Implementation
        tk.Label(self.root, text="نظام تشغيل مخصص - OS Project", font=("Arial", 18, "bold")).pack(pady=10)

        # 1. إدارة العمليات
        p_frame = tk.LabelFrame(self.root, text=" إدارة العمليات (Process Management) ")
        p_frame.pack(fill="x", padx=20, pady=5)
        tk.Button(p_frame, text="تشغيل عملية جديدة", command=self.add_process).pack(side="left", padx=10, pady=10)
        self.p_label = tk.Label(p_frame, text="العمليات النشطة: 0")
        self.p_label.pack(side="left")

        # 2. إدارة الذاكرة
        m_frame = tk.LabelFrame(self.root, text=" إدارة الذاكرة (Memory Management) ")
        m_frame.pack(fill="x", padx=20, pady=5)
        self.progress = ttk.Progressbar(m_frame, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)
        self.m_label = tk.Label(m_frame, text=f"المستخدم: 0 / {self.memory_capacity} MB")
        self.m_label.pack()

        # 3. نظام الملفات
        f_frame = tk.LabelFrame(self.root, text=" نظام الملفات (File System) ")
        f_frame.pack(fill="x", padx=20, pady=5)
        tk.Button(f_frame, text="إنشاء ملف", command=self.create_file).pack(side="left", padx=10, pady=10)
        tk.Button(f_frame, text="عرض الملفات", command=self.show_files).pack(side="left", padx=10, pady=10)

        # 4. إدارة الأجهزة
        io_frame = tk.LabelFrame(self.root, text=" إدارة الأجهزة (I/O Management) ")
        io_frame.pack(fill="x", padx=20, pady=5)
        tk.Button(io_frame, text="فحص حالة الأجهزة", command=self.check_io).pack(pady=10)

    def add_process(self):
        p_id = random.randint(100, 999)
        usage = random.randint(50, 150)
        if self.memory_used + usage <= self.memory_capacity:
            self.processes.append(p_id)
            self.memory_used += usage
            self.update_stats()
            messagebox.showinfo("Process", f"Process {p_id} Started")
        else:
            messagebox.showerror("Error", "Memory Full!")

    def create_file(self):
        name = simpledialog.askstring("Files", "Enter file name:")
        if name:
            self.files.append(name)
            messagebox.showinfo("Success", "File Created")

    def show_files(self):
        messagebox.showinfo("Files", f"Disk Contents: {', '.join(self.files)}")

    def check_io(self):
        # I/O devices management check
        messagebox.showinfo("I/O Status", "Scanning Hardware...\nKeyboard: OK\nMouse: OK")

    def update_stats(self):
        self.p_label.config(text=f"العمليات النشطة: {len(self.processes)}")
        self.m_label.config(text=f"المستخدم: {self.memory_used} / {self.memory_capacity} MB")
        self.progress["value"] = (self.memory_used / self.memory_capacity) * 100

if __name__ == "__main__":
    root = tk.Tk()
    app = OSProject(root)
    root.mainloop()
                                              