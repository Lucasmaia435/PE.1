# Importando módulos
import cv2 as cv
import argparse as arg
import numpy as np

# Adicionando argumento de comando para receber imagem  
img = arg.ArgumentParser()
img.add_argument('image')
imgs = vars(img.parse_args())


if __name__ == '__main__':
    # Configurando a imagem
    img = cv.imread(imgs['image'],cv.IMREAD_COLOR)
    main_win = 'Stars'
    cv.namedWindow(main_win, cv.WINDOW_KEEPRATIO)
    #cv.resizeWindow('Stars',800,600)
    height, width, _ = img.shape
    # Contador de corpos
    cont = 0
    # Definição de estrela
    stars_condition = [12,12,12]
    # Checagem de todos os pixels
    for i in range(0, height):
        for j in range(0, width):
            if np.all(img[i, j] >= stars_condition):
                cont = cont + 1
                #if (np.all(img[i, j+1]>= stars_condition) and np.all(img[i-1, j]>= stars_condition) and np.all(img[i+1, j]>= stars_condition)  and np.all(img[i, j-1]>= stars_condition)):
                    #cont = cont - 4
                    #img[i, j] = (255-img[i, j])
                if (np.all(img[i, j+1]>= stars_condition) and np.all(img[i-1, j]>= stars_condition) and np.all(img[i+1, j]>= stars_condition)  and np.all(img[i, j-1]>= stars_condition) and np.all(img[i+1, j+1]>= stars_condition) and np.all(img[i-1, j+1]>= stars_condition) and np.all(img[i-1, j-1]>= stars_condition) and np.all(img[i+1, j-1]>= stars_condition)):
                    cont = cont - 8
    # Abrindo a imagem
    cv.imshow(main_win, img)
    print("Está secção possui: {} corpos celestes que emitem ou refletem luz".format(cont))
    cv.waitKey(0)
    cv.destroyAllWindows()