# ft_package — Guide complet de création d'un package Python

## Table des matières

1. [Qu'est-ce qu'un package Python ?](#1-quest-ce-quun-package-python)
2. [Structure du projet](#2-structure-du-projet)
3. [Explication des fichiers](#3-explication-des-fichiers)
   - [pyproject.toml](#31-pyprojecttoml)
   - [ft_package/__init__.py](#32-ft_package__init__py)
   - [ft_package/ft_package.py](#33-ft_packageft_packagepy)
   - [README.md](#34-readmemd)
   - [LICENSE](#35-license)
4. [Comment créer ce package étape par étape](#4-comment-créer-ce-package-étape-par-étape)
5. [Construire le package (build)](#5-construire-le-package-build)
6. [Installer le package](#6-installer-le-package)
7. [Utiliser le package](#7-utiliser-le-package)
8. [Désinstaller le package](#8-désinstaller-le-package)
9. [Concepts clés à retenir](#9-concepts-clés-à-retenir)
10. [Glossaire du débutant](#10-glossaire-du-débutant)

---

## 1. Qu'est-ce qu'un package Python ?

Un **package** Python est un dossier contenant un fichier `__init__.py` (et éventuellement d'autres modules `.py`). Il permet d'organiser du code réutilisable et de le distribuer facilement.

Un **paquet distribuable** (ou *distribution package*) va plus loin : il ajoute des métadonnées (nom, version, auteur, licence...) et peut être installé avec `pip`, partagé sur PyPI, ou simplement construit en fichier `.tar.gz` ou `.whl`.

### Utilité
- **Réutiliser** du code dans plusieurs projets
- **Partager** son code avec d'autres développeurs
- **Distribuer** une bibliothèque via PyPI (Python Package Index)
- **Installer** proprement avec gestion des dépendances

## 2. Structure du projet

```
ex09/
├── ft_package/            # Le package Python (dossier importable)
│   ├── __init__.py        # Rendre le dossier importable + exporter les fonctions
│   └── ft_package.py      # Module contenant le code (count_in_list)
├── pyproject.toml          # Métadonnées et configuration de build
├── README.md               # Documentation (obligatoire pour PyPI)
├── LICENSE                 # Licence du projet (MIT ici)
└── dist/                   # Généré après le build
    ├── ft_package-0.0.1.tar.gz       # Source distribution (sdist)
    └── ft_package-0.0.1-py3-none-any.whl  # Wheel (bdist)
```

## 3. Explication des fichiers

### 3.1 pyproject.toml

Fichier central (standard PEP 621) contenant toutes les métadonnées du paquet :

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "ft_package"
version = "0.0.1"
description = "un exemple de paquet de test"
readme = "README.md"
license = "MIT"
authors = [
    { name = "Herimamy12", email = "nherimam@student.42antananarivo.mg" }
]

[project.urls]
homepage = "https://github.com/Herimamy12/piscine_python/tree/main/ForDataScience/Python_0_Starting"

[tool.setuptools.packages.find]
include = ["ft_package*"]
```

| Champ | Rôle |
|-------|------|
| `[build-system]` | Déclare les outils nécessaires pour construire le paquet |
| `requires` | Liste des dépendances de build (setuptools ici) |
| `build-backend` | Moteur de build utilisé |
| `[project]` | Métadonnées du paquet |
| `name` | Nom du paquet (doit être unique sur PyPI) |
| `version` | Version sémantique (semver : MAJEUR.MINEUR.PATCH) |
| `readme` | Chemin vers le fichier README |
| `license` | SPDX identifier de la licence |
| `authors` | Liste des auteurs avec nom et email |
| `[project.urls]` | URLs supplémentaires (homepage, documentation...) |
| `[tool.setuptools.packages.find]` | Dit à setuptools quels dossiers inclure |

### 3.2 ft_package/__init__.py

Ce fichier est obligatoire pour qu'un dossier soit considéré comme un package Python importable. Il contient :

```python
from .ft_package import count_in_list

__all__ = ["count_in_list"]
```

| Élément | Rôle |
|---------|------|
| `from .ft_package import count_in_list` | Importe la fonction depuis le module voisin (le `.` signifie "dans le même dossier") |
| `__all__` | Liste ce qui est exporté publiquement (contrôle `from ft_package import *`) |

### 3.3 ft_package/ft_package.py

Le module qui contient le code réel :

```python
def count_in_list(lst, item):
    return lst.count(item)
```

Une simple fonction qui utilise la méthode `.count()` native des listes Python.

### 3.4 README.md

Documentation du projet. Pour PyPI, il est fortement recommandé. Il peut être écrit en Markdown (`.md`) ou reStructuredText (`.rst`).

### 3.5 LICENSE

Le fichier de licence. Le choix MIT est permissif : tout le monde peut utiliser, modifier, distribuer le code, même dans des projets propriétaires.

## 4. Comment créer ce package étape par étape

### Étape 1 : Créer la structure de dossiers

```bash
mkdir ft_package
```

### Étape 2 : Écrire le code du module

Crée `ft_package/ft_package.py` avec la fonction `count_in_list`.

### Étape 3 : Créer le fichier __init__.py

Crée `ft_package/__init__.py` qui importe et expose la fonction.

### Étape 4 : Rédiger pyproject.toml

Définir nom, version, auteur, licence...

### Étape 5 : Ajouter README.md et LICENSE

Documentation et licence.

### Étape 6 : Construire le package

```bash
pip install build    # installer l'outil de build
python -m build     # construire le package
```

### Étape 7 : Installer et tester

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
# ou
pip install ./dist/ft_package-0.0.1.tar.gz
```

## 5. Construire le package (build)

### Prérequis

```bash
pip install build
```

### Commander la construction

```bash
python -m build
```

Cette commande génère deux fichiers dans `dist/` :

- **`.tar.gz`** (source distribution / sdist) : contient les sources + un `setup.cfg` généré. Portable, permet de reconstruire le wheel.
- **`.whl`** (wheel / bdist) : format binaire prêt à l'emploi, décompressé directement au bon endroit lors de l'installation. Plus rapide à installer.

### Pourquoi deux formats ?

| Format | Avantage | Usage |
|--------|----------|-------|
| `.tar.gz` (sdist) | Compatible partout, contient les sources | Distribution sur PyPI, compatibilité maximale |
| `.whl` (wheel) | Installation plus rapide, pas de build nécessaire | Usage quotidien, installation directe |

## 6. Installer le package

### Depuis le wheel (recommandé)

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

### Depuis la source

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

### Vérifier l'installation

```bash
pip list                     # voir tous les paquets installés
pip show -v ft_package       # voir les détails du paquet
```

## 7. Utiliser le package

Dans n'importe quel script Python :

```python
from ft_package import count_in_list

resultat1 = count_in_list(["toto", "tata", "toto"], "toto")
print(resultat1)  # 2

resultat2 = count_in_list(["toto", "tata", "toto"], "tutu")
print(resultat2)  # 0
```

Le `from ft_package import count_in_list` fonctionne parce que :

1. Le package `ft_package` est installé dans `site-packages` (dossier des paquets système)
2. Le fichier `ft_package/__init__.py` exporte `count_in_list`
3. Python peut donc résoudre l'import

## 8. Désinstaller le package

```bash
pip uninstall ft_package
```

## 9. Concepts clés à retenir

### Python Package vs Distribution Package

- **Package** : un dossier avec `__init__.py` (importable dans Python)
- **Distribution package** : un package + métadonnées, prêt à être distribué (ce qu'on crée avec `python -m build`)

### Le circuit complet

```
Code source → pyproject.toml → python -m build → dist/*.whl → pip install → site-packages/ → import
```

### Commandes essentielles

| Commande | Action |
|----------|--------|
| `python -m build` | Construire le paquet |
| `pip install ./dist/paquet-version.whl` | Installer le paquet |
| `pip show -v nom_du_paquet` | Afficher les détails |
| `pip list` | Lister les paquets installés |
| `pip uninstall nom_du_paquet` | Désinstaller |

### Pour aller plus loin

- **PyPI** (Python Package Index) : dépôt public où publier son paquet (`pip upload`)
- **Test PyPI** : https://test.pypi.org/ pour s'entraîner avant la publication officielle
- **setup.py** : l'ancienne méthode (encore supportée) — `pyproject.toml` est le standard moderne
- **setup.cfg** : alternative à `pyproject.toml` pour setuptools

## 10. Glossaire du débutant

| Terme | Définition |
|-------|------------|
| **Package** | Dossier contenant `__init__.py` et des modules Python |
| **Module** | Fichier `.py` contenant du code Python |
| **Distribution** | Paquet prêt à être installé (`.tar.gz` ou `.whl`) |
| **pip** | Gestionnaire de paquets de Python (Pip Installs Packages) |
| **PyPI** | Python Package Index, le dépôt officiel des paquets Python |
| **sdist** | Source distribution (`.tar.gz`), contient les sources |
| **wheel** | Format binaire (`.whl`), installation rapide |
| **setuptools** | Bibliothèque standard pour construire des paquets Python |
| **build** | Outil moderne pour construire des paquets (recommande par PyPA) |
| **pyproject.toml** | Fichier de configuration standard (PEP 518, PEP 621) |
| **`__init__.py`** | Fichier qui rend un dossier importable comme package |
| **`__all__`** | Liste des noms exportés publiquement par un module |
| **Metadata-Version** | Version du format des métadonnées du paquet |
| **site-packages** | Dossier où pip installe les paquets Python |
| **SPDX** | Format standard pour identifier les licences (ex: "MIT") |

---

*Documentation créée dans le cadre du projet Piscine Python — Python 0 — ex09*
