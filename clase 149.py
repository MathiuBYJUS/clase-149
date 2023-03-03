from tkinter import*
import random
 
root=Tk()
 
root.title("Generador de palabras")
root.geometry("500x500")
root.configure(bg="blue")



label_1=Label(root,text="Generador de palabras")
label_1.place(relx=0.5 , rely=0.3, anchor=CENTER)
label_2=Label(root,text="a")
label_2.place(relx=0.5 , rely=0.4, anchor=CENTER)



def palabra():
  alpha1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  random_no1 = random.randint(1, 26)
  random_alpha1 =  alpha1[random_no1]
  random_no2 = random.randint(1, 26)
  random_alpha2 = alpha1[random_no2]
  random_no3 = random.randint(1, 26)
  random_alpha3 = alpha1[random_no3]
  label_2["text"] = random_alpha1 + random_alpha2 + random_alpha3

         
   

  
button_1=Button(root , text="Dame click para generar la palabra" , command=palabra , bg="red", fg="white") 
button_1.place(relx=0.5 , rely=0.5 , anchor=CENTER)


    
root.mainloop()  