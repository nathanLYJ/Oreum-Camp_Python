import tkinter as tk

# 기본 윈도우 생성
root = tk.Tk()

# 윈도우 이름 설정
root.title("My World!")

# 윈도우 크기 설정
root.geometry("640x480")

# 레이블 위젯 추가
label = tk.Label(root, text = 'Tkinter install')
label.pack()

# 버튼 위젯 추가 - 동작에 대한 기능 구현
def on_click():
  print('click button')

# 텍스트 입력을 위한 입력 필드 생성
entry = tk.Entry(root)
entry.pack()

# 입력 필드의 내용을 가져와서 출력하는 함수
def get_text():
  print(entry.get())

# 입력 내용을 출력하는 버튼
button1 = tk.Button(root, text = 'enter', command=get_text)
button1.pack()


# 동작을 수행하는 버튼!
button = tk.Button(root, text = 'Click me', command = on_click)
button.pack()

# 메인 이벤트 루프 생성
root.mainloop()