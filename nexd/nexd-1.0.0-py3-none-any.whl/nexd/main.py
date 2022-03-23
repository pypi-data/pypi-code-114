import os
import contextlib

with contextlib.redirect_stdout(open(os.devnull, 'w')):
    #importations utiles sans les messages des librairies
    import cv2
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt


class Nexd:
    
    def __init__(self, *args, **kwargs):
        self.__author = "importFourmi"
        self.__args = args
        self.__kwargs = kwargs
        self.methods = [f for f in dir(self) if not f.startswith('_')]
        
        if self.__kwargs.get("verbose") == 0:
            self.verbose = False
        else:
            self.verbose = True

    def load_img(self, img_path):
        """
        Fonction qui télécharge l'image en RGB.
        
        :param img_path: path de l'image
        
        :return: l'image
        """
        
        try:
            if not(os.path.isfile(img_path)):
                print("Image not found")
                return np.array([])

            else :
                # l'image est créée avec OpenCV
                img = cv2.imread(img_path)  
                
                # on met de la bonne couleur
                return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
        
        except Exception as e:
            print(e)
            return None


    def imshow(self, img, title=""):
        """
        Fonction qui affiche l'image.
        
        :param img: image (ou path vers l'image)
        :param (title): titre de l'image
        
        :return: ne retourne rien
        """
        
        try:
            # si l'image est un path à télécharger
            if isinstance(img, str): 
                img = self.load_img(img)

            if np.any(img):
                
                img = img.copy()
                
                # on affiche les dimensions de l'image
                print(np.array(img).shape)

                # si il y a un titre on l'affiche
                if title:
                    plt.title(title)
                    
                # on n'affiche pas les axes
                plt.axis('off')  

                plt.imshow(img)
                plt.show()
                
        except Exception as e:
            print(e)
            return None
        
    
    def ext_list(self, path=None, list_ext=[".png", ".jpg", ".jpeg"]):
        """
        Fonction qui liste les extensions fournies en paramètre d'un dossier.
        
        :param path: path du dossier à extraire (None si dossier courant)
        :param (list_ext): liste des extensions possibles (par défaut: liste des images)
        
        :return: la liste des chemins
        """
        
        try:
            return np.array([file for file in os.listdir(path) for ext in list_img if file.endswith(ext)])
                
        except Exception as e:
            print(e)
            return None       


    def draw_rect(self, img, coords, color=(255, 0, 0), thickness=1):
        """
        Fonction qui dessine des rectangles sur une image.
        
        :param img: image sur laquelle on veut dessiner des rectangles
        :param coords: liste des coordonnées des rectangles (x_start, y_start, x_end, y_end)
        :param (color): couleur des rectangles à dessiner
        :param (thickness): épaisseur des rectangles (-1 pour un rectangle plein)
        
        :return: l'image avec les rectangles
        """
        
        try:
            # si l'image est un path à télécharger
            if isinstance(img, str):
                img = self.load_img(img)
            
            if np.any(img):
                
                img = img.copy()
                
                # si il y a qu'un seul rectangle
                if len(np.array(coords).shape) == 1:
                    # on dessine le rectangle
                    coords = np.array([coords])
                
                # si c'est une liste de rectangles
                else:
                    for coord in coords:
                        # on dessine tous les rectangles
                        img = cv2.rectangle(img, (coord[0], coord[1]), (coord[2], coord[3]), color, thickness)
                return img
            
            else:
                return np.array([])
            
        except Exception as e:
            print(e)
            return None


    def draw_pixels(self, img, x, y, value=None, color=[0, 255, 0], radius=None):
        """
        Fonction qui dessine les pixels sur l'image.
        
        :param x: liste des x à dessiner
        :param y: liste des y à dessiner
        :param (value): liste des valeurs pour chaque pixel
        :param (color): couleur des pixels si il n'y a pas de valeurs pour chaque pixel
        :param (radius): radius des pixels
            
        :return: l'image avec les pixels
        """
        
        try:
            # si l'image est un path à télécharger
            if isinstance(img, str):
                img = self.load_img(img)

            if np.any(img):

                img = img.copy()
                
                if radius is None:
                    radius = int(0.01*max(img.shape[0], img.shape[1]))                    

                if not(value is None):
                    # normalise linéairement les données entre 0.0 et 1.0
                    norm = matplotlib.colors.Normalize(vmin=min(value), vmax=max(value))

                    # transforme les valeurs en couleurs
                    rgba = plt.get_cmap('inferno')(norm(value.astype(np.float64)))

                    # on dessine un cercle de 1% de la taille de l'image (de la couleur de la valeur)
                    for i in range(len(x)):
                        img = cv2.circle(img, (int(x[i]), int(y[i])), radius, rgba[i][:-1]*255, -1)

                else:
                    # on dessine un cercle (en vert) de 1% de la taille de l'image
                    for i in range(len(x)):
                        img = cv2.circle(img, (int(x[i]), int(y[i])), radius, color, -1)

                return img
        
        except Exception as e:
            print(e)
            return None


    def imsave(self, filename, img):
        """
        Fonction qui permet d'enregistrer une image.

        :param filename: string représentant le nom de l'image
        :param img: image à enregistrer
            
        :return: ne retourne rien
        """

        try:
            # ordre normal des paramètres
            if isinstance(filename, str) and not isinstance(img, str):
                plt.imsave(filename, img)
            
            # si on se trompe sur l'ordre des paramètres
            elif isinstance(img, str) and not isinstance(filename, str):
                plt.imsave(img, filename)
        
        except Exception as e:
            print(e)
            return None


    def extension_rect(self, coords, coef):
        """
        Fonction qui multiplie les coordonnées par un coefficient (O: pas d'extension, 0.5: size*2, 1:size*3, etc.).
        
        :param coords: liste de coordonnées de rectangles
        :param coef: coefficient multiplicateur
        
        :return: les nouvelles coordonnées
        """
        
        try:
            # où mettre les nouvelles coordonnées
            result = []
            
            # si il y a qu'un seul rectangle
            if len(np.array(coords).shape) == 1:
                # on dessine le rectangle
                coords = np.array([coords])
                
            for coord in coords:

                width = coord[2] - coord[0]
                height = coord[3] - coord[1]

                result.append([ coord[0] - int((width*coef)/2), 
                                coord[1] - int((height*coef)/2), 
                                coord[2] + int((width*coef)/2), 
                                coord[3] + int((height*coef)/2)
                              ] )

            return np.array(result)
        
        except Exception as e:
            print(e)
            return None


nexd = Nexd(verbose=0)

if nexd.verbose:
    print("Bienvenue dans Nexd, les fonctions disponibles sont les suivantes et vous pouvez utiliser help(fonction) pour plus d'informations :")
    for fonction in nexd.methods:
        print("  -", fonction)