import tkinter
import threading
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showerror
from tkinter import messagebox
import calibCam
import mainCalib54

# Variaveis globais
pathGRID = []
pathWorld = None
pathPoints = []

labelTitlePathGRID = None
labelPathCam1GRID = None
labelPathCam2GRID = None
labelPathCam3GRID = None
labelPathCam4GRID = None

labelTitleWorldPath = None
labelPathWorld = None

labelTitlePathPoints = None
labelPathCam1Points = None
labelPathCam2Points = None
labelPathCam3Points = None
labelPathCam4Points = None

def handleCalibCam(window):
    fname = askopenfilename(filetypes=(("PNG", "*.png"),
                                       ("JPEG", "*.jpg"),
                                       ("Todos os arquivos", "*.*")))
    if fname:
        # try:
            window.destroy()
            calibCam.calibcam(fname)
        # except:                     # <- naked except is a bad idea
        #     showerror("Open Source File",
        #                 "Failed to read file\n'%s'" % fname)
        # return

def handleOpenGRID(window):
    
    global pathGRID
    global labelTitlePathGRID
    global labelPathCam1GRID
    global labelPathCam2GRID
    global labelPathCam3GRID
    global labelPathCam4GRID

    if hasattr(labelTitlePathGRID, 'place_forget'):
        labelTitlePathGRID.place_forget()
    if hasattr(labelPathCam1GRID, 'place_forget'):
        labelPathCam1GRID.place_forget()
    if hasattr(labelPathCam2GRID, 'place_forget'):
        labelPathCam2GRID.place_forget()
    if hasattr(labelPathCam3GRID, 'place_forget'):
        labelPathCam3GRID.place_forget()
    if hasattr(labelPathCam4GRID, 'place_forget'):
        labelPathCam4GRID.place_forget()
    
    pathGRID = []

    fname = askopenfilenames(filetypes=(("CSV", "*.csv"),
                                        ("M", "*.m"),
                                        ("MAT", "*.mat"),
                                       ("Todos os arquivos", "*.*")))
 
    if fname:
        # print(fname)
        # print(len(fname))

        if (len(fname) != 4):
            messagebox.showerror(
                "Erro, quantidade diferente de quatro", 
                "É preciso selecionar quatro arquivos contendo as coordenadas do GRID")
        else:
        
            for item in fname:
                pathGRID.append(item)

            labelTitlePathGRID = tkinter.Label(window, text="Coordenadas do GRID carregado", background="#FFF")
            labelTitlePathGRID.place(x=410, y=5)
            labelPathCam1GRID = tkinter.Label(window, text="Câmera 1: " + pathGRID[0] if len(pathGRID) > 0 else "", background="#FFF")
            labelPathCam1GRID.place(x=410, y=25)
            labelPathCam2GRID = tkinter.Label(window, text="Câmera 2: " + pathGRID[1] if len(pathGRID) > 1 else "", background="#FFF")
            labelPathCam2GRID.place(x=410, y=45)
            labelPathCam3GRID = tkinter.Label(window, text="Câmera 3: " + pathGRID[2] if len(pathGRID) > 2 else "", background="#FFF")
            labelPathCam3GRID.place(x=410, y=65)
            labelPathCam4GRID = tkinter.Label(window, text="Câmera 4: " + pathGRID[3] if len(pathGRID) > 3 else "", background="#FFF")
            labelPathCam4GRID.place(x=410, y=85)

def handleOpenWorld(window):

    global labelTitleWorldPath
    global labelPathWorld
    global pathWorld

    pathWorld = None

    if hasattr(labelTitleWorldPath, 'place_forget'):
        labelTitleWorldPath.place_forget()
    if hasattr(labelPathWorld, 'place_forget'):
        labelPathWorld.place_forget()

    fname = askopenfilename(filetypes=(("CSV", "*.csv"),
                                        ("M", "*.m"),
                                        ("MAT", "*.mat"),
                                       ("Todos os arquivos", "*.*")))
 
    if fname:
            pathWorld = fname
            labelTitleWorldPath = tkinter.Label(window, text="Coordenadas do mundo carregado", background="#FFF")
            labelTitleWorldPath.place(x=410, y=115)
            labelPathWorld = tkinter.Label(window, text="Mundo 1: " + pathWorld, background="#FFF")
            labelPathWorld.place(x=410, y=135)

def handleCalib():
    global pathGRID
    global pathWorld

    if (len(pathGRID) < 4):
        messagebox.showerror(
                "Erro, coordenadas do GRID não carregado", 
                "É preciso carregar os arquivos contendo as coordenadas do GRID")
    elif (pathWorld is None):
        messagebox.showerror(
                "Erro, coordenadas do mundo não carregado", 
                "É preciso carregar o arquivo contendo as coordenadas do mundo")
    else:
        try:
            mainCalib54.calibCams(pathGRID, pathWorld)

            messagebox.showinfo(
                    "Calibração realizada com sucesso!", 
                    "A calibração entre as coordenadas do mundo e do GRID foi realizada com sucesso!")
        except:
            messagebox.showerror(
                    "Erro ao tentar fazer calibração!", 
                    "A calibração entre as coordenadas do mundo e do GRID não foi realizada com sucesso!")

