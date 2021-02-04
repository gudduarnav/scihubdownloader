try:
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.messagebox as tkMessageBox
except ImportError:
    print("Install tkinter")

import scihub

class App:
    def __init__(self, root):
        #setting title
        root.title("SciHub Downloader")
        #setting window size
        width=603
        height=268
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_152=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_152["font"] = ft
        GLabel_152["fg"] = "#333333"
        GLabel_152["justify"] = "center"
        GLabel_152["text"] = "SciHub URL:"
        GLabel_152.place(x=10,y=20,width=110,height=30)

        self.GLineEdit_156=tk.Entry(root, textvariable=tk.StringVar(root, "https://sci-hub.se/"))
        self.GLineEdit_156["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_156["font"] = ft
        self.GLineEdit_156["fg"] = "#333333"
        self.GLineEdit_156["justify"] = "left"
        #GLineEdit_156["text"] = "https://sci-hub.se/"
        self.GLineEdit_156.place(x=130,y=20,width=449,height=30)

        GLabel_693=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_693["font"] = ft
        GLabel_693["fg"] = "#333333"
        GLabel_693["justify"] = "center"
        GLabel_693["text"] = "DOI:"
        GLabel_693.place(x=0,y=80,width=70,height=25)

        self.GLineEdit_570=tk.Entry(root, textvariable=tk.StringVar(root, "https://doi.org/10.1109/PS.2006.4350204"))
        self.GLineEdit_570["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_570["font"] = ft
        self.GLineEdit_570["fg"] = "#333333"
        self.GLineEdit_570["justify"] = "left"
        #GLineEdit_570["text"] = "https://doi.org/10.1109/PS.2006.4350204"
        self.GLineEdit_570.place(x=130,y=80,width=449,height=30)

        GLabel_635=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_635["font"] = ft
        GLabel_635["fg"] = "#333333"
        GLabel_635["justify"] = "center"
        GLabel_635["text"] = "Folder:"
        GLabel_635.place(x=10,y=140,width=70,height=25)

        self.GLineEdit_167=tk.Entry(root, textvariable=tk.StringVar(root, "./"))
        self.GLineEdit_167["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_167["font"] = ft
        self.GLineEdit_167["fg"] = "#333333"
        self.GLineEdit_167["justify"] = "left"
        #GLineEdit_167["text"] = "./"
        self.GLineEdit_167.place(x=130,y=140,width=448,height=30)

        GButton_321=tk.Button(root)
        GButton_321["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=16)
        GButton_321["font"] = ft
        GButton_321["fg"] = "#000000"
        GButton_321["justify"] = "center"
        GButton_321["text"] = "Download"
        GButton_321.place(x=260,y=190,width=318,height=45)
        GButton_321["command"] = self.GButton_321_command

        GLabel_691=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_691["font"] = ft
        GLabel_691["fg"] = "#333333"
        GLabel_691["justify"] = "center"
        GLabel_691["text"] = "Wait Time:"
        GLabel_691.place(x=0,y=200,width=122,height=30)

        self.GLineEdit_358=tk.Entry(root,textvariable=tk.StringVar(root,"5"))
        self.GLineEdit_358["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_358["font"] = ft
        self.GLineEdit_358["fg"] = "#333333"
        self.GLineEdit_358["justify"] = "left"
        #GLineEdit_358["text"] = "5"
        self.GLineEdit_358.place(x=130,y=200,width=110,height=30)

    def GButton_321_command(self):
        try:
            print("START DOWNLOAD")
            url = self.GLineEdit_156.get().strip()
            doi = self.GLineEdit_570.get().strip()
            folder = self.GLineEdit_167.get().strip()
            waittime = int(self.GLineEdit_358.get().strip())

            s = scihub.SciHub(url = url, waitTime=waittime, folder=folder)
            result = s.download(doi)
            if not result:
                raise Exception("Failed to download DOI")
            print("DONE")
            tkMessageBox.showinfo("DOI Downloaded from SCIHUB",
                                   "DOI {} downloaded to {} from URL {}".format(doi, folder, url))

        except Exception as ex:
            print("Exception:", str(ex))
            tkMessageBox.showerror("Exception during Download", str(ex))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
