from random import randrange


def verif(f,l,u,m,p,pv):
    if fname(f)!=None:
        return fname(f)
    elif lname(l)!=None:
        return lname(l)
    elif username(u)!=None:
        return username(u)
    elif password(p)!=None:
        return password(p)
    elif p!=pv:
        return "passwords do not match"
    else :
        return True



def fname(ch:str):
    for i in ch:
        if ch.isalpha()==False:
            return "first name must be alphabetical"
        elif len(ch)<2:
            return "sorry your first name is too short "
        elif  len(ch)>12:
            return "sorry you first name is too long"
        elif ch=="":
            return "first name are empty "
        else :
            return None

def lname(ch:str):
    for i in ch:
        if ch.isalpha()==False:
            return "last name must be alphabetical"
        elif len(ch)<2:
            return "sorry your last name is too short "
        elif  len(ch)>12:
            return "sorry you last name is too long"
        elif ch==None:
            return "last name are empty "
        else :
            return None

interdit="@/\-'\"&:;?!%£$+*|`^]})([{°"

def username(ch):
    for i in ch:
        if interdit.find(i)!=-1:
            return "pleas enter a readable "
        elif len(ch)<2:
            return "sorry your username is too short "
        elif len(ch)>15:
            return "sorry your username is too long "
        else :
            return None

def password(ch:str):
    if len(ch)<8:
        return "your password is too short"
    elif ch.isalnum() or ch.isalpha():
        return "try a difficult password"
    else:
        return None



def getcode():
    return randrange(100000,999999)