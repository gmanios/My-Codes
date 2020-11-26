import tkinter as tk
from tkinter import filedialog
from matplotlib.widgets import TextBox
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

import pylustrator
from matplotlib.widgets import RadioButtons
def onclick(event):
    print("Wavelength:"+str(round(float(event.xdata)))+"|Value:"+str(round(float(event.ydata))))
    plt.title("Wavelength:"+str(round(float(event.xdata)))+"|Value:"+str(round(float(event.ydata))),loc='left')

global wavelength,wavelength2,max1,max2,text,plot,val


def get_offset(offset):
    return offset



def Sample_split2(f):
    global plot1,max1,graph2,offset,index,data,fig
    import os
    counter=0
    color=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--']
    pylustrator.start()
    fig, ax = plt.subplots()
    plt.grid()
    spectra_array = []
    plot_array=[]
    matrix_arr=[]
    name_arr=[]

    for f1 in f:
     counter+=1
     name=os.path.basename(f1)
     name_arr.append(name)
     file= open(f1, "r")  # read file


     list1 = list(file.readlines())  # list of lines
    # x1 y1     wavelength = []
     wavelength = []
     y2 = []
     y3=[]

     for lol in range(0, len(list1)):
        row = list1[lol]
        wavelength.append(float(row.split("\t")[0]))
        y2.append(float(row.split("\t")[1]))



     file.close()



     matrix = [[y2[k] for k in range(len(wavelength))]]


     matrix=np.array(matrix)
     matrix_arr.append((matrix))

     for i in range (len(matrix)):
         spectra_array.append(matrix[i])
         data = np.squeeze(matrix[i])

         plot1,=ax.plot(wavelength,data,label=name)


    spectra_array=np.array(spectra_array)
    matrix_arr=np.array(matrix_arr)
    data=np.array(data)
    # spectra_dict = dict(zip(plot_array, spectra_array))

    # plot_array=np.array(plot_array)

    plt.legend()
    plt.legend(loc="best")
    plt.ylabel('Value')
    plt.xlabel('Wavelength')

    axcolor = 'lightgoldenrodyellow'  # radio button window color
    plt.subplots_adjust(left =0.4)

    rax = plt.axes([0.05, 0.8, 0.15, 0.15], facecolor=axcolor)  # radio button window pos
    radio = RadioButtons(rax, name_arr)


    offset_value=0.005*max(data)



    def choose_spectra2(label):
        global index,offset
        offset=0
        hzdict = dict(zip(name_arr, spectra_array))
        ydata = hzdict[label]
        hzdict = list(hzdict)
        index = hzdict.index(label)
        plot1, = ax.plot(wavelength,data)
        ax.lines.remove(spectra_array[index])
        plot1.set_ydata(spectra_array[index])




        # plot1, = ax.plot(data)
        # plot1.set_ydata(spectra_array[index])
        # plot1, = ax.plot(data)
        # del ax.lines[index]
        # plot1, = ax.plot(data)
        # del ax.lines[index]

        plt.draw()

    radio.on_clicked(choose_spectra2)


    fig.canvas.mpl_connect('button_press_event', onclick)
    offset2=0

    def next2( event):
            global offset

            offset += offset_value
            ydata =offset



            plot1.set_ydata(spectra_array[index]+offset)
            plot1.set_alpha(0.5)
            plt.draw()

            print("Offset:" + str(offset))
            plt.title("Offset:" + str(offset),loc='left')

    def prev( event):
            global offset
            offset -=offset_value
            ydata = offset

            plot1.set_ydata(spectra_array[index] + offset)
            plot1.set_alpha(0.5)
            plt.draw()

            print("Offset:" + str(offset))
            plt.title("Offset:" + str(offset), loc='left')


    # 0.1, 0.0, 0.85, 0.075
    def on_key_press(event):
        if event.key == "w":
         next2(event)
        if event.key=="s":
         prev(event)

    fig.canvas.mpl_connect('key_press_event', on_key_press)


    plt.show()
    plt.close()







