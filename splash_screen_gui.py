from cgi import test
from tkinter.ttk import Progressbar
from tkinter import *
from PIL import ImageTk, Image
from numpy import imag

w=Tk()

#Indicamos las dimensiones y posicion inicial del la pantalla de carga
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)

#Creamos la barra de progreso, su largo, color y orientacion(La parte que no carga)
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')  #Color gris de la barra
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)



#La ventana que llama despues de cargar el splash screen
def new_win():
  # w.destroy()
    q=Tk()
    q.title('Main window')
    q.geometry('427x250')
    l1=Label(q,text='ADD TEXT HERE ',fg='grey',bg=None)
    l=('Calibri (Body)',24,'bold')
    l1.config(font=l)
    l1.place(x=80,y=100)
    
    
    
    q.mainloop()


#Barra de progreso
def bar():

    l4=Label(w,text='Cargando...',fg='white',bg=MainWindow)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    w.destroy()
    #new_win()   #Llamamos a la otra ventana
        
    
progress.place(x=-10,y=235) #

#-----------------------Interfaz del splashScreen (Frame Principal)-------------------------
MainWindow='#800080'
Frame(w,width=427,height=241,bg=MainWindow).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='Iniciar',command=bar,border=0,fg=MainWindow,bg='white')
b1.place(x=170,y=200)


#-----------Labels-------------------------

l1=Label(w,text='Detector de mascarilla',fg='white',bg=MainWindow)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=100,y=80)


image = Image.open("images/mascarilla.png")
image = image.resize((50,50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
l2=Label(w,image=img,fg='white',bg=MainWindow)
l2.pack()
l2.place(x=40,y=80)

l3=Label(w,text='5T3-CO',fg='white',bg=MainWindow)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=100,y=110)


w.mainloop()


