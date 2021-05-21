 
# Tarea 3: Chat usando el modelo Gossip
## Marcos Adrián Valdivié Rodríguez C412

La implementación proporciondada consiste en una clase llamada Node, esta es la encargada de comunicarse con los demás usuarios. 

La clase recibe al iniciarse un puerto, al que se vinculará el proceso que está corriendo para recibir y enviar mensajes y un array de puertos correspondiente a los vecinos inmediatos del nodo en el grafo subyacente. 

Al instanciarse la clase se creará un socket UDP y se vinculará al puerto correspondiente. Además se iniciarán los hilos correspondientes al envío y recibo de mensajes.

La clase posee tres métodos:

1. **sendFromInput** que se ocupa de tomar lo que se ha escrito a la consola y llamar al método gossip para enviar ese mensaje a los nodos adyacentes.

2. **receive** que se ocupa de recibir cada mensaje, y reenviarlo en caso de que sea la primera vez que se recibe ese mensaje.

3. **gossip** que es el encargado de reenviar los mensajes a los nodos adyacentes.

***
Para ejecutar el programa es necesario antes haber preparado los archivos txt, estos en particular tendrán primero el puerto al cual se vinculará el nodo y luego los puertos de los nodos adyacentes separados por cada línea. Se prepararon algunos de estos archivos para la prueba.

Para probar el programa se debe correr el script con el comando 

```bash
$ pyhton3 Node.py --name <id>
```
donde <id> es el nombre del archivo txt correspondiente al nodo que se desea incializar (A, B, C, D en el caso de ejemplo proporcionado) y además el nombre que será usado para identificar quien envió cada mensaje.

***
Para el desarrollo del programa se usaron los módulos socket, random, time, threading y argparse de python.