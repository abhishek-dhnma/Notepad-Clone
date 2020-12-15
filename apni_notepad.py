import tkinter as tk #window create hoga esse
from tkinter import ttk 
from tkinter import font ,colorchooser,filedialog,messagebox 
import os   #for read, write, save files or data




main_application = tk.Tk() 
main_application.geometry("800x800")  #Size k liya
main_application.title("Apni Notepad")  #Opening Window ka size



main_menu = tk.Menu() # ye humara MAIN MENU HAI 


#ICONS ICONS ICONS ICONS ICONS 

new_icon = tk.PhotoImage(file = "Icons/new.png")
open_icon = tk.PhotoImage(file = "Icons/open.png")
save_icon = tk.PhotoImage(file = "Icons/save.png")
saveas_icon = tk.PhotoImage(file = "Icons/save-as.png")
exit_icon = tk.PhotoImage(file = "Icons/exit.png")

copy_icon = tk.PhotoImage(file = "Icons/copy.png")
paste_icon = tk.PhotoImage(file ="Icons/paste.png")
cut_icon = tk.PhotoImage(file = "Icons/cut.png")

tool_bar = tk.PhotoImage(file = "Icons/tool-box.png")
status_bar = tk.PhotoImage(file = "Icons/view.png")

dark_theme = tk.PhotoImage(file = "Icons/oval.png")
light_theme = tk.PhotoImage(file = "Icons/dry-clean.png")





#Creating Sub-Menus 
file = tk.Menu(main_menu, tearoff = False)#tearoff for Dropdown menu nhi bahar nikalega
Edit = tk.Menu(main_menu,tearoff = False)
View = tk.Menu(main_menu,tearoff = False)
colour_theme = tk.Menu(main_menu, tearoff = False)




main_menu.add_cascade(label = "File" ,menu = file)
main_menu.add_cascade(label = "Edit", menu = Edit)
main_menu.add_cascade(label= "View", menu = View)
main_menu.add_cascade(label= "Themes", menu = colour_theme)

#Colour Theme Hex Values 
theme_choose = tk.StringVar()
colour_icon = (light_theme, dark_theme)
colour_dict = {
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Light': ('#000000', '#ffffff')
    }








# SECOND LABEL
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side = tk.TOP, fill = tk.X)

## FONT BOX  
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label, width = 30, textvariable = font_family, state = "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row = 0, column = 0, padx = 5, pady = 5)


##  SIZE BOX

size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width = 20, textvariable = size_variable, state = "readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(2)
font_size.grid(row=0, column =1, padx = 5)


## BOLD BUTTON
bold_icon = tk.PhotoImage(file = "Icons/bold.png")
bold_btn = ttk.Button(tool_bar_label, image  = bold_icon)
bold_btn.grid(row=0, column = 2, padx = 5)



## ITALIC BUTTON

italic_icon = tk.PhotoImage(file = "Icons/italic.png")
italic_btn = ttk.Button(tool_bar_label, image = italic_icon)
italic_btn.grid(row = 0, column = 3, padx = 5)

## UNDERLINE BUTTON

underline_icon = tk.PhotoImage(file = "Icons/underline.png")
underline_btn = ttk.Button(tool_bar_label, image = underline_icon)
underline_btn.grid(row = 0, column = 4, padx = 5)

##  FONT COLOUR CHANGER

font_colour_icon  = tk.PhotoImage(file = "Icons/colour-changer.png")
font_colour_btn = ttk.Button(tool_bar_label, image = font_colour_icon)
font_colour_btn.grid(row = 0, column = 5, padx = 5)


##  LEFT ALIGN

left_aligh_icon = tk.PhotoImage(file = "Icons/left-align.png")
left_aligh_btn = ttk.Button(tool_bar_label, image = left_aligh_icon)
left_aligh_btn.grid(row = 0, column = 6, padx = 6)

## CENTER ALIGN
Center_align_icon = tk.PhotoImage(file = "Icons/center-align.png")
Center_align_btn = ttk.Button(tool_bar_label, image = Center_align_icon)
Center_align_btn.grid(row = 0, column = 7, padx = 5)


## RIGHT ALIGN

right_align_icon = tk.PhotoImage(file = "Icons/right-align.png")
right_align_btn = ttk.Button(tool_bar_label, image = right_align_icon)
right_align_btn.grid(row =0, column = 8, padx = 5)









## THEMES FUNCTION

def change_theme():
    choose_theme = theme_choose.get()
    colour_tuple = colour_dict.get(choose_theme)
    fg_color,bg_color = colour_tuple[0], colour_tuple[1]
    text_editor.config(background = bg_color,fg = fg_color)




count = 0
for i in colour_dict:
    colour_theme.add_radiobutton(label = i, image = colour_icon[count], compound = tk.LEFT,variable =theme_choose, command = change_theme)
    count += 1



## TEXT EDITOR 
text_editor = tk.Text(main_application)
text_editor.config(wrap = "word", relief = tk.FLAT)


## CREATING SCROOL BAR AND MAKE THEM WORK EK SATH 
scroll_bar = tk.Scrollbar(main_application) #creating Scrol bar in text editor
text_editor.focus_set() 
scroll_bar.pack(side = tk.RIGHT, fill = tk.Y) #scrool bar ko right side me krdiya
text_editor.pack(fill = tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set )


#  FONT AND SIZE CHANGING FUNCTION 

Font_current = "Arial"
Font_size_current = 16
    #FONT CHANGING
def changing_font(main_application):
    global Font_current
    Font_current = font_family.get()
    text_editor.configure(font = (Font_current,Font_size_current))

    #SIZE CHANGING

def change_size(main_application):
    global Font_size_current
    Font_size_current = size_variable.get()
    text_editor.configure(font = (Font_current, Font_size_current))

