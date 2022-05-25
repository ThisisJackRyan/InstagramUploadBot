import pickle

accounts = []
l =len(accounts)

if l > 5:
    accounts.clear()
print(accounts)
a = input("add somthing")
accounts.append(a)
with open("accounts", "wb")as f:
    pickle.dump(accounts, f)

b = input("add somthing")
accounts.append(b)
with open("accounts", "wb")as f:
    pickle.dump(accounts, f)

with open("accounts", "rb")as f:
    pickle.load(f)

print(accounts)