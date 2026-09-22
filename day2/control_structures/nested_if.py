def studentLogin(hasAccount,hasVerified):
    hasAccount
    hasVerified
    if(hasAccount):
        if(hasVerified):
            print("Login Sucessfull")
        if(hasVerified is False):
            print("Has account but verification required.")
    else:
        print("He doesnot have an account")
studentLogin(True,False)