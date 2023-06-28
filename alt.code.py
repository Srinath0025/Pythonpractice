sub=" subject"
mk=" mark"
t=" tamil"
tm=" 98"
e=" english"
en=" 88"
m=" maths"
ms=" 95"
s=" science"
sc=" 92"
so=" social"
soc=" 99"
print(f"╔{'═'*10}╦{'═'*10}╗")
print(f"║{sub}{' '*(10-len(sub))}║{mk}{' '*(10-len(mk))}║")
print(f"╠{'═'*10}╬{'═'*10}╣")
print(f"║{t}{' '*(10-len(t))}║{tm}{' '*(10-len(tm))}║")
print(f"║{e}{' '*(10-len(e))}║{en}{' '*(10-len(en))}║")
print(f"║{m}{' '*(10-len(m))}║{ms}{' '*(10-len(ms))}║")
print(f"║{s}{' '*(10-len(s))}║{sc}{' '*(10-len(sc))}║")
print(f"║{so}{' '*(10-len(so))}║{soc}{' '*(10-len(soc))}║")
print(f"╠{'═'*10}╬{'═'*10}╣")
print(f"║{' '*10}║{' '*10}║")
print(f"╚{'═'*10}╩{'═'*10}╝")

a=input("enter the value")
print(type(a))
b=int(input("enter the value"))
print(type(b))
