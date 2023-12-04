
import tkinter as tk
import Main

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("S@fe Text")
        self.geometry("270x610")
        self.resizable(False,False)

        self.frames = {
            "Frame1": Frame1,
            "Frame2": Frame2
        }

        self.current_frame = None
        self.show_frame("Frame1")

    def show_frame(self, container):
        new_frame = self.frames[container]
        if self.current_frame is not None:
            self.current_frame.grid_forget()

        self.current_frame = new_frame(self)
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame.tkraise()

class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # label
        label = tk.Label(self, text="Encryptor", font=("Helvetica", 18))
        label.pack(padx=10, pady=10)

        # input message
        self.inputText = tk.Text(self, height=10, width=30)
        self.inputText.pack(padx=10, pady=10)

        # input key
        self.inputKey = tk.Text(self, height=5, width=30)
        self.inputKey.pack(padx=10, pady=10)

        # convert button
        self.btn = tk.Button(self, text="Eecrypt your message",command=lambda: self.Encryptor())
        self.btn.pack(padx=10, pady=10)
        
        # output text
        self.outputText = tk.Text(self, height=10, width=30)
        self.outputText.pack(padx=10, pady=5)
        

        # switch beetwen frames
        self.btn = tk.Button(self, text="Decryptor",
                        command=lambda: parent.show_frame("Frame2"))
        self.btn.pack(padx=10, pady=10)
    
    def Encryptor(self):
        enteredMessage = self.inputText.get("1.0", tk.END)
        enteredKey = self.inputKey.get("1.0", tk.END)
        
        while enteredMessage.endswith("\n"):   
            enteredMessage =enteredMessage[:-1]
        
        while enteredKey.endswith("\n"):
            enteredKey =enteredKey[0:-1]

        temp = Main.Encryptor(enteredMessage,enteredKey)
        
        self.outputText.delete("1.0",tk.END)
        self.outputText.insert(tk.END, str(temp))


class Frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # label
        label = tk.Label(self, text="Decryptor", font=("Helvetica", 18))
        label.pack(padx=10, pady=10)

        # input message
        self.inputText = tk.Text(self, height=10, width=30)
        self.inputText.pack(padx=10, pady=10)

        # input key
        self.inputKey = tk.Text(self, height=5, width=30)
        self.inputKey.pack(padx=10, pady=10)

        # convert button
        self.btn = tk.Button(self, text="Decrypt your message",command=lambda: self.Decryptor())
        self.btn.pack(padx=10, pady=10)
        
        # output text
        self.outputText = tk.Text(self, height=10, width=30)
        self.outputText.pack(padx=10, pady=5)
        

        # switch beetwen frames
        self.btn = tk.Button(self, text="Encryptor",
                        command=lambda: parent.show_frame("Frame1"))
        self.btn.pack(padx=10, pady=10)
    
    def Decryptor(self):
        enteredMessage = self.inputText.get("1.0", tk.END)
        enteredKey = self.inputKey.get("1.0", tk.END)
        
        while enteredMessage.endswith("\n"):   
            enteredMessage =enteredMessage[:-1]
        
        while enteredKey.endswith("\n"):
            enteredKey =enteredKey[0:-1]

        temp = Main.Decryptor(enteredMessage,enteredKey)
        
        self.outputText.delete("1.0",tk.END)
        self.outputText.insert(tk.END, str(temp))

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
