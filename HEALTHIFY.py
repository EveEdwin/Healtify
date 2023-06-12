print(":::::::::::::::::::::>>WELCOME TO HEALTHIFY<<:::::::::::::::::::::")
print("\n1. Register yourself\n2. Login\n")
def main():
    global b
    b=int(input("Enter your choice"))

a=0
s=0
def ch():
    print("\n1. Disease Diagnosis\n2. Exit\n")
    global s
    i=input("Enter your choice :")
    if i=="1" or i=="1." or i=="Disease Diagnosis":
        s=0
        print(dis())
    elif i=="2" or i=="2." or i=="Exit":
        s=0
        print("::::::::::::::::>>THANK YOU FOR USING HEALTHIFY<<:::::::::::::::::")
    else:
        s=1
        print("Enter a valid choice")

              
#login

def login():
    print("\n:::::::::::::::::::::>>LOGIN<<:::::::::::::::::::::\n")
    pw=int(input("Enter your id"))
    import pickle
    search=[pw]
    info={}
    data = open(r"C:\Users\DELL\OneDrive\Desktop\login.dat","rb")
    try:
        while True:
            info = pickle.load(data)         
            if info['id'] in search:
                global user
                user = info["Name"]
                print("\n::::::::::::::::>>WELCOME", info["Name"].upper(),"<<:::::::::::::::::\n")
                ch()
                break
            '''
            else:
                print("\t\t\t:>>Invalid ID<<:")
                print("\t\t\tREGISTER YOURSELF\n")
                break'''
    except:
        print("\t\t\t:>>Invalid ID<<:")
        print("\t\t\tREGISTER YOURSELF\n")
        data.close()
        registration()
    

#Register yourself

def registration():
    print("\n:::::::::::::::::::::>>REGISTRATION<<:::::::::::::::::::::\n")
    import pickle
    info= {}
    data=open(r"C:\Users\DELL\OneDrive\Desktop\login.dat",'ab')
    while True:
        info["Name"] = input("Enter name")
        info["Phone Number"] = int(input("Enter phone number"))
        info["age"] = int(input("Enter age"))
        import time
        idno = int(time.time()) 
        info["id"] = idno
        pickle.dump(info,data)
        print("\nYour id is - ",idno,".Kindly note it down.")
        break
    data.close()
    login()
    





def search():
    import pickle
    found=False
    dis={}
    disfile=open(r"C:\Users\DELL\OneDrive\Desktop\med.dat","rb")
    try:
        while True:
            dis=pickle.load(disfile)
            
            if dis["Disease"]==c.lower():
                for key in dis:
                    print(key,"\t:\t",dis[key],"\n")
                    found=True
    except:
        if found==False:
            print("No such result found")
        else:
            print("Search successful")    
        print("\n::::::::::::::::::::>>HEALTHIFY<<:::::::::::::::::::::")
        disfile.close()
        ch()
def dis():
    global c
    print("\n")
    c=input("Enter your disease")
    search()
    return("\n:::::::::::::::::::>>HEALTHIFY<<:::::::::::::::::::::")
    '''
    print("\n1. Chickenpox\n2. HIV/AIDS\n3. Smallpox\n4. Dengue\n5. Malaria\n6. Any other disease\n")
    global v
    global c
    j=input("Select your Disease :")
    if j=="1" or j=="1.":
        v=0
        print("\nMEDICATION\nAcyclovir (Zovirax, Sitavig)\nValacyclovir (Valtrex) and famciclovir\n\nAdults: 1 adult tablet daily.\nChildren:½ pediatric tablet daily.\n")
    elif j=="2" or j=="2.":
        v=0
        print("\nMEDICATION\nAbacavir, or ABC (Ziagen)\t300 mg twice daily or 600 mg once daily\nDidanosine, or ddl (Videx)\t200 mg once daily\nEmtricitabine, or FTC (Emtriva)\t150 mg twice daily or 300 mg once daily\nLamivudine, or 3TC (Epivir)\t250–300 mg twice daily\nStavudine, or d4T (Zerit)\t300 mg once daily\n")
    elif j=="3" or j=="3.":
        v=0
        print("\nTREATMENT\nNo cure or treatment for smallpox exists. A vaccine can prevent smallpox, but the risk of the vaccine's side effects is too high to justify routine vaccination for people at low risk of exposure to the smallpox virus.\n")
    elif j=="4" or j=="4.":
        v=0
        print("\nMEDICATION\nThere is no specific medicine to treat dengue.\nTreat the symptoms of dengue and see your healthcare provider.\n")
    elif j=="5" or j=="5.":
        v=0
        print("\nMEDICATION\nAtovaquone-proguanil (Malarone)\nQuinine sulfate (Qualaquin) with doxycycline (Oracea, Vibramycin, others)\nPrimaquine phosphate\n\nAdults: 1 adult tablet daily.\nChildren:½ pediatric tablet daily.\n")
    elif j=="6" or j=="6.":
        v=0
'''
        
        
        #print("\nMEDICATION\nAspirin or Ibuprofen (Advil, Motrin IB)\t300 mg twice daily\nAcetaminophen (Excedrin Migraine)\t600 mg once daily\nSumatriptan (Imitrex, Tosymra)\t\t200 mg once daily\n")
'''
def sym():
    symp=input("Enter your symptom: ")
    choice=input("More sypmtoms Yes/No(Y/N)")
    while choice not in "nN":
        symp=input("Enter your symptom: ")
        choice=input("More sypmtoms Yes/No(Y/N)")
       
def dia():
    print("\n1. On the basis of symptoms\n2. On the basis of disease\n")
    global a
    j=input("Enter your choice :")
    if j=="1" or j=="1.":
        a=0
        print(sym())
    elif j=="2" or j=="2.":
        a=0
        print(dis())
    else:
        a=1
        print("Enter a valid choice")

'''
main()
if b==1:
    registration()
elif b==2:
    
    login()
else :
    print("Enter a valid choice")
    main()


'''
ch()

while s==1:
    ch()


while a==1:
    dia()
'''
