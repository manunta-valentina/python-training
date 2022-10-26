fruits = ["mela", "banana", "fragola"] #crea una lista
for x in fruits: #il ciclo for viene utilizzato per l'iterazione sulla lista
  print(x) # stampa le variabili della lista
  if x == 'banana':  # pongo la x uguale a una variabile
     break  #utilizzando break possiamo interrompere il ciclo prima che abbia eseguito il ciclo di tutti gli elementi presenti nella lista, in
      questo caso stamperà fino a banana
 
 
fruits = ["mela", "banana", "fragola"]   #crea una lista
for x in fruits: #il ciclo for viene utilizzato per l'iterazione sulla lista
  if x == "fragola": # pongo la x uguale a una variabile
    break   #utilizzando break possiamo interrompere il ciclo prima che abbia eseguito il ciclo di tutti gli elementi presenti nella lista
  print(x)  # metendo il print dopo esci dal ciclo quando x è "fragola", ma questa volta la pausa viene prima della stampa, quindi stamperà gli elementi mela e banana ma
  non fragola
 
 

fruits = ["mela", "banana", "fragola"]  #crea una lista
for x in fruits:  #il ciclo for viene utilizzato per l'iterazione sulla lista
  if x == "banana":  # pongo la x uguale a una variabile
    continue   #utilizzando continue possiamo interrompere il ciclo e continuare con la successiva, quindi stamperà mela e fragola(salta banana)
  print(x)  # stampa le variabili della lista