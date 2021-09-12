import tkinter as tk
import sub_calc as s

root = tk.Tk()
root.title(" GUI Subnet calculator")
root.geometry("600x400")
root.config(bg='#710312')

ip = tk.StringVar(root)
ip_bin = tk.StringVar(root)
sub_bin = tk.StringVar(root)
sub = tk.StringVar(root)
nwadr = tk.StringVar(root)
bdadr = tk.StringVar(root)
no_host = tk.StringVar(root)


def clean():
    ip.set('')
    ip_bin.set('')
    sub.set('')
    sub_bin.set('')
    nwadr.set('')
    bdadr.set('')
    no_host.set('')


def main_sub_calc():
    ip1 = ip.get()
    sub1 = sub.get()
    ip_bin.set(s.get_ip(ip1)[0])
    sub_bin.set(s.get_subnet_mask(sub1)[0])
    nwadr.set(s.get_nw_address(ip1, sub1))
    bdadr.set(s.get_broadcast_address(ip1, sub1))
    no_host.set(s.get_no_of_ips(sub1))


tk.Label(root, text="IP Address").grid(row=0, column=1)
ipfld = tk.Entry(root, textvariable=ip)
ipfld.grid(row=0, column=3)

tk.Label(root, text="Subnet").grid(row=1, column=1)
sbntfld = tk.Entry(root, textvariable=sub)
sbntfld.grid(row=1, column=3)

tk.Button(root, text="Calculate", command=main_sub_calc).grid(row=2, column=2)
tk.Button(root, text="Clear", command=clean).grid(row=2, column=3)

tk.Label(root, text="IP Address").grid(row=3, column=1)
ip_binfld = tk.Entry(root, textvariable=ip_bin,width=40)
ip_binfld.grid(row=3, column=3)

tk.Label(root, text="Subnet").grid(row=4, column=1)
sub_binfld = tk.Entry(root, textvariable=sub_bin,width=40)
sub_binfld.grid(row=4, column=3)

tk.Label(root, text="Network Address").grid(row=5, column=1)
nwadrfld = tk.Entry(root, textvariable=nwadr,width=40)
nwadrfld.grid(row=5, column=3)

tk.Label(root, text="Broadcast Address").grid(row=6, column=1)
bdadrfld = tk.Entry(root, textvariable=bdadr,width=40)
bdadrfld.grid(row=6, column=3)

tk.Label(root, text="No Of available IP").grid(row=7, column=1)
avipfld = tk.Entry(root, textvariable=no_host,width=40)
avipfld.grid(row=7, column=3)


root.mainloop()