font_box.bind("<<ComboboxSelected>>", changing_font)
font_size.bind("<<ComboboxSelected>>", change_size)


## BOLD FUNCTION

##print(tk.font.Font(font= text_editor["font"]).actual())
#this tell us what this we need to change weight(key) normal(value) [in dictory]

def bold_fun():
    text_get = tk.font.Font(font= text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font = (Font_current, Font_size_current, "bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font = (Font_current, Font_size_current, "normal"))

bold_btn.configure(command = bold_fun) # Now Attach this func with bold button


## ITALIC FUCTION AND BUTTON

def italic_fun():
    text_get = tk.font.Font(font= text_editor["font"])
    if text_get.actual()["slant"] == 'roman':
        text_editor.configure(font = (Font_current, Font_size_current, "italic"))
    if text_get.actual()["slant"] == 'italic':
        text_editor.configure(font = (Font_current, Font_size_current, "roman"))

italic_btn.configure(command = italic_fun)


## UNDERLINE FUNCTION

def under_line_fun():
    text_get = tk.font.Font(font= text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font = (Font_current, Font_size_current, "underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font = (Font_current, Font_size_current, "normal"))

underline_btn.configure(command = under_line_fun)


## COLOUR CHANING FUNCTION AND BUTTON

def colour_choose():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_colour_btn.configure(command = colour_choose)

## LEFT ALIGNMENT FUNCTION

def alignment_left():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("left", justify = tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "left")

left_aligh_btn.configure(command = alignment_left)

## CENTER ALIGNMENT FUNCTION

def alignment_center():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("center", justify = tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "center")

Center_align_btn.configure(command = alignment_center)

## RIGHT ALIGNMENT FUNCTION

def alignment_right():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("right", justify = tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "right")

right_align_btn.configure(command = alignment_right)


# STATUS BAR AND CHARACTER COUNT MACHINE

status_bars = ttk.Label(main_application, text = "status bar")
status_bars.pack(side = tk.BOTTOM)

text_change = False

def change_word(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0,"end-1c").split())
        character = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text = f"character :{character} word: {word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", change_word)









# TOOL BAR AND STATUS BAR HIDE FUNCTIONS

show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bars.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side = tk.BOTTOM)
        show_status_bar=True
            



View.add_checkbutton(label = "Tool Bar",image = tool_bar, compound = tk.LEFT, accelerator = "Ctr+h", onvalue = True, offvalue = 0,variable= show_toolbar, command = hide_toolbar)
View.add_checkbutton(label = "Status Bar", image = status_bar , compound = tk.LEFT, accelerator = "Ctr+g", onvalue = True, offvalue = 0,variable = show_status_bar, command = hide_statusbar )


## CUT COPY PASTE FUNCTIONS
Edit.add_command(label = "Copy", image = copy_icon, compound = tk.LEFT, accelerator = "Ctr+C", command = lambda:text_editor.event_generate("<<Control c>>"))
Edit.add_command(label = "Cut", image = cut_icon, compound = tk.LEFT, accelerator = "Ctr+X", command = lambda:text_editor.event_generate("<<Control v>>") )
Edit.add_command(label = "Paste", image = paste_icon, compound= tk.LEFT, accelerator = "CTR+V", command = lambda:text_editor.event_generate("<<Control x>>"))



## NEW

text_url = " "
def new_file(event = None):
    global text_url
    text_url = " "
    text_editor.delete(1.0,tk.END)
file.add_command(label = "New", image = new_icon, compound = tk.LEFT, accelerator = "Ctr+N", command = new_file )#Accelerator for ShortCut Keys
## OPEN

def open_file(event = None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir = os.getcwd(), title = "select file", filetypes = (("Text file","*.txt"),("All files","*.*")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))
file.add_command(label = "Open", image = open_icon, compound = tk.LEFT, accelerator = "Ctr+O", command = open_file )


## SAVE FUNCTION

def save_file(event = None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0,tk.END))
            with open(text_url, "w", encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode = "w", defaultextension = "txt", filetypes  = (("Text file","*.txt"),("all files","*.*")))
            content2 = text_editor.get(1.0,tk.END)
            text_url.write(content2)
            text_url.Close()
    except:
        return

   
        
            





file.add_command(label = "Save", image = save_icon, compound = tk.LEFT, accelerator = "Ctr+S", command = save_file )

## SAVE AS FUNCTION
def save_as_file(event = None):
    global text_url
    try:
        content = text_editor.get(1.0,tk.END)
        text_url = filedialog.asksaveasfile(mode = "w",defaultextension = "txt", filetypes  = (("Text file","*.txt"),("all files","*.*"))) 
        text_url.write(content)
        text_url.Close()
    except:
        return

file.add_command(label = "Save As", image = saveas_icon, compound = tk.LEFT, accelerator = "Ctr+Alt+S" , command = save_as_file)

## EXIT FUNCTION
def exit_fun(event = None):
    global text_change, text_url
    try:
        if text_change:
            mbox = messagebox.askyesnocancel("warning", "Do you want to save this file")
            if mbox is True:
                if text_url:
                    content = text_editor.get(1.0,tk.END)
                    with open(text_url , "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2 = text_editor.get(1.0,tk.END)
                    text_url = filedialog.asksaveasfile(mode = "w",defaultextension = "txt", filetypes  = (("Text file","*.txt"),("all files","*.*"))) 
                    text_url.write(content2)
                    text_url.Close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return




file.add_command(label = "Exit", image = exit_icon, compound = tk.LEFT, accelerator = "Ctr+N", command = exit_fun )





#kisne file ko dhkna hai (ye humhe main_application me dhkana hai)
main_application.config(menu = main_menu)




main_application.mainloop()

