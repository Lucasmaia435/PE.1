# Importando módulos
import cv2 as cv
import argparse as arg
import numpy as np

# Adicionando argumento de comando para receber imagem  
img = arg.ArgumentParser()
img.add_argument('image')
imgs = vars(img.parse_args())

# Definindo Main do programa
if __name__ == '__main__':
    # Configurando a imagem
    img = cv.imread(imgs['image'],cv.IMREAD_COLOR)
    height, width, _ = img.shape
    # Contador de corpos
    cont = 0
    # Definição de estrela
    stars_condition = np.array([12,12,12])
    # Checagem de todos os pixels
    for i in range(0, height):
        for j in range(0, width):
            if np.all(img[i, j] >= stars_condition):
                cont = cont + 1
    print("Está secção possui: {} corpos celestes que emitem ou refletem luz".format(cont))
    print("Aplicar filtro?[y/n]")
    filter = input()
    if filter == 'y' :
        for i in range(0, height):
            for j in range(0, width):
                if np.all(img[i, j] >= stars_condition):
                    if (np.all(img[i, j+1]>= stars_condition) and np.all(img[i-1, j]>= stars_condition) and np.all(img[i+1, j]>= stars_condition)  and np.all(img[i, j-1]>= stars_condition)):
                        cont = cont - 4
        print("Está secção possui: {} corpos celestes que emitem ou refletem luz (Filtro aplicado)".format(cont))
