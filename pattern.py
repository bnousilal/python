str="python"

def banner_text(text, width=80): #width = 80 is default parameter
    if ( text == '*'):
        print(text * width)
    else:
        centered = text.center(width - 4)
        print("**{}**".format(centered))


banner_text('*', 80)
banner_text("Nousi", 80)
banner_text('*', 80)

list=[str[:i] for i in range(1,len(str)+1)]
j = 0
for i in list:
    print(f'{i*(len(i)):^40}')