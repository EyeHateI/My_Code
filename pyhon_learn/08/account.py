import tkinter as tk
import tkinter.messagebox
class Account:
    def account_check(account):
        length = 12
        least = 5
        x = 0
        print(account)
        if len(str(account)) > length:
            tk.messagebox.showerror(title='Error',message='账号长度过长')
            x = 1
        elif len(str(account)) < least:
            tk.messagebox.showerror(title='Error',message='账号长度过短')
            x = 1
        else:
            pass
        return x