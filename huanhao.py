import os
import tkinter as tk
from tkinter import messagebox
import winreg
import shutil
from tkinter import simpledialog

# messagebox.showerror("错误", "请以管理员权限运行程序！")
def account_switch_tool(window):
    window.attributes('-topmost', 1)
    def add_item():
        item = entry.get()
        folder_path = "hfconfig"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        subfolder_name = entry.get()
        subfolder_path = os.path.join(folder_path, subfolder_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        filename = os.path.join(subfolder_path, entry.get() + "-1.txt")  # 获取输入框中的文件名，并加上文件夹路径
        filename1 = os.path.join(subfolder_path, entry.get() + "-2.txt")  # 获取输入框中的文件名，并加上文件夹路径
        if item:
            # 检查是否存在同名文件
            if os.path.exists(filename) or os.path.exists(filename1):
                messagebox.showerror("错误", "已存在同名文件，请更改项目名称")
                return

        if item:
            listbox.insert(tk.END, item)
            entry.delete(0, tk.END)
            update_yes_button_state()
            # 从注册表中读取数据并保存到文件
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\miHoYo\原神")
                value, _ = winreg.QueryValueEx(key, "GENERAL_DATA_h2389025596")
                hex_value = value.hex()
                with open(filename, "w") as file:
                    file.write(hex_value)
                messagebox.showinfo("成功", f"游戏账号已成功保存到文件 '{filename}'")
            except Exception as e:
                messagebox.showerror("错误", f"保存文件时出错：{str(e)}")
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\miHoYo\原神")
                value, _ = winreg.QueryValueEx(key, "MIHOYOSDK_ADL_PROD_CN_h3123967166")
                hex_value = value.hex()
                with open(filename1, "w") as file:
                    file.write(hex_value)
                # messagebox.showinfo("成功", f"游戏账号已成功保存到文件 '{filename}'")
            except Exception as e:
                x = 1
                # messagebox.showerror("错误", f"保存文件时出错：{str(e)}")

    def delete_item():
        selected_indices = listbox.curselection()
        for index in selected_indices:
            folder_name = listbox.get(index)
            folder_path = os.path.join("hfconfig", folder_name)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)  # 递归删除文件夹及其内容
                listbox.delete(index)
        update_yes_button_state()

    def yes_item():

        selected_indices = listbox.curselection()
        if not selected_indices:
            messagebox.showerror("错误", "请先选择一个项目")
            return

        folder_name = listbox.get(selected_indices[0])
        folder_path = os.path.join("hfconfig", folder_name)
        if os.path.exists(folder_path):
            filename1 = os.path.join(folder_path, folder_name + "-1.txt")
            filename2 = os.path.join(folder_path, folder_name + "-2.txt")
            try:
                with open(filename1, "r") as file:
                    data1 = file.read()
                with open(filename2, "r") as file:
                    data2 = file.read()
                # 将数据写回注册表
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\miHoYo\原神", 0, winreg.KEY_SET_VALUE)
                # 删除指定名称的键值
                winreg.DeleteValue(key, "GENERAL_DATA_h2389025596")
                winreg.DeleteValue(key, "MIHOYOSDK_ADL_PROD_CN_h3123967166")
                #写回数据
                winreg.SetValueEx(key, "GENERAL_DATA_h2389025596", 0, winreg.REG_BINARY, bytes.fromhex(data1))
                winreg.SetValueEx(key, "MIHOYOSDK_ADL_PROD_CN_h3123967166", 0, winreg.REG_BINARY, bytes.fromhex(data2))
                messagebox.showinfo("成功", "数据成功写回注册表")
            except Exception as e:
                messagebox.showerror("错误", f"写回注册表时出错：{str(e)}")

    def rename_item(event):
        selected_indices = listbox.curselection()
        if not selected_indices:
            return
        index = selected_indices[0]
        old_name = listbox.get(index)
        new_name = simpledialog.askstring("重命名", "请在下方输入要修改的新的项目名称:", initialvalue=old_name)
        if new_name:
            folder_path_old = os.path.join("hfconfig", old_name)
            folder_path_new = os.path.join("hfconfig", new_name)
            os.rename(folder_path_old, folder_path_new)
            listbox.delete(index)
            listbox.insert(index, new_name)
            update_yes_button_state()


    def update_yes_button_state():
        if listbox.size() == 0:
            yes_button.config(state=tk.DISABLED)
        else:
            yes_button.config(state=tk.NORMAL)

    def load_saved_items():
        folder_path = "hfconfig"
        if not os.path.exists(folder_path):
            return
        for subfolder_name in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder_name)
            if os.path.isdir(subfolder_path):
                listbox.insert(tk.END, subfolder_name)
    class Tooltip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tooltip = None
            self.widget.bind("<Enter>", self.show_tooltip)
            self.widget.bind("<Leave>", self.hide_tooltip)

        def show_tooltip(self, event=None):
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 20
            self.tooltip = tk.Toplevel(self.widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")
            label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1)
            label.pack()

        def hide_tooltip(self, event=None):
            if self.tooltip:
                self.tooltip.destroy()
                self.tooltip = None

    # 创建主窗口

    # 创建列表框
    listbox = tk.Listbox(window)
    listbox.grid(row=0, column=0, padx=10, pady=10)
    listbox.bind("<Double-Button-1>", rename_item)

    # 创建输入框
    entry = tk.Entry(window)
    entry.grid(row=1, column=0, padx=10, pady=5)

    # 创建添加按钮
    add_button = tk.Button(window, text="添加", command=add_item)
    add_button.grid(row=1, column=1, padx=5, pady=5)
    Tooltip(add_button, "点击后会将当前登录的账号登陆情况保存在本地\n下次切换账号不需要再次输入账号密码\n为您节约时间\n (设备从通行证解绑或更改密码之后失效)")

    # 创建删除按钮
    delete_button = tk.Button(window, text="删除", command=delete_item)
    delete_button.grid(row=1, column=2, padx=5, pady=5)

    # 创建确认按钮
    yes_button = tk.Button(window, text="确认", command=yes_item, padx=40, pady=10)
    yes_button.grid(row=2, column=0, padx=5, pady=5)

    # 加载之前保存的项目
    load_saved_items()