def Sample_split3(f):
    global plot1,max1,graph2,offset,index,data,fig
    import os
    counter=0
    color=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--']
    pylustrator.start()
    fig, ax = plt.subplots()
    plt.grid()
    spectra_array = []
    plot_array=[]
    matrix_arr=[]
    name_arr=[]

    for f1 in f:
     counter+=1
     name=os.path.basename(f1)
     name_arr.append(name)
     file= open(f1, "r")  # read file


     list1 = list(file.readlines())  # list of lines
    # x1 y1     wavelength = []
     wavelength = []
     y2 = []
     y3=[]

     for lol in range(0, len(list1)):
        row = list1[lol]
        wavelength.append(float(row.split("\t")[0]))
        y2.append(float(row.split("\t")[1]))



     file.close()



     matrix = [[y2[k] for k in range(len(wavelength))]]


     matrix=np.array(matrix)
     matrix_arr.append((matrix))

     for i in range (len(matrix)):
         counter=0
         spectra_array.append(matrix[i])
         data = np.squeeze(matrix[i])

         plot1,=ax.plot(wavelength,data,label=name)
         plot1.set_alpha(0.7)



    spectra_array=np.array(spectra_array)
    matrix_arr=np.array(matrix_arr)
    data=np.array(data)
    # spectra_dict = dict(zip(plot_array, spectra_array))

    # plot_array=np.array(plot_array)

    plt.legend()
    plt.legend(loc="best")
    plt.ylabel('Value')
    plt.xlabel('Wavelength')

    axcolor = 'lightgoldenrodyellow'  # radio button window color
    plt.subplots_adjust(left =0.4)

    rax = plt.axes([0.05, 0.8, 0.15, 0.15], facecolor=axcolor)  # radio button window pos
    radio = RadioButtons(rax, name_arr)


    offset_value=0.005*max(data)




    def choose_spectra2(label):
        global index,offset
        offset=0.02*max(data)
        hzdict = dict(zip(name_arr, spectra_array))
        ydata = hzdict[label]
        hzdict = list(hzdict)
        index = hzdict.index(label)
        plot1, = ax.plot(wavelength,data)
        ax.lines.remove(spectra_array[index])
        plot1.set_ydata(spectra_array[index] +offset )





        # plot1, = ax.plot(data)
        # plot1.set_ydata(spectra_array[index])
        # plot1, = ax.plot(data)
        # del ax.lines[index]
        # plot1, = ax.plot(data)
        # del ax.lines[index]

        plt.draw()

    radio.on_clicked(choose_spectra2)


    fig.canvas.mpl_connect('button_press_event', onclick)
    offset2=0

    def next2( event):
            global offset

            offset += offset_value
            ydata =offset


            plot1.set_ydata(spectra_array[index]+offset)
            plot1.set_alpha(0.5)
            plt.draw()

            print("Offset:" + str(offset))
            plt.title("Offset:" + str(offset),loc='left')

    def prev( event):
            global offset
            offset -=offset_value
            ydata = offset

            plot1.set_ydata(spectra_array[index] + offset)
            plot1.set_alpha(0.5)
            plt.draw()

            print("Offset:" + str(offset))
            plt.title("Offset:" + str(offset), loc='left')


    # 0.1, 0.0, 0.85, 0.075
    def on_key_press(event):
        if event.key == "w":
         next2(event)
        if event.key=="s":
         prev(event)

    fig.canvas.mpl_connect('key_press_event', on_key_press)


    plt.show()
    plt.close()





def Run2():
  filename=Import_File()
  pylustrator.start()

  Sample_split2(filename)  # Returns a raman_file and a photolum


def Run3():
  filename=Import_File()
  pylustrator.start()

  Sample_split3(filename)  # Returns a raman_file and a photolum




def Import_File(event=None):
    file_list=[]
    filename = filedialog.askopenfilenames()

    file_list.append(filename)



    return filename





def gui():
    # GUI
    root = tk.Tk()
    root.geometry("300x250")

    root.title("Multiple Spectra comparison tool  - @ 2020 FORTH IMBB - G.Manios")

    photo = PhotoImage(file=r"TIPP_LOGO.png")

    photoimage2 = photo.subsample(1, 1)
    button2= tk.Button(root, height=100, width=200, text='Plot multiple Spectra (SAMPLE) ', command=Run2, image=photoimage2,
                       compound=LEFT).pack(side=TOP)

    button1 = tk.Button(root, height=100, width=250, text='Plot multiple Raman Spectra (SAMPLE) ', command=Run3,
                        image=photoimage2,
                        compound=LEFT).pack(side=BOTTOM)
    label2 = tk.Label(text="Click to see a set of plots")
    label2.pack()




    root.mainloop()

gui()




