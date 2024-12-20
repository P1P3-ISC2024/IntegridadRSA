from tkinter import *
from tkinter import filedialog
from Keys import *
from rsa_file import *
from tkinter import messagebox
import HacerHash as HH
import LeerHash as LH

class GUI():  

  HEIGHT = 600
  WIDTH = 500
  background_color = "#23262E"
  white = "#fff"
  select_color = "#7A5FEE"
  show_inputs = False
  last_option = 0
  window = None
  frame = None
  
  path_encrypt = ""
  path_key = ""
  path_file_to_Decrypt = ""  
  
  generate_keys = False
  choose_file = False
  choose_fileD = False
  choose_key = False

  dynamic_widgets = []
  
  def __init__(self):
    self.window = Tk()
    self.window.title("Practice 2.RSA")
    self.window.geometry(str(self.HEIGHT)+'x'+str(self.WIDTH))
    self.window.resizable(0,0)

    self.frame = Frame(self.window,
                  background=self.background_color
                  )
    self.frame.pack(fill="both",
               expand=True
               )

    self.label_opt = Label(self.frame, 
                           text="Choose your option:",
                           fg=self.white,
                           bg=self.background_color,
                           font=("Arial",14)
                           )
    self.label_opt.pack()

    option = IntVar()

    self.radioButton1 = Radiobutton(self.frame,
                               text="Sign document",
                               variable=option,
                               value=1,
                               bg=self.background_color,
                               selectcolor=self.select_color,
                               fg=self.white,
                               font=("Arial",12)
                               )
    self.radioButton1.pack()

    self.radioButton2 = Radiobutton(self.frame,
                                    text="Check signature",
                                    variable=option,
                                    value=2,
                                    bg=self.background_color,
                                    selectcolor=self.select_color,
                                    fg=self.white,
                                    font=("Arial",12)
                                    )
    self.radioButton2.pack()

    self.selectButton = Button(self.frame,
                               text="select",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial",12),
                               command=lambda:self.selectButton_function(option.get())
                               )
    self.selectButton.pack()
        
    
  def run(self):
    self.window.mainloop()

    

  def selectButton_function(self,option):    
    if(option==1 and self.last_option != option):
      #Sign document
      self.generateCDwigets()  
      
         
    elif(option == 2 and self.last_option != option):
      self.generateKeysWigets()
      #Check signature  
      
    
    self.last_option = option
    
  def setInputText(self,input_entry,text):
    input_entry.delete(0,END)
    input_entry.insert(0,text)

  def destroyDynamicWidgets(self):
    self.generate_keys = False
    self.choose_file = False
    self.choose_fileD = False
    self.choose_key = False
    for i in self.dynamic_widgets:
      i.destroy()

  def generateCDwigets(self):
    self.destroyDynamicWidgets()
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    chooseKeysBtn = Button(self.frame,
                               text="Key",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial",12),
                               height= 1, width=15,
                               command=lambda:self.pathKeyDecrypt()
                               )
    chooseKeysBtn.pack()
    self.dynamic_widgets.append(chooseKeysBtn)
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    File = Button(self.frame,
                              text="File",
                              bd=0,
                              fg=self.white,
                              bg=self.select_color,
                              font=("Arial",12),
                              height= 1, width=15,
                              command=lambda:self.pathFileEncrypt()
                              )
    File.pack()
    self.dynamic_widgets.append(File)
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    encryptButton = Button(self.frame,
                                  text="Sign",
                                  bd=0,
                                  fg=self.white,
                                  bg=self.select_color,
                                  font=("Arial",12),
                                  height= 1, width=15,
                                  command=lambda:self.encrypt()
                                  )
    encryptButton.pack()
    self.dynamic_widgets.append(encryptButton)
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    
  def pathKeyDecrypt(self):    
    self.path_key = filedialog.askopenfilename()          
    self.choose_key = True
    print("Archivo seleccionado")
  
  def pathFileDecrypt(self):
    self.path_file_to_Decrypt = filedialog.askopenfilename()          
    self.choose_fileD = True
    print("Archivo seleccionado")
  
  def generateKeysWigets(self):
    self.destroyDynamicWidgets()
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    chooseKeysBtn = Button(self.frame,
                               text="Key",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial",12),
                               height= 1, width=15,
                               command=lambda:self.pathKeyDecrypt()
                               )
    chooseKeysBtn.pack()
    self.dynamic_widgets.append( chooseKeysBtn );
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    EncryptedfileBtn = Button(self.frame,
                               text="File",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial",12),
                               height= 1, width=15,
                               command=lambda:self.pathFileDecrypt()
                               )
    EncryptedfileBtn.pack()
    self.dynamic_widgets.append(EncryptedfileBtn)
    label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    label_space.pack()
    self.dynamic_widgets.append(label_space)
    encryptButton = Button(self.frame,
                                  text="Verify",
                                  bd=0,
                                  fg=self.white,
                                  bg=self.select_color,
                                  font=("Arial",12),
                                  height= 1, width=15,
                                  command=lambda:self.decrypt()
                                  )
    encryptButton.pack()
    self.dynamic_widgets.append(encryptButton);

  def pathFileEncrypt(self):     
    self.path_encrypt = filedialog.askopenfilename()    
    self.choose_file = True
    print("Archivo seleccionado")
    
  def generateKeysFunction(self):
    keysPublic_Generator()
    self.generate_keys = True
    print("Keys generated")
    
  def pathFile(self,var_storage_path,check_type_path):
    path = filedialog.askopenfilename()    
    var_storage_path = path    
    check_type_path = True    
    print("Archivo seleccionado")
  
  def encrypt(self):    
    if(self.choose_file and self.choose_key):
      encrypt_message(path_file=self.path_encrypt,path_key = self.path_key)
      print("Hash ready")
      messagebox.showinfo(title="Tarea terminada",message="The document is signed and save as message_C.txt")

  
  def decrypt(self):
    if(self.choose_fileD and self.choose_key):
      data = LH.readFile(direccion=self.path_file_to_Decrypt)
      LH.comprobar(data,self.path_key)
      print("test ready")

if __name__ == "__main__":
  gui = GUI()
  gui.run()