import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from math import sin, cos, pi

#specificly designed entry function with option to limit input(from=...,to=...)
class LimitedFloatEntry(tk.Entry):
    '''A new type of Entry widget that allows you to set limits on the entry'''
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar(master, 0)
        self.var.trace('w', self.validate)
        self.get = self.var.get
        self.from_  = kwargs.pop('from_', 0)
        self.to = kwargs.pop('to', 1)
        self.old_value = 0
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)

    def validate(self, *args):
        try:
            value = self.get()
            # special case allows for an empty entry box
            if value not in ('', '-') and not self.from_ <= float(value) <= self.to:
                raise ValueError
            self.old_value = value
        except ValueError:
            self.set(self.old_value)

    def set(self, value):
        self.delete(0, tk.END)
        self.insert(0, str(value))

def check1():
    reinf_diam = entry2.get()
    reinf_numb = entry3.get()
    try:
        reinf_diam = float(reinf_diam)
        reinf_numb = float(reinf_numb)
    except:
        reinf_diam = 0.0
        reinf_numb = 0.0
    
    if reinf_diam == 0.0 or reinf_numb == 0.0:
        label7_result.config(text="Plese insert values")
    elif float(reinf_diam) >= 12 and float(reinf_numb) >= 4:
        label7_result.config(text="OK"+u'\u2714'+"(" + str(round(int(reinf_numb),0))+u'\u03D5'+ str(round(int(reinf_diam),2)) +")")
    elif float(reinf_diam) < 12 or float(reinf_numb) < 4:
        label7_result.config(text="Error"+u'\u2716'+"(" + str(round(int(reinf_numb),0))+u'\u03D5'+ str(round(int(reinf_diam),2)) +")")

