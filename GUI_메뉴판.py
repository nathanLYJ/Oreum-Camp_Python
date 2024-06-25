import tkinter as tk
from tkinter import messagebox

def order_items():
    order_summary = "Order Summary\n"
    total_cost = 0

    # 아메리카노 메뉴 계산
    quantity = int(Americano_entry.get())
    if quantity > 0:
        item_total = quantity * 3000
        order_summary += f"Americano: {quantity} x 3000 = {item_total} won\n"
        total_cost += item_total

    # 라떼 메뉴 계산
    quantity = int(Latte_entry.get())
    if quantity > 0:
        item_total = quantity * 4000
        order_summary += f"Latte: {quantity} x 4000 = {item_total} won\n"
        total_cost += item_total

    # 녹차 메뉴 계산
    quantity = int(green_tea_entry.get())
    if quantity > 0:
        item_total = quantity * 2000
        order_summary += f"Green Tea: {quantity} x 2000 = {item_total} won\n"
        total_cost += item_total

    # 치즈케익 메뉴 계산
    quantity = int(cheese_Cake_entry.get())
    if quantity > 0:
        item_total = quantity * 5000
        order_summary += f"Cheese Cake: {quantity} x 5000 = {item_total} won\n"
        total_cost += item_total

    order_summary += f"\nTotal Cost: {total_cost} won\n"
    result_label.config(text=order_summary)

# 기본 윈도우를 구성
root = tk.Tk()
root.title("Cafe Order System")

# 아메리카노 메뉴 설정
tk.Label(root, text='Americano (3000 won):').grid(row=0, column=0)
Americano_entry = tk.Entry(root, width=5)
Americano_entry.grid(row=0, column=1)

# 라떼
tk.Label(root, text='Latte (4000 won):').grid(row=1, column=0)
Latte_entry = tk.Entry(root, width=5)
Latte_entry.grid(row=1, column=1)

# 녹차
tk.Label(root, text='Green Tea (2000 won):').grid(row=2, column=0)
green_tea_entry = tk.Entry(root, width=5)
green_tea_entry.grid(row=2, column=1)

# 치즈케익
tk.Label(root, text='Cheese Cake (5000 won):').grid(row=3, column=0)
cheese_Cake_entry = tk.Entry(root, width=5)
cheese_Cake_entry.grid(row=3, column=1)

# 주문하기 버튼
order_button = tk.Button(root, text='Order', command=order_items)
order_button.grid(row=4, column=0, columnspan=2)

# 결과창
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
