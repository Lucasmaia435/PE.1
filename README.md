<h2>
ESCOLA DE CIÊNCIAS E TECNOLOGIA
<br>
PROBABILIDADE E ESTATÍSTICA 
</h2>
<h3>
Professor : João Vital da Cunha Júnior 
<br>
Alunos : Lucas Maia Rezende Costa e Ariel Louise Queiros de Morais
</h3>
<br>
<h1 align='center'> 
Contador de objetos emissores e/ou refletores de luz no espaço
</h1>
Este trabalho foi feito no âmbito de realizar a contagem de objetos encontrados em imagens do espaço, a fim de futuramente ocorrer a diferenciação dos objetos através da sua coloração. O algoritmo do contador consiste em uma verificação pixel por pixel da imagem, e se o pixel saciar a condição de objeto luminoso, este então será contado.

O desenvolvimento do algoritmo foi feito em Python com o auxílio do seguintes módulos:

* OpenCV ou cv2;
* Argparse;
* Numpy;

O módulo OpenCV foi usado para ler, corrigir e percorrer todos os pixels da imagem a fim de recolher as suas cores. 
  
O módulo Argparse teve a função de receber como argumento de linha de comando, juntamente com o argumento 
```console
user@computer:~$ python programa.py image.png
```

O módulo Numpy foi usado para realizar a comparação entre as cores dos pixels com a condição de objeto lúminoso.

```python
light_condition = [12,12,12]
if numpy.all(img[i, j] > stars_condition):
    cont += 1
```
Sabendo que a imagem é uma matriz NxM, e que N é sua largura e M sua altura, o algoritmo sempre irá usar as configurações da imagem recebida, então imagens com diferentes resoluções, por exemplo 512x512 e 1280x720, podem ser testadas sem a necessidade de alteração no código.

Após a contagem, o programa é encerrado e retorna para o usuário no terminal a seguinte mensagem:

```console
Está secção possui: 23 corpos que emitem ou refletem luz
```


