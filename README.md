# Linear Regression App
This is a small application that allows you to **see how powerful your model is** and **visualise linear regression** with a CSV file. 


## Before Getting Started

>The purpose of linear regression is to predict **the value of something** (often represented on the *y-axis*) using **one or more parameters** (often represented on the *x-axis*).

![image](images\1Images\Figure_1.png)

>- The slope is the regression line shown in red.
>- The intercept is the value of the y-axis when x = 0.

>As we can see here, we can somehow predict a student's mark based on their study hours.

We can even add another parameter and represent the regression using a three-dimensional graph, like this:

![image](images\1Images\Figure_2.png)

Nevertheless, we unfortunately cannot represent the regression with more than two features because humans are unable to see in four dimensions (or more) ! 
## Features :


* Can load a CSV file ;
* Preview dataset columns ;
* Choose the column you want to predict (y);
* Choose the Select independent variables (features/parameters) ;
* Displays all the necessary information and metrics about the model ;
* Customise visualisation settings ;
* Display the final graph ; 
* A restart button on the left ;
* A prediction area to forecast the Y-axis using the entered features.


## How to utilise it :
### Lauch the application :
```bash
python main.py
```

### In the app :

#### Choose a CSV file :
* You need to either choose a CSV file through the "choose CSV" button or paste a CSV-file path by clicking on the second RadioButton :


![image](images\2Images\pick_csv.png) 



![image](images\2Images\pick_csv2.png) 


Or :


![image](images\2Images\pick_csv_bypath.png) 
    *and click on the confirm button and please remove the parentheses !*

#### Insert the independant varables :
Now that the CSV file is loaded, let's **insert the independent variables** (The column(s) which will predict the *Y axis*), you can refer to the CSV preview ; when you have finished, click on the **"confirm"** button ! :

![image](images\2Images\treeview_of_csv.png)
    *Example of a treeview*




![image](images\2Images\features_2D.png)
    *Note that string values are not valid and will raise an error*


![image](images\2Images\features_3D.png)
    *In 3D (2 features)*


![image](images\2Images\features_mt3D.png)
    *With more than 2 features*


#### Setting the colour of the graph's features :
Afterwards, let's set the colours of our future graph :



![image](images\2Images\choosing_colours2.png)
    *You just have to click on the "pick" button and choose the colour like that.*



Please note that if you have inserted more than two features, it is normal to be able to customise only two colours, as the graph will not actually display the real regression. Instead, it will compare the predicted and actual values on a 2D graph.


![image](images\2Images\colours_choice_mt3D.png) 




> **Please note that you can access all the necessary information about the linear regression training.**
>
> - The coefficient(s)  represents how much the marks increase when the study time increases by 1 unit.
> - The R² score indicates how accurate the model is. Here, a score of 0.904 means the model is fairly accurate.  
>   - 0 = useless model  
>   - 1 = perfect model
> - The MSE (*Mean Squared Error*) represents the average squared error between the predicted values and the real values. Lower is better.
> If you ever want to explore that further, I recommend taking a look at scikit-learn's documentation. Nevertheless, the material is presented in a highly detailed manner, and you'd better have a solid grasp of the fundamentals of mathematics.
> https://scikit-learn.org/stable/getting_started.html



#### Displaying the graph : 
* Once you have finished setting the colours, you can press the 'Confirm' button to display the graph.
*Please note that you needn't press the "Confirm" button if the graph is already displayed, as it is not possible to display two graphs at the same time.*

##### Small example (Image at the beginning) :

![image](images\1Images\Figure_1.png)
    *In 2D*


![image](images\2Images\graph_example_3D.png)
    *In 3D*


![image](images\2Images\metrics_3D(2).png)
    *Comparing graph (more than 2 features)*




### Downloading the graph :
If you want to download the graph by any chance, click on the button at the bottom of the graph :



![image](images\1Images\image.png)



### Predicting values :

This app will also enable you to predict the values that you enter yourself at the bottom of the interface. No matter the number of parameters; you just have to use a semi-colon when entering several parameters :

![image](images\2Images\predicting_values2D.png)
    *With one parameter.*



![image](images\2Images\predicting_valuesmt3D.png)
    *With more parameters.*




