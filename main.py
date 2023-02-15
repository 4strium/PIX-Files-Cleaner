import tkinter as tk
from dir_object import directory
from checkbox_obj import Checkbox

# Generate Desktop directory :
Desktop_dir = directory('Desktop')

# Generate Downloads directory :
Downloads_dir = directory('Downloads')

# Generate Documents directory :
Documents_dir = directory('Documents')

# Generate Music directory :
Music_dir = directory('Music')

# Generate Videos directory :
Videos_dir = directory('Videos')

# Generate Pictures directory :
Pictures_dir = directory('Pictures')

import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
root.title("PIX Files Cleaner")
root.geometry("1920x1080")
root.resizable(False, False)  # Bloquer le ratio de la fenêtre
root.iconbitmap('icon\icon_window.ico')

# Ajout d'une image de fond
bg_image = tk.PhotoImage(file='img/Background.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

checkbox_destop = Checkbox(root,100,270,"#1e98ff")
checkbox_music = Checkbox(root,1210,270,"#1e98ff")
checkbox_downloads = Checkbox(root,100,412,"#2393ff")
checkbox_videos = Checkbox(root,1210,412,"#2491ff")
checkbox_docs = Checkbox(root,100,572,"#288bff")
checkbox_images = Checkbox(root,1210,572,"#298aff")

# Lancement de la boucle principale
root.mainloop()

Desktop_dir.clear_pix_files()