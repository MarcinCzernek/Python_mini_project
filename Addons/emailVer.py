from verify_email import verify_email

def message(text, end="\n"):
    print(f">>>{text}",end=end)

message("Adres Email:",end="")
mail=input()
if mail in["",None]:
    message("Please enter email address")
    exit()

if verify_email(mail):
    message(f"Email {mail} exists!")
else:
    message(f"Email {mail} not exists")