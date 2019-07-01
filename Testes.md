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

# Testes

## Primeiro teste
A seguinte imagem, possui 15 objetos, porém 19 pixels coloridos com cores a cima do padrão _light_condition_, ou seja, irão ser contados :
<img src="images/test_15.png">

Resultado:
```console
Está secção possui: 19 corpos celestes que emitem ou refletem luz
Aplicar filtro?[y/n]
y 
Está secção possui: 15 corpos celestes que emitem ou refletem luz (Filtro aplicado)
```

Então esse teste teve 100% de êxito.


## Segundo teste

A seguinte imagem, possui 44 objetos, porém 5 objetos possuem mais de 1px² de área :
<img src="images/test_44_5.png">

Resultado: 
```console
Está secção possui: 44 corpos celestes que emitem ou refletem luz
Aplicar filtro?[y/n]
y
Está secção possui: 8 corpos celestes que emitem ou refletem luz (Filtro aplicado)
```
Esse teste obteve uma contagem de 3 objetos a mais.