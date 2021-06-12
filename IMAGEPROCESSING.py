
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from PIL import ImageEnhance 
from PIL import ImageFilter 
#extra from tkinter 
import ttk as tkinter.ttk 
import * import tkinter.filedialog 
#height width of canvas 
HEIGHT = 200 
WIDTH = 200 
window = tk.Tk() 
#styling button and labels all at one time 
style = ttk.Style() 
style.configure("TButton",foreground='IndianRed1',background="white") style.configure("TLabel",foreground='blue2') 
#functions for filter 
def select_image(): 
	path = tk.filedialog.askopenfilename(parent=window,initialdir='C:/imageselection',title='choose image',
    filetypes=[('jpg images','.jpg')]) 
    print(path) 
    im = Image.open(path)
    tkimage = ImageTk.PhotoImage(im) return path 
def action1():
	enhancer2 = ImageEnhance.Color(img1) 
    enhancer2.enhance(0).save('baw.jpg') 
    enhancer2.show()
def action2(): 
	enhancer1 = ImageEnhance.Brightness(img1) 
    enhancer1.enhance(3).save('brightness.jpg') 
    enhancer1.show()
def action3():
	enhancer3 = ImageEnhance.Contrast(img1)         
    enhancer3.enhance(3).save('contrast.jpg') 
    enhancer3.show() 
def action4():
  enhancer4 = img1.filter(ImageFilter.BoxBlur(10))
   enhancer4.show() 
def action5(): 
	enhancer5 = img1.filter(ImageFilter.EMBOSS) 
	enhancer5.show() 
	enhancer5.save('emboss.jpg') 
def action6(): 
	enhancer6 = img1.filter(ImageFilter.CONTOUR)
	 enhancer6.show() 
	 enhancer6.save('contour.jpg') 
def action7(): 
	enhancer7 = img1.filter(ImageFilter.SMOOTH_MORE) 
    enhancer7.show() 
    enhancer7.save('smooth.jpg') 
def action8(): 
	enhancer8 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE) 
	enhancer8.show() 
	enhancer8.save('imageenhance.jpg') 
def action9(): 
    enhancer9 = ImageEnhance.Color(img1) 
    enhancer9.enhance(2).save('image.jpg') #function for second window def open_window(): top = Toplevel() top.title("image filters gui app") 
Label(top, text = 'IMAGE MAGICK', font =('Verdana', 10)).grid(column=1,row=0) 
Label(top, text = '1.please select the filter you would like to apply on the image\n2.press exit to quit').grid(column=1,row=1) 
button1 = Button(top,text="EXIT",command=top.destroy).grid(column=1,row=5) 
button2 = Button(top,text="brightness",command=action2).grid(column=1,row=6)
button3 = Button(top,text="black and white",command=action1).grid(column=1,row=7) 
button4 = Button(top,text="contrast",command=action3).grid(column=1,row=8) 
button5 = Button(top,text="blurred",command=action4).grid(column=1,row=9) 
button6 = Button(top,text="emboss",command=action5).grid(column=1,row=10) 
button7 = Button(top,text="contour",command=action6).grid(column=1,row=11) 
button8 = Button(top,text="smooth",command=action7).grid(column=1,row=12) 
button9 = Button(top,text="enhance_edge",command=action8).grid(column=1,row=13)
button10 = Button(top,text="increase_color",command=action9).grid(column=1,row=14) 
x = select_image() 
img1 = Image.open(x)
window.title("image magic") 
canvas = tk.Canvas(window,height=HEIGHT,width=WIDTH) 
canvas.grid(row=0,column=0) 
#.pack() frame = tk.Frame(window,bg='red') frame.place(relx=0.0,rely=0.0,relwidth=8,relheight=8) 
#lets start button button15=tk.Button(window,text="LETSSTART",bg='gray',fg='yellow',command=open_window,height=0,width=12) button15.grid(row=129,column=69,sticky=W,pady=1) #exit button button100=Button(window,text="EXIT",command=window.destroy).grid(column=59,row=110) 
#main label Label(window, text = 'IMAGE MAGICK', font =('Verdana', 35)).grid(column=59,row=0) label38 = ttk.Label(window,text="1.press lets start button to add filter on the image").grid(row=65,column=59) label77 = ttk.Label(window,text="2.press quit to exit from the window").grid(row=75,column=59) #button456 = tk.Button(window,text="select image",command=select_image,height=0,width=12) #button456.grid(row=59,column=99,sticky=W) 
window.mainloop()

