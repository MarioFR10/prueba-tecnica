# Prueba tecnica ELVA

## Autor: Mario Fernández Robert
#

<h2 align="center">
  Guía de uso
</h2>

* Clonar repositorio mediante en siguiente comando (es necesario tener git)
```
git clone https://github.com/MarioFR10/prueba-tecnica.git
```

* Dirigirse a la carpeta en donde se clonó el repositorio

```
cd .\prueba-tecnica
```
* Ejecutar el programa, existen 2 parametros necesarios para el correcto funcionamiento el primero es la palabra que se desea descomponer y el segundo son la serie de palabras contra las que se evaluará
```
python .\word-split.py hellocat apple,bat,cat,goodbye,hello,yellow,why
```
* Ejemplo de funcionamiento
```
$ python .\word-split.py hellocat apple,bat,cat,goodbye,hello,yellow,why
$ hello,cat
```