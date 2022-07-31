def banner_text(text):
    width = 80
    if ( text == '*'):
        print(text * width)
    else:
        centered = text.center(width - 4)
        print("**{}**".format(centered))


banner_text('*')
banner_text("Nousi")
banner_text('*')

number = 5123537
print(f"{number:.4f}")
print(f"{number:,}")
print(f"{number:,.3f}")
print(f"{number:.0f}")
print(f"{number:12.1f}")