## Requirements :
> - Python 3.11+
> - Scikit-learn: The module used to train models and make predictions. 
> - Matplotlib (.pyplot): The module used to plot and visualise data.
> - Pandas: Handles data easily with just a few lines of code.
> - NumPy: Used for faster numerical calculations. 
>
> We can all see that it's too much. Fortunately, you can download everything at once using the terminal command : 
>```bash
>pip install -r requirements.txt
>```
> If you ever use the python launcher (for windows), as I do ; you will have to run this command :
>```bash
>py -(the_version) -m pip install -r requirements.txt
>```
> ![image](images\1Images\image_teminal.png)


## How it works :
### The structure/tree


```text
│   .gitignore
│   CHANGELOG.md
│   main.py
│   README.md
│   requirements.txt
│
├───core
│   │   data.py
│   │   model.py
│   │   __init__.py
│   │
│   └───__pycache__
│           data.cpython-314.pyc
│           model.cpython-314.pyc
│           __init__.cpython-314.pyc
│
├───images
│   ├───1Images
│   │       Choose_colour.png
│   │       Choose_csv.png
│   │       Figure_1.png
│   │       Figure_2.png
│   │       File_explorer.png
│   │       image.png
│   │       image_teminal.png
│   │       Path_pasting.png
│   │       predict_one_parameter.png
│   │       predict_two_parameters.png
│   │       Selecting_columns.png
│   │       Show_colours.png
│   │
│   └───2Images
│           choosing_colours1.png
│           choosing_colours2.png
│           colours_choice.png
│           colours_choice_mt3D.png
│           features_2D.png
│           features_3D.png
│           features_mt3D.png
│           graph_example_2D.png
│           graph_example_3D.png
│           graph_example_vs.png
│           metrics_2D.png
│           metrics_3D(2).png
│           metrics_3D.png
│           metrics_mt3D.png
│           pick_csv.png
│           pick_csv2.png
│           pick_csv_bypath.png
│           predicting_values2D.png
│           predicting_valuesmt3D.png
│           Screenshot 2026-06-14 141229.png
│           treeview_of_csv.png
│
└───ui
    │   app.py
    │   plot.py
    │   __init__.py
    │
    └───__pycache__
            app.cpython-314.pyc
            plot.cpython-314.pyc
            __init__.cpython-314.pyc
    

```

### What does each file do?
> - **data.py** handles everything related to the dataset : loading the CSV, dropping rows with missing values, validating and extracting the feature/target columns, and detecting non-numeric columns.
> - **model.py** trains a linear regression model on the data, evaluates it (R2, MSE), and has a method for predictining values you enter yourself.
> - **plot.py** is used to draw graphs. It can also identify whether a graph is two-dimensional or three-dimensional.
> - **app.py** — the core of the application. It builds the entire tkinter(ttk) interface, handles user interactions, and coordinates `data.py` and `model.py` to load data, train the model, and display the results by using `plot.py`.    
> - The **images** file is used to save the images shown in this README.
> The subfolder **1Images** saves all the images used in the first version.
> The other subfolder **2Images** saves images with the new interface released in the [2.0.0] version.
> - All files in both `_pycache_` are not imporant, don't consider them.
> - **main.py** is basically for linking the files in the UI folder to the files in the core folder.
> - The **.gitignore** file is used for hiding files. In this case : `_pycache_`.
> - **CHANGELOG.md** shows all the changes made when moving to a new version.
> - **README.md** is just simply this file.
> - Both **__init__** files allow **main.py** to communicate with the files inside the **ui** and **core** folders.
> - You can see a quick descrption of all of the functions in the code as well.

## Future improvements

> - A better interface ;
> - Display a residuals plot.





# Application de Régression Linéaire (in french)

Il s'agit d'une petite application qui vous permet de **voir à quel point votre modèle est puissant** et de **visualiser une régression linéaire** à partir d'un fichier CSV. 


## Avant de commencer

>L'objectif de la régression linéaire est de prédire **la valeur de quelque chose** (souvent représentée sur l'*axe y*) à partir **d'un ou plusieurs paramètres** (souvent représentés sur l'*axe x*).

![image](images\1Images\Figure_1.png)

>- La pente est la droite de régression affichée en rouge.
>- L'ordonnée à l'origine est la valeur de l'axe y lorsque x = 0.

>Comme on peut le voir ici, on peut d'une certaine façon prédire la note d'un élève en fonction de son temps d'étude.

On peut même ajouter un autre paramètre et représenter la régression à l'aide d'un graphique en trois dimensions, comme ceci :

![image](images\1Images\Figure_2.png)

Néanmoins, nous ne pouvons malheureusement pas représenter la régression avec plus de deux variables, car les êtres humains sont incapables de voir en quatre dimensions (ou plus) !

