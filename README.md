<h2 align = "center">
ESCOLA DE CIÊNCIAS E TECNOLOGIA
<br>
<br>
PROBABILIDADE E ESTATÍSTICA 
</h2>
<br>
<br>
<h3>
Professor : João Vital da Cunha Júnior 
<br>
Alunos : Lucas Maia Rezende Costa e Ariel Louise Queiros de Morais
</h3></h3>
<br>
<h1 align='center'> 
Contador de objetos emissores e/ou refletores de luz no espaço
</h1>
Este trabalho foi feito no âmbito de realizar a contagem de objetos encontrados em imagens do espaço, a fim de futuramente ocorrer a diferenciação dos objetos através da sua coloração. Com a praticidade da contagem e identificação 
seria possível, por exemplo, a identificação de lixo espacial, de cometas, meteoros, exoplanetas e diferentes tipos de estrelas de qualquer computador com acesso a uma imagem do céu noturno.
<br>

## Tópicos
1. Algoritmo
1. Módulos
1. Percorrer os pixels
1. Verificação e comparação de cores
1. Filtro de correção de contagem  
1. Testes
1. Referências

## Algoritmo  
O algoritmo do contador consiste em:

<ol>
    <li>O algoritmo recebe a imagem do usuário</li>
    <li>Ocorre o redimensionamento da imagem </li>
    <li>Todos os pixels da imagem são percorridos</li>
    <li>Ocorre a checagem de todos os pixels</li>
    <li>Aplica-se o filtro de "condição"</li>
    <li>Aplica-se o filtro de "correção de contagem"</li>
    <li>O algoritmo abre a nova imagem</li>
    <li>Exibe o resultado da contagem de objetos</li>
</ol>

## Módulos
O desenvolvimento do algoritmo foi feito em Python com o auxílio do seguintes módulos:

* OpenCV[1]
* Argparse[2]
* Numpy[3]

O módulo _OpenCV_ foi usado para receber, redimensionar, percorrer e checar todos os pixels da imagem.

```Python
    img = cv.imread('image.png',cv.IMREAD_COLOR)
``` 
> exemplo de leitura de imagem com OpenCV.

Sabendo que a imagem é uma matriz NxM, N sua largura e M sua altura, o algoritmo sempre irá usar as configurações da imagem recebida, então imagens com diferentes resoluções, por exemplo 512x512 e 1280x720, podem ser testadas sem a necessidade de alteração no código.

O módulo _Argparse_ teve a função de receber como argumento de linha de comando, juntamente com o argumento:
```console
user@computer:~$ python programa.py image.png
```
> exemplo de execução python com o argumento extra do caminho/nome da imagem.

O módulo _Numpy_ foi usado para realizar a comparação entre as cores dos pixels com a condição de objeto lúminoso.

## Percorrer os pixels
Para haver a checagem de todos os pixels é necessário o uso de dois laços de repetição, dois _for's_, um para ir por cada linha, e outro por cada coluna:
```python
    for i in range(0, height):
        for j in range(0, width):
```
> O valor de _i_ vai de 0 até o valor máximo de altura e o de _j_ de 0 até o valor máximo de largura.

## Verificação e comparação de cores

Numpy arrays, são estruturas de dados do módulo _Numpy_, e com essas estruturas é possível a manipulação, verificação e operações com multiplos arrays, que no caso são usados para armazenar as cores de cada pixel. Por exemplo:
[R,G,B]
```python
light_condition = np.array([12,12,12])
```
A variável _'light_condition'_ é um numpy array que tem como valores em cada índice um valor de R,G ou B
```Python
    light_condition[0] = R
    light_condition[1] = G
    light_condition[2] = B
```
Então a verificação das cores é feita analisando o padrão RGB de cada pixel e comparando com a variável _'light_condition'_.
```Python
if numpy.all(img[i, j] > light_condition):
    cont += 1
```
Então, se o padrão RGB do pixel(X, Y ; sendo X e Y as coordenadas do pixel) for maior que o padrão RGB da variável  _'light_condition'_ a contagem irá ser realizada.

## Filtro de correção de contagem
Há objetos que na imagem possuem mais de 1px(pixel) de 'tamanho' então, esse filtro foi feito com o objetivo de minimizar a contagem extra do mesmo objeto. 

O filtro foi desenvolvido com a lógica de haver a verificação de todos os pixels 'vizinhos' , no caso superior, inferior, esquerdo e direito. e caso todos forem classificados como objetos hávera uma subtração na contagem a fim de buscar um valor mais próximo do real.

```python
if (
    np.all(img[i, j+1]>= light_condition) 
    and np.all(img[i-1, j]>= light_condition) 
    and np.all(img[i+1, j]>= light_condition)  
    and np.all(img[i, j-1]>= light_condition)
    ):
    
    cont = cont - 4
```
> Após a checagem de cores de cada pixel 'vizinho', e confirmar que todos são objetos também, ocorre uma diminuição de 4 unidades na contagem.

## Algoritmo pronto
```python
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
                    if (
                        np.all(img[i, j+1]>= stars_condition) 
                    and np.all(img[i-1, j]>= stars_condition) 
                    and np.all(img[i+1, j]>= stars_condition)  
                    and np.all(img[i, j-1]>= stars_condition)):
                        cont = cont - 4
        print("Está secção possui: {} corpos celestes que emitem ou refletem luz (Filtro aplicado)".format(cont))
```
> Todas as linhas que iniciam com '#' são comentários que são ignoradas pelo programa.
## Testes

## Referências

[1] - https://opencv.org/

[2] - https://docs.python.org/3/library/argparse.html

[3] - https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html