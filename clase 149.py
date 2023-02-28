from tkinter import*
import random
 
root=Tk()
 
root.title("Generador de palabras")
root.geometry("500x500")
root.configure(bg="blue")



label_1=Label(root,text="Generador de palabras")
label_1.place(relx=0.5 , rely=0.3, anchor=CENTER)
label_2=Label(root,text="aqui estoy")
label_2.place(relx=0.5 , rely=0.4, anchor=CENTER)

def palabra():
 alpha1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
random_no1= random.randint(1, 27)
random_alpha1=  alpha1[random_no1]
label_2["text"]=random_alpha1

  
button_1=Button(root , text="Dame click para generar la palabra" , bg="red", fg="white" , command=palabra)
button_1.place(relx=0.5 , rely=0.5 , anchor=CENTER)


    
root.mainloop()