import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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

# Ajout d'un bouton pour vérifier si la case est cochée
def check_allcheckbox():
    no_folder = True
    if checkbox_destop.check_checkbox():
        Desktop_dir.clear_pix_files()
        no_folder = False

    if checkbox_music.check_checkbox():
        Music_dir.clear_pix_files()
        no_folder = False

    if checkbox_downloads.check_checkbox():
        Downloads_dir.clear_pix_files()
        no_folder = False

    if checkbox_videos.check_checkbox():
        Videos_dir.clear_pix_files()
        no_folder = False

    if checkbox_docs.check_checkbox():
        Documents_dir.clear_pix_files()
        no_folder = False

    if checkbox_images.check_checkbox():
        Pictures_dir.clear_pix_files()
        no_folder = False
    
    if no_folder == True :
        messagebox.showinfo("ERREUR","Il semblerait que vous aillez oublié de sélectionner un ou plusieurs dossiers à analyser...\n\nCochez les sous-catégories où des fichiers PIX sont enregistrés !")


style = ttk.Style()
style.configure("TButton", font=("Helvetica", 48), background="#ffac04", foreground="#ffac04", borderwidth=0, width=45)
check_button = ttk.Button(root, text="Supprimer les fichiers générés lors de vos sessions PIX", command=check_allcheckbox, style="TButton")
check_button.place(x=160,y=800)

# Lancement de la boucle principale
root.mainloop()

Desktop_dir.clear_pix_files()