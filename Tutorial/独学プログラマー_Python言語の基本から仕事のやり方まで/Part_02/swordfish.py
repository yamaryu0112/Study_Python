while True:
    print("あなたは誰？")
    name = input()
    if name != "Joe":
        continue
    print("こんにちは、Joe。パスワードは何？")
    password = input()
    if password == "swordfish":
        break
print("認証しました。")
