# Changelog :

All notable changes to this project are documented here.  


---

## [1.0.0] - 2026-05-11

### Added
- CSV file loading via the file explorer or by pasting a file path ;
- Preview of the first 3 rows of the dataset ;
- Selection of 1 or 2 feature columns and one target column ;
- Automatic handling of missing values ;
- Training of a linear regression model using scikit-learn ;
- Display of metrics: MSE, R² score, coefficients, and intercept ;
- 2D graph with regression line ;
- 3D graph with regression plane ;
- Customisable colours (slope, training data, test data) ;
- Application restart button.


## [1.1.0] - 2026-05-16

### Added
- A spot added at the bottom of the interface to predict values ;

### Fixed
- Fixed a bug in the predict function of model.py.


## [2.0.0] - 2026-06-14

### Added
- Support for more than two features (up to 10).
- Prediction-vs-actual graph with an ideal reference line when visualisation in higher dimensions is not possible.

### Changed
- Complete redesign of the user interface while still using ttk.
- Most of the codebase has been adapted to support multiple features.
- Graph behaviour now changes automatically when more than two features are selected.

#### Acknowledgements
I admit having used AI to create a visually appealing design, as designing one entirely by myself would have been rather time-consuming.


## [2.0.1] - 2026-06-16

### Fixed
- Replaced backslashes with forward slashes in image paths so that images now load correctly.


## [2.0.1.1] - 2026-06-18

### Fixed
- Replace the image in the comparative chart with the correct version in the README.


# Changelog (In french) :
 
Toutes les modifications notables de ce projet sont documentées ici.

---
 
## [1.0.0] - 2026-05-11
 
### Ajouté
- Chargement d'un fichier CSV via l'explorateur de fichiers ou en collant un chemin ;
- Aperçu des 3 premières lignes du jeu de données ;
- Sélection de 1 ou 2 colonnes features et d'une colonne cible ;
- Gestion automatique des valeurs manquantes ;
- Entraînement d'un modèle de régression linéaire (scikit-learn) ;
- Affichage des métriques : MSE, R², coefficients et ordonnée à l'origine ;
- Graphique 2D avec droite de régression ;
- Graphique 3D avec plan de régression ;
- Personnalisation des couleurs (pente, données d'entraînement, données de test) ;
- Bouton de redémarrage de l'application.

 

## [1.1.0] - 2026-05-16

### Ajouté
- Endroit ajouté pour prédire des valeurs en bas de l'interface ;
- Bug corrigé dans **model.py** dans la fonction *predict*.



## [2.0.0] - 2026-06-14

### Ajouté
- Possibilité d'utiliser plus de deux variables explicatives (jusqu'à 10).
- Ajout d'un graphique comparant les valeurs prédites aux valeurs réelles, accompagné d'une ligne de référence idéale lorsque la visualisation en dimensions supérieures n'est pas possible.

### Modifié
- Refonte complète de l'interface utilisateur, tout en conservant ttk.
- Une grande partie du code a été adaptée afin de prendre en charge plusieurs variables explicatives.
- Le comportement du graphique s'adapte désormais automatiquement lorsque plus de deux variables explicatives sont sélectionnées.


#### Reconnaissance
J'avoue avoir eu recours à l'IA pour créer un design visuellement attractif, car le concevoir entièrement moi-même serait une perte de temps.

## [2.0.1] - 2026-06-16

### Corrigé
- Remplacement des antislashs (« \ ») par des slashs (« / ») dans les chemins d'accès des images afin qu'elles se chargent désormais correctement.


## [2.0.1.1] - 2026-06-18

### Corrigé
- Correction du lien vers le graphique comparatif dans le fichier README.