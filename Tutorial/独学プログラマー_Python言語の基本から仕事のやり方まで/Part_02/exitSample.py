import sys
import time

while True:
    print("終了するにはexitと入力してください。")
    response = input()
    print(response + "と入力されました")
    time.sleep(3)
    if response == "exit":
        print("終了します")
        time.sleep(3)
        sys.exit()
    
