import tkinter as tk

def on_button_click():
    label.config(text="버튼을 클릭했습니다!")
    entry_text = entry.get()
    label.config(text=f"입력한 텍스트: {entry_text}")

# 창 생성
root = tk.Tk()
root.title("Tkinter 예제")

# 레이블 설정
label = tk.Label(root, text="여기에 텍스트가 표시됩니다", font=("Helvetica", 16), bg="yellow", fg="blue")
label.pack(padx=20, pady=20)

# 버튼 설정
button = tk.Button(root, text="클릭하세요", command=on_button_click, bg="blue", fg="white")
button.pack(padx=10, pady=10)

# 입력 필드 설정
entry = tk.Entry(root, show="*", width=50)
entry.pack(padx=10, pady=10)

# 창 실행
root.mainloop()