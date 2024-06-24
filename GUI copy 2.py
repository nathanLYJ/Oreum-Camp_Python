import tkinter as tk

def convert_temperature():
    celsius = float(entry.get())
    fahrenheit = celsius * 9 / 5 + 32
    result_label.config(text=f"{celsius} 섭씨 = {fahrenheit:.2f} 화씨")

# 기본 윈도우 생성 및 설정
root = tk.Tk()
root.title("온도 변환기")
root.geometry("300x150")

# 입력 필드와 레이블
entry = tk.Entry(root)
entry.pack(pady=10)

convert_button = tk.Button(root, text="섭씨 -> 화씨 변환", command=convert_temperature)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="변환 결과를 여기에 표시합니다.")
result_label.pack(pady=10)

# 메인 이벤트 루프 실행
root.mainloop()