def handleOpenPoints(window):
    
    global pathPoints
    global labelTitlePathPoints
    global labelPathCam1Points
    global labelPathCam2Points
    global labelPathCam3Points
    global labelPathCam4Points

    if hasattr(labelTitlePathPoints, 'place_forget'):
        labelTitlePathPoints.place_forget()
    if hasattr(labelPathCam1Points, 'place_forget'):
        labelPathCam1Points.place_forget()
    if hasattr(labelPathCam2Points, 'place_forget'):
        labelPathCam2Points.place_forget()
    if hasattr(labelPathCam3Points, 'place_forget'):
        labelPathCam3Points.place_forget()
    if hasattr(labelPathCam4Points, 'place_forget'):
        labelPathCam4Points.place_forget()
    
    pathPoints = []

    fname = askopenfilenames(filetypes=(("CSV", "*.csv"),
                                        ("M", "*.m"),
                                        ("MAT", "*.mat"),
                                       ("Todos os arquivos", "*.*")))
 
    if fname:
        # print(fname)
        # print(len(fname))

        if (len(fname) != 4):
            messagebox.showerror(
                "Erro, quantidade diferente de quatro", 
                "É preciso selecionar quatro arquivos contendo as coordenadas dos marcadores")
        else:
        
            for item in fname:
                pathPoints.append(item)

            labelTitlePathPoints = tkinter.Label(window, text="Coordenadas dos marcadores carregado", background="#FFF")
            labelTitlePathPoints.place(x=410, y=165)
            labelPathCam1Points = tkinter.Label(window, text="Câmera 1: " + pathPoints[0] if len(pathPoints) > 0 else "", background="#FFF")
            labelPathCam1Points.place(x=410, y=185)
            labelPathCam2Points = tkinter.Label(window, text="Câmera 2: " + pathPoints[1] if len(pathPoints) > 1 else "", background="#FFF")
            labelPathCam2Points.place(x=410, y=205)
            labelPathCam3Points = tkinter.Label(window, text="Câmera 3: " + pathPoints[2] if len(pathPoints) > 2 else "", background="#FFF")
            labelPathCam3Points.place(x=410, y=225)
            labelPathCam4Points = tkinter.Label(window, text="Câmera 4: " + pathPoints[3] if len(pathPoints) > 3 else "", background="#FFF")
            labelPathCam4Points.place(x=410, y=245)

def handleReconstruction():
    global pathGRID
    global pathWorld
    global pathPoints

    if (len(pathGRID) < 4):
        messagebox.showerror(
                "Erro, coordenadas do GRID não carregado", 
                "É preciso carregar os arquivos contendo as coordenadas do GRID")
    elif (pathWorld is None):
        messagebox.showerror(
                "Erro, coordenadas do mundo não carregado", 
                "É preciso carregar o arquivo contendo as coordenadas do mundo")
    elif (len(pathPoints) < 4):
        messagebox.showerror(
                "Erro, coordenadas dos marcadores não carregados", 
                "É preciso carregar os arquivos contendo as coordenadas dos marcadores")
    else:
        try:
            mainCalib54.calibPoints(pathPoints)
        except Exception as ex:

            if (str(ex) == "NotCalib"):
                messagebox.showerror(
                "Erro, é preciso calcular a calibração entre coordenadas do GRID com as do mundo", 
                "Você ainda não calculou a calibração entre as coordenadas do GRID com as do mundo")
            elif (str(ex) == "Octave evaluation error:\nerror: strtrim: S argument must be a string or cellstring"):
              print('Erro ao fechar a janela')  
            else:
                messagebox.showerror(
                "Erro, ocorreu um erro ao tentar calcular a reconstrução", 
                "Erro, ocorreu um erro ao tentar calcular a reconstrução")

def main():

    global pathGRID

    window = tkinter.Tk()
    window.title('Sistema de reconstrução da marcha humana')
    window.configure(background='white')
    window.geometry("640x480")

    # Abre a janela em tela cheia
    window.attributes('-zoomed', True)
    
    # Abre a janela em fullscreen
    # window.attributes("-fullscreen", True)

    btnCalibCam = tkinter.Button(window, text="Calibrar coordenadas da câmera",
                                 width=45, height=2, command=lambda: handleCalibCam(window))
    btnCalibCam.place(x=5, y=5)
    
    btnOpenGRID = tkinter.Button(window, text="Carregar coordenadas do GRID (4 câmeras)",
                                 width=45, height=2, command=lambda: handleOpenGRID(window))
    btnOpenGRID.place(x=5, y=65)
    
    btnOpenWorld = tkinter.Button(window, text="Carregar coordenadas do mundo",
                                 width=45, height=2, command=lambda: handleOpenWorld(window))
    btnOpenWorld.place(x=5, y=125)

    btnCalib = tkinter.Button(window, text="Calcular a calibração entre coordenadas do GRID e mundo", width=45, height=2, command=lambda: handleCalib())
    btnCalib.place(x=5, y=185)

    btnOpenPoints = tkinter.Button(window, text="Carregar coordenadas dos marcadores (4 câmeras)",
                                 width=45, height=2, command=lambda: handleOpenPoints(window))
    btnOpenPoints.place(x=5, y=245)

    btnOpenShow = tkinter.Button(window, text="Calcular a reconstrução e exibir",
                                 width=45, height=2, command=lambda: handleReconstruction())
    btnOpenShow.place(x=5, y=305)

    window.mainloop()

if __name__ == "__main__":
    main()