## Fonctionnalités :


* Chargement d'un fichier CSV ;
* Aperçu des colonnes du jeu de données ;
* Choix de la colonne à prédire (y) ;
* Choix des variables indépendantes (features/paramètres) ;
* Affichage de toutes les informations et indicateurs nécessaires concernant le modèle ;
* Personnalisation des paramètres de visualisation ;
* Affichage du graphique final ;
* Un bouton de redémarrage à gauche ;
* Une zone de prédiction pour estimer la valeur de l'axe Y à partir des features saisies.


## Comment l'utiliser :
### Lancer l'application :
```bash
python main.py
```

### Dans l'application :

#### Choisir un fichier CSV :
* Vous devez soit choisir un fichier CSV via le bouton "choose CSV", soit coller un chemin de fichier CSV en cliquant sur le deuxième RadioButton :


![image](images\2Images\pick_csv.png) 



![image](images\2Images\pick_csv2.png) 


Ou :


![image](images\2Images\pick_csv_bypath.png) 
    *et cliquez sur le bouton "confirm" et veuillez supprimer les parenthèses !*

#### Insérer les variables indépendantes :
Maintenant que le fichier CSV est chargé, **insérons les variables indépendantes** (la ou les colonnes qui permettront de prédire l'*axe Y*). Vous pouvez vous appuyer sur l'aperçu du CSV ; une fois terminé, cliquez sur le bouton **"confirm"** ! :

![image](images\2Images\treeview_of_csv.png)
    *Exemple d'un aperçu (treeview)*




![image](images\2Images\features_2D.png)
    *Notez que les valeurs textuelles ne sont pas valides et déclencheront une erreur*


![image](images\2Images\features_3D.png)
    *En 3D (2 features)*


![image](images\2Images\features_mt3D.png)
    *Avec plus de 2 features*


#### Paramétrer la couleur des features du graphique :
Ensuite, paramétrons les couleurs de notre futur graphique :



![image](images\2Images\choosing_colours2.png)
    *Il vous suffit de cliquer sur le bouton "pick" et de choisir la couleur de cette façon.*



Veuillez noter que si vous avez inséré plus de deux features, il est normal de ne pouvoir personnaliser que deux couleurs, car le graphique n'affichera pas la régression réelle. À la place, il comparera les valeurs prédites et les valeurs réelles sur un graphique 2D.


![image](images\2Images\colours_choice_mt3D.png) 




> **Veuillez noter que vous pouvez accéder à toutes les informations nécessaires concernant l'entraînement de la régression linéaire.**
>
> - Le ou les coefficients représentent de combien les notes augmentent lorsque le temps d'étude augmente d'une unité.
> - Le score R² indique la précision du modèle. Ici, un score de 0.904 signifie que le modèle est assez précis.  
>   - 0 = modèle inutile  
>   - 1 = modèle parfait
> - Le MSE (*Mean Squared Error* — erreur quadratique moyenne) représente l'erreur moyenne au carré entre les valeurs prédites et les valeurs réelles. Plus il est faible, mieux c'est.
> Si vous souhaitez approfondir le sujet, je vous recommande de consulter la documentation de scikit-learn. Néanmoins, le contenu y est présenté de manière très détaillée, et il vaut mieux avoir une solide maîtrise des fondamentaux mathématiques.
> https://scikit-learn.org/stable/getting_started.html



#### Afficher le graphique : 
* Une fois les couleurs définies, vous pouvez appuyer sur le bouton "Confirm" pour afficher le graphique.
*Veuillez noter qu'il n'est pas nécessaire d'appuyer sur le bouton "Confirm" si le graphique est déjà affiché, car il n'est pas possible d'afficher deux graphiques en même temps.*

##### Petit exemple (image du début) :

![image](images\1Images\Figure_1.png)
    *En 2D*


![image](images\2Images\graph_example_3D.png)
    *En 3D*


![image](images\2Images\metrics_3D(2).png)
    *Graphique de comparaison (plus de 2 features)*




### Télécharger le graphique :
Si jamais vous souhaitez télécharger le graphique, cliquez sur le bouton en bas du graphique :



![image](images\1Images\image.png)



### Prédiction de valeurs :

Cette application vous permettra également de prédire les valeurs que vous saisissez vous-même en bas de l'interface. Quel que soit le nombre de paramètres, il vous suffit d'utiliser un point-virgule pour saisir plusieurs paramètres :

![image](images\2Images\predicting_values2D.png)
    *Avec un paramètre.*



![image](images\2Images\predicting_valuesmt3D.png)
    *Avec plusieurs paramètres.*




## Prérequis :
> - Python 3.11+
> - Scikit-learn : le module utilisé pour entraîner les modèles et effectuer des prédictions. 
> - Matplotlib (.pyplot) : le module utilisé pour tracer et visualiser les données.
> - Pandas : gère facilement les données en quelques lignes de code.
> - NumPy : utilisé pour des calculs numériques plus rapides. 
>
> On peut voir que c'est beaucoup. Heureusement, vous pouvez tout installer en une seule commande via le terminal : 
>```bash
>pip install -r requirements.txt
>```
> Si jamais vous utilisez le lanceur Python (pour Windows), comme moi ; vous devrez exécuter cette commande :
>```bash
>py -(the_version) -m pip install -r requirements.txt
>```
> ![image](images\1Images\image_teminal.png)


## Fonctionnement :
### La structure/arborescence


```text
│   .gitignore
│   CHANGELOG.md
│   main.py
│   README.md
│   requirements.txt
│
├───core
│   │   data.py
│   │   model.py
│   │   __init__.py
│   │
│   └───__pycache__
│           data.cpython-314.pyc
│           model.cpython-314.pyc
│           __init__.cpython-314.pyc
│
├───images
│   ├───1Images
│   │       Choose_colour.png
│   │       Choose_csv.png
│   │       Figure_1.png
│   │       Figure_2.png
│   │       File_explorer.png
│   │       image.png
│   │       image_teminal.png
│   │       Path_pasting.png
│   │       predict_one_parameter.png
│   │       predict_two_parameters.png
│   │       Selecting_columns.png
│   │       Show_colours.png
│   │
│   └───2Images
│           choosing_colours1.png
│           choosing_colours2.png
│           colours_choice.png
│           colours_choice_mt3D.png
│           features_2D.png
│           features_3D.png
│           features_mt3D.png
│           graph_example_2D.png
│           graph_example_3D.png
│           graph_example_vs.png
│           metrics_2D.png
│           metrics_3D(2).png
│           metrics_3D.png
│           metrics_mt3D.png
│           pick_csv.png
│           pick_csv2.png
│           pick_csv_bypath.png
│           predicting_values2D.png
│           predicting_valuesmt3D.png
│           Screenshot 2026-06-14 141229.png
│           treeview_of_csv.png
│
└───ui
    │   app.py
    │   plot.py
    │   __init__.py
    │
    └───__pycache__
            app.cpython-314.pyc
            plot.cpython-314.pyc
            __init__.cpython-314.pyc
    

```

### Rôle de chaque fichier :
> - **data.py** gère tout ce qui concerne le jeu de données : chargement du CSV, suppression des lignes avec des valeurs manquantes, validation et extraction des colonnes features/cible, et détection des colonnes non numériques.
> - **model.py** entraîne un modèle de régression linéaire sur les données, l'évalue (R², MSE), et dispose d'une méthode pour prédire les valeurs que vous saisissez vous-même.
> - **plot.py** sert à tracer les graphiques. Il peut également identifier si un graphique est en deux dimensions ou en trois dimensions.
> - **app.py** — le cœur de l'application. Il construit toute l'interface tkinter(ttk), gère les interactions utilisateur, et coordonne `data.py` et `model.py` pour charger les données, entraîner le modèle, et afficher les résultats à l'aide de `plot.py`.    
> - Le dossier **images** sert à sauvegarder les images affichées dans ce README.
> Le sous-dossier **1Images** sauvegarde toutes les images utilisées dans la première version.
> L'autre sous-dossier **2Images** sauvegarde les images de la nouvelle interface publiée dans la version [2.0.0].
> - Tous les fichiers dans les deux `_pycache_` ne sont pas importants, ne les prenez pas en compte.
> - **main.py** sert essentiellement à relier les fichiers du dossier UI aux fichiers du dossier core.
> - Le fichier **.gitignore** sert à masquer des fichiers. Dans ce cas : `_pycache_`.
> - **CHANGELOG.md** affiche tous les changements effectués lors du passage à une nouvelle version.
> - **README.md** est tout simplement ce fichier.
> - Les deux fichiers **__init__** permettent à **main.py** de communiquer avec les fichiers des dossiers **ui** et **core**.
> - Vous pouvez également voir une description rapide de toutes les fonctions directement dans le code.

## Améliorations futures

> - Une meilleure interface ;
> - Affichage d'un graphique des résidus.