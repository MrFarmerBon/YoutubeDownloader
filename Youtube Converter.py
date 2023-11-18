from tkinter import *
from tkinter.filedialog import askdirectory
from pytube import YouTube
from PIL import Image, ImageTk

def Download(link):
  #MP4 Option
  if value_inside.get() == "MP4":
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=fd)
    except:
      #Error Message
        print("An error has occurred")
    print("Download is completed successfully")
  #MP3 Option
  elif value_inside.get() == "MP3":
     youtubeObject = YouTube(link)
     audio_stream = youtubeObject.streams.filter(only_audio=True).first()
     try:
         audio_stream.download(output_path=fd)
     except Exception as e:
         print("An error has occurred:", str(e))
     print("MP3 download is completed successfully")
def submit():
  #On submit button press
    print("Selected Option: "+(value_inside.get()))
    print("Selected Directory: "+fd)
    print("Selected URL: "+url.get())
    Download(link=url.get())
def file_location():
  #Select a file location 
    global fd
    fd = askdirectory()
    Directory_Entry_button.config(text=fd)

#Create Window
window = Tk()
window.geometry("350x200")
window.title("Youtube To ...")
#Title
Title = Label(text="Youtube Video Converter", font="helvica 12 underline")
Title.pack()

#Open Image
image = Image.open("Youtube_logo.png")
max_width = 50
max_height = 50
#Display Window On Window
image.thumbnail((max_width, max_height))
image = ImageTk.PhotoImage(image)
image_label = Label(window, image=image)
image_label.pack()

#Foramt Options
Format_list = ["MP4", "MP3"]
value_inside = StringVar(window)
value_inside.set("Select an Option")
question_menu = OptionMenu(window, value_inside, *Format_list)
question_menu.pack()

#Youtube URL Entry and Variable
url = StringVar()
url.set("youtube.com/watch?v=")
URL_Entry = Entry(window, textvariable=url, width= 34)
URL_Entry.pack()

#Select a File Loctation
Directory_Entry_button = Button(window, text='File Directory', command=file_location)
Directory_Entry_button.pack()

#Submit Button
submit_button = Button(window, text='Submit', command=submit)
submit_button.pack()

window.mainloop()


#Here Comes The Sun - https://www.youtube.com/watch?v=GKdl-GCsNJ0