def check2():     
    pile_diam = entry1.get()
    reinf_diam = entry2.get()
    reinf_numb = entry3.get()
    cover = entry4.get()
    try:
        pile_diam = float(pile_diam)
        reinf_diam = float(reinf_diam)
        reinf_numb = float(reinf_numb)
        cover = float(cover)
    except:
        pile_diam = 0.0
        reinf_diam = 0.0
        reinf_numb = 0.0
        cover = 0.0
    
    if pile_diam == 0.0 or reinf_diam == 0.0 or reinf_numb == 0.0 or cover ==0.0:
        label8_result.config(text="Plese insert values")
    elif ((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb <= 400:
        bar_spacing = ((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb
        label8_result.config(text="OK"+u'\u2714'+"(" + str(round(bar_spacing,2)) +"mm)")
    elif ((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb > 400:
        bar_spacing = ((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb
        label8_result.config(text="Error"+u'\u2716'+"(" + str(round(bar_spacing,2)) + "mm)")
        
def check3():     
    pile_diam = entry1.get()
    reinf_diam = entry2.get()
    reinf_numb = entry3.get()
    cover = entry4.get()
    try:
        pile_diam = float(pile_diam)
        reinf_diam = float(reinf_diam)
        reinf_numb = float(reinf_numb)
        cover = float(cover)
    except:
        pile_diam = 0.0
        reinf_diam = 0.0
        reinf_numb = 0.0
        cover = 0.0
    
    if pile_diam == 0.0 or reinf_diam == 0.0 or reinf_numb == 0.0 or cover ==0.0:
        label9_result.config(text="Plese insert values")
    elif var1.get() == 1 and (((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb)-reinf_diam >= 80:
        bar_spacing1 = (((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb)-reinf_diam
        label9_result.config(text="OK"+u'\u2714'+"(" + str(round(bar_spacing1,2)) + "mm)")
    elif var1.get() == 0 and (((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb)-reinf_diam >= 100:
        bar_spacing1 = (((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb)-reinf_diam
        label9_result.config(text="OK"+u'\u2714'+"(" + str(round(bar_spacing1,2)) + "mm)")   
    else:
        bar_spacing1 = (((((pile_diam / 2)*1000) - cover - (reinf_diam / 2))*2*3.1415)/reinf_numb)-reinf_diam
        label9_result.config(text="Error"+u'\u2716'+"(" + str(round(bar_spacing1,2)) + "mm)")     

def check4():     
    cover = entry4.get()
    try:
        cover = float(cover)
    except:
        cover = 0.0
    if cover == 0.0:
        label10_result.config(text="Plese insert values")
    elif cover >= 75:
        label10_result.config(text="OK"+u'\u2714'+"(" + str(cover) + "mm)")
    else:
        label10_result.config(text="Error"+u'\u2716'+"(" + str(cover) + "mm)")
def check5():     
    pile_diam = entry1.get()
    reinf_diam = entry2.get()
    reinf_numb = entry3.get()
    try:
        pile_diam = float(pile_diam)
        reinf_diam = float(reinf_diam)
        reinf_numb = float(reinf_numb)
    except:
        pile_diam = 0.0
        reinf_diam = 0.0
        reinf_numb = 0.0
    
    if pile_diam == 0.0 or reinf_diam == 0.0 or reinf_numb == 0.0:
        label11_result.config(text="Plese insert values")
    elif 3.1415*((pile_diam/2)**2) <=0.5 and 3.1415*((reinf_diam/2)**2)*reinf_numb >= 0.005*3.1415*(((pile_diam/2)*1000)**2):
        area_of_reinf = 3.1415*((reinf_diam/2)**2)*reinf_numb
        label11_result.config(text="OK"+u'\u2714'+"(" + str(round(area_of_reinf,1)) +"mm^2)")
    elif 3.1415*((pile_diam/2)**2) <= 1 and 3.1415*((pile_diam/2)**2) > 0.5 and 3.1415*(((reinf_diam/2)/1000)**2)*reinf_numb >= 0.0025:
        area_of_reinf = 3.1415*((reinf_diam/2)**2)*reinf_numb
        label11_result.config(text="OK"+u'\u2714'+"(" + str(round(area_of_reinf,1)) +"mm^2)")
    elif 3.1415*((pile_diam/2)**2) > 1 and 3.1415*((reinf_diam/2)**2)*reinf_numb >= 0.0025*3.1415*(((pile_diam/2)*1000)**2):
        area_of_reinf = 3.1415*((reinf_diam/2)**2)*reinf_numb
        label11_result.config(text="OK"+u'\u2714'+"(" + str(round(area_of_reinf,1)) + "mm^2)")    
    else:
        area_of_reinf = 3.1415*((reinf_diam/2)**2)*reinf_numb
        label11_result.config(text="Error"+u'\u2716'+"(" + str(round(area_of_reinf,1)) + "mm^2)")
def check6():     
    pile_diam = entry1.get()
    reinf_diam = entry2.get()
    reinf_numb = entry3.get()
    try:
        pile_diam = float(pile_diam)
        reinf_diam = float(reinf_diam)
        reinf_numb = float(reinf_numb)
    except:
        pile_diam = 0.0
        reinf_diam = 0.0
        reinf_numb = 0.0
        cover = 0.0
    
    if pile_diam == 0.0 or reinf_diam == 0.0 or reinf_numb == 0.0:
        label12_result.config(text="Plese insert values")
    elif 3.1415*((reinf_diam/2)**2)*reinf_numb <= 0.04*3.1415*(((pile_diam/2)*1000)**2) and var2.get() == 0:
        area_of_reinf_percentage = ((3.14159*((reinf_diam/2)**2)*reinf_numb) / (3.1415*(((pile_diam/2)*1000)**2)))*100
        label12_result.config(text="OK"+u'\u2714'+"(" + str(round(area_of_reinf_percentage,2)) + "%)")
    elif 3.1415*((reinf_diam/2)**2)*reinf_numb <= 0.08*3.1415*(((pile_diam/2)*1000)**2) and var2.get() == 1:
        area_of_reinf_percentage = ((3.14159*((reinf_diam/2)**2)*reinf_numb) / (3.1415*(((pile_diam/2)*1000)**2)))*100
        label12_result.config(text="OK"+u'\u2714'+"(" + str(round(area_of_reinf_percentage,2)) + "%)")
    else:
        area_of_reinf_percentage = ((3.14159*((reinf_diam/2)**2)*reinf_numb) / (3.1415*(((pile_diam/2)*1000)**2)))*100
        label12_result.config(text="Error"+u'\u2716'+"(" + str(round(area_of_reinf_percentage,2)) +"%)")  
#centering entire window
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()



def plot():
    pile_diam = entry1.get()
    reinf_diam = entry2.get()
    reinf_numb = entry3.get()
    cover = entry4.get()
    try:
        pile_diam = float(pile_diam)
        reinf_diam = float(reinf_diam)
        reinf_numb = int(reinf_numb)
        cover = float(cover)
    except:
        pile_diam = 0.0
        reinf_diam = 0.0
        reinf_numb = 0
        cover = 0.0
    
    # Clear the existing plot
    if plt.fignum_exists(1) == True:
        for widgets in frm_form1.winfo_children():
            widgets.destroy()
    else:
        None    
    # Create the figure that will contain the plot
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    
    # Plot the outer circle
    circle = plt.Circle((0, 0), pile_diam / 2, color='black', fill=False)
    ax.add_patch(circle)
    
    if reinf_numb == 0:
        angle = 0
    else:
        angle = (2 * pi) / reinf_numb

    # Plot the smaller circles
    for i in range(reinf_numb):
        x = (pile_diam / 2 - (cover/1000 + reinf_diam / 2000)) * cos(i * angle)
        y = (pile_diam / 2 - (cover/1000 + reinf_diam / 2000)) * sin(i * angle)
        smaller_circle = plt.Circle((x, y), reinf_diam / 2000, color='red', fill=False)
        ax.add_patch(smaller_circle)
    # Set axis limits
    if pile_diam > 0:
        plt.ylim(-(pile_diam/2)*1.1, (pile_diam/2)*1.1)
        plt.xlim(-(pile_diam/2)*1.1, (pile_diam/2)*1.1)
    else:
        plt.ylim(-0.4, 0.4)
        plt.xlim(-0.4, 0.4)
    ax.set_aspect('equal')
        
    # Create the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frm_form1)
    canvas.draw()

    # Place the canvas on the Tkinter window
    canvas.get_tk_widget().pack() 

#added function to quit upon exiting window, bug is caused by matplotlib
def quit_me():
    window.quit()
    window.destroy()

#input red if wrong, green if ok
def check_value(entry, min_value, max_value):
    try:
        value = float(entry.get().strip())
        valid = min_value <= value <= max_value
    except ValueError:
        valid = False
    entry.config(fg='green' if valid else 'red')
    return valid  # in case you want the checking result somewhere else
    
if __name__ == '__main__':
    window = tk.Tk()
    window.title("Longitudinal reinforcement check for circular piles")
    window.geometry("1300x330")
    window.resizable(0, 0)
    center(window)
    #added to kill python code when exiting window, bug with matplotlib see stackoverflow
    window.protocol("WM_DELETE_WINDOW", quit_me)
# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information

#graph frame
frm_form1 = tk.Frame(master=window, width=600, height=400, borderwidth=10, relief="ridge")
frm_form1.pack(side= tk.LEFT)
#input frame
frm_form = tk.Frame(master=window, width=200, height=100, borderwidth=10)
frm_form.pack(side= tk.TOP)
#results frame
frm_form2 = tk.Frame(master=window, width=700, height=250, borderwidth=10)
frm_form2.pack(side= tk.TOP, expand=True, fill="both")



label1 = tk.Label(master=frm_form, text="Pile diameter:")
label1.grid(sticky="W", row=0,column=0)
entry1 = LimitedFloatEntry(master=frm_form,width=5, from_=0.0, to=1.2)
entry1.grid(row=0,column=1)
entry1.bind('<KeyRelease>', lambda e: check_value(e.widget, 0.3, 1.2))
label1_units = tk.Label(master=frm_form,width=1 , text="m")
label1_units.grid(row=0,column=2)

label2 = tk.Label(master=frm_form, text="Reinforcement diameter:")
label2.grid(sticky="W", row=1,column=0)
entry2 = LimitedFloatEntry(master=frm_form,width=5, from_=0.0, to=50.0)
entry2.grid(row=1,column=1)
entry2.bind('<KeyRelease>', lambda e: check_value(e.widget, 6, 50))
label2_units = tk.Label(master=frm_form,width=4 , text="mm")
label2_units.grid(row=1,column=2)

label3 = tk.Label(master=frm_form, text="Number of reinfocement bars:")
label3.grid(sticky="W", row=2,column=0)
entry3 = LimitedFloatEntry(master=frm_form,width=5, from_=0.0, to=30.0)
entry3.grid(row=2,column=1)
entry3.bind('<KeyRelease>', lambda e: check_value(e.widget, 3, 22))
label3_units = tk.Label(master=frm_form,width=4 , text="-")
label3_units.grid(row=2,column=2)

label4 = tk.Label(master=frm_form, text="Cover thickness:")
label4.grid(sticky="W", row=3,column=0)
entry4 = LimitedFloatEntry(master=frm_form,width=5, from_=0.0, to=400)
entry4.grid(row=3,column=1)
entry4.bind('<KeyRelease>', lambda e: check_value(e.widget, 1, 300))
label4_units = tk.Label(master=frm_form,width=4 , text="mm")
label4_units.grid(row=3,column=2)

label5 = tk.Label(master=frm_form, text="Maximum size of aggregate <= 20mm?*")
label5.grid(sticky="W", row=4,column=0)
var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(master=frm_form, text='',variable=var1, onvalue=1, offvalue=0, command="")
checkbox1.grid(row=4,column=1)

label6 = tk.Label(master=frm_form, text="Longitudinal reinforcement overlapping?")
label6.grid(sticky="W", row=5,column=0)
var2 = tk.IntVar()
checkbox2 = tk.Checkbutton(master=frm_form, text='',variable=var2, onvalue=1, offvalue=0, command="")
checkbox2.grid(row=5,column=1)

#Button to start calculations

pile_diam = entry1.get()
try:
    pile_diam = float(pile_diam) * 1000
except:
    pile_diam = 0.0

btn_check = tk.Button(
    master=frm_form,
    text="Check conditions",
    height=1,
    command=lambda: [check1(), check2(), check3(), check4(), check5(), check6(),plot()] 
)
btn_check.grid(row=6,column=1)

#RESULTS PLACEMENT

label7_result = tk.Label(master=frm_form2, text="")
label7_result.grid(sticky="W", row=0,column=1)
label8_result = tk.Label(master=frm_form2, text="")
label8_result.grid(sticky="W", row=1,column=1)
label9_result = tk.Label(master=frm_form2, text="")
label9_result.grid(sticky="W", row=2,column=1)
label10_result = tk.Label(master=frm_form2, text="")
label10_result.grid(sticky="W", row=3,column=1) 
label11_result = tk.Label(master=frm_form2, text="")
label11_result.grid(sticky="W", row=4,column=1)
label12_result = tk.Label(master=frm_form2, text="")
label12_result.grid(sticky="W", row=5,column=1)


#NORM CONDITIONS labels and positions
label7 = tk.Label(master=frm_form2, text="BS EN 1536, Section 7.5.2: Minimum logitudinal reinforcement shall be 4 bars of min. 12mm")
label7.grid(sticky="W", row=0,column=0)

label8 = tk.Label(master=frm_form2, text="BS EN 1536, Section 7.5.2: Spacing of longitudinal bars should not exceed 400mm")
label8.grid(sticky="W", row=1,column=0)

label9 = tk.Label(master=frm_form2, text="BS EN 1536, Section 7.5.2: Horizontal clear distance between bars not less than 100mm/80mm*")
label9.grid(sticky="W", row=2,column=0)

label10 = tk.Label(master=frm_form2, text="BS EN 1536, Section 7.7.3: Recommended minimum cover in relation to execution(min. 75mm)")
label10.grid(sticky="W", row=3,column=0)

label11 = tk.Label(master=frm_form2, text="BS EN 1536, Section 7.5.2: Minimum area of longitudinal reinforcement As")
label11.grid(sticky="W", row=4,column=0)

label12 = tk.Label(master=frm_form2, text="BS EN 1992-1-1, Section 9.5.2: Maxiumum area of longitudinal reinforcement in columns As_max")
label12.grid(sticky="W", row=5,column=0)

window.mainloop()