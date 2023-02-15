import os

class directory :

    def __init__(self, path_input):
        self.path = os.path.join(os.path.join(os.path.expanduser('~')), path_input)
    
    def clear_pix_files(self):
        list_of_root =[]
        list_of_files =[]
        for root, dirs, files in os.walk(self.path):
            list_of_root.append(root)
            list_of_files.append(files)
        for path_root in list_of_root :
            for element in os.listdir(path_root):
                if os.path.isfile(os.path.join(path_root,element)) and (element.startswith('Pix_') or element.startswith('pix_')):
                    os.remove(os.path.join(path_root,element))