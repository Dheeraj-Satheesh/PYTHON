h=int(input())
if h<8:
    print("Invaild input")
elif h<12:
    s=(100*(h-8)+200)
    print(s)
elif h<16:
    s=(400+(200*(h-12))+200)
    print(s)
else:
    s=(1200+200+(250*(h-16)))
    print(s)

