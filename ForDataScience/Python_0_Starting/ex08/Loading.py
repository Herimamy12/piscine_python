#!/usr/bin/env python3

"""Barre de progression minimaliste inspirée de tqdm.

Fournit un itérateur `ft_tqdm` qui affiche une barre de progression
dans le terminal, dont le format est identique à celui de tqdm.

Utilisation :
    from Loading import ft_tqdm
    for x in ft_tqdm(range(100), desc='Traitement'):
        ...
"""

import sys
import time
import shutil


def ft_tqdm(iterable=None, *, total=None, desc='', leave=True,
            ncols=None, mininterval=0.1, unit='it', unit_scale=False,
            file=None, ascii=False):
    """Retourne un itérateur avec barre de progression (comme tqdm).

    Paramètres
    ----------
    iterable : iterable, optionnel
        L'itérable à parcourir.
    total : int, optionnel
        Nombre total d'itérations. Si None, on utilise len(iterable).
    desc : str
        Texte descriptif affiché avant la barre.
    leave : bool
        Si True, la barre reste affichée après la fin (défaut : True).
    ncols : int, optionnel
        Largeur totale en caractères. Si None, la barre fait
        10 caractères par défaut (comportement tqdm).
    mininterval : float
        Intervalle minimum en secondes entre deux mises à jour
        (défaut : 0.1).
    unit : str
        Unité affichée (défaut : 'it').
    unit_scale : bool
        Si True, les nombres sont divisés par 1000 avec un préfixe
        (k, M, G, T).
    file : file, optionnel
        Flux de sortie (défaut : sys.stderr).
    ascii : bool
        Si True, utilise '#' au lieu du caractère Unicode '█'.

    Retour
    ------
    _Tqdm
        Itérateur affichant une barre de progression.
    """

    class _Tqdm:
        """Itérateur interne gérant l'affichage de la barre de progression."""

        def __init__(self, iterable, total, desc, leave, ncols,
                     mininterval, unit, unit_scale, file, ascii):
            self.iterable = iterable
            self.total = total if total is not None else (
                len(iterable) if hasattr(iterable, '__len__') else None)
            self.desc = desc or ''
            self.leave = leave
            self.ncols = ncols
            self.mininterval = mininterval
            self.unit = unit
            self.unit_scale = unit_scale
            self.file = file or sys.stderr
            self.ascii = ascii

            self.n = 0
            self.debut = None
            self.dernier_affichage = 0.0
            self.ferme = False

        def __iter__(self):
            """Parcourt l'itérable et met à jour la barre à chaque étape."""
            if self.iterable is None:
                raise TypeError("ft_tqdm() nécessite un itérable")
            self.debut = time.time()
            self._afficher()  # état initial à 0%
            for element in self.iterable:
                yield element
                self.update(1)
            self.close()

        def update(self, n=1):
            """Incrèmente le compteur et rafraîchit l'affichage si nécessaire.

            Paramètres
            ----------
            n : int
                Nombre d'unités ajoutées (défaut : 1).
            """
            maintenant = time.time()
            if self.debut is None:
                self.debut = maintenant
            self.n += n
            if (maintenant - self.dernier_affichage >= self.mininterval
                    or (self.total and self.n >= self.total)):
                self.dernier_affichage = maintenant
                self._afficher()

        def _afficher(self):
            """Affiche la barre de progression sur le flux de sortie."""
            try:
                barre = self._formater()
                print(barre, end='\r', file=self.file)
                self.file.flush()
            except Exception:
                pass

        def _formater(self):
            """Construit la chaîne formatée comme la barre de tqdm.

            Le format respecté est :
                {desc}: {pct:3d}%|{barre}| {n}/{total}
                    [{temps_écoulé}<{eta}, {taux}{unit}/s]

            Retour
            ------
            str
                La ligne de progression formatée.
            """
            maintenant = time.time()
            ecoule = maintenant - (self.debut or maintenant)

            if self.total:
                fraction = min(float(self.n) / self.total, 1.0)
                pourcentage = int(fraction * 100)

                # Début de la ligne : description + pourcentage
                if self.desc:
                    debut = f"{self.desc}: {pourcentage:3d}%|"
                else:
                    debut = f"{pourcentage:3d}%|"

                # Compteur (n/total)
                if self.unit_scale:
                    total_str = self._echelle(self.total)
                    n_str = self._echelle(self.n)
                else:
                    total_str = str(self.total)
                    n_str = str(self.n)

                compteur = f" {n_str}/{total_str}"

                # Métriques : taux et ETA
                if self.n > 0 and ecoule > 0:
                    taux = self.n / ecoule
                    eta = (self.total - self.n) / taux
                    eta_str = self._format_tps(eta)

                    if self.unit_scale:
                        if taux >= 1000:
                            taux_str = self._echelle(taux)
                        else:
                            taux_str = f"{int(taux)}"
                    else:
                        taux_str = f"{taux:6.2f}"

                    metriques = (
                        f" [{self._format_tps(ecoule)}<{eta_str}, "
                        f"{taux_str}{self.unit}/s]"
                    )
                else:
                    # n == 0 : on ne connaît pas encore le taux ni l'ETA
                    metriques = (
                        f" [{self._format_tps(ecoule)}<?, "
                        f"?{self.unit}/s]"
                    )

                # Suffixe complet après la barre
                suffixe = f"|{compteur}{metriques}"

                # Calcul de la largeur disponible pour la barre
                if self.ncols:
                    # Mode adaptatif : la barre utilise toute la largeur
                    largeur_barre = max(
                        3, self.ncols - len(debut) - len(suffixe))
                else:
                    # Mode par défaut : barre de 10 caractères (tqdm)
                    largeur_barre = 10

                # Construction de la barre
                if self.ascii:
                    # Mode ASCII : '#' pour rempli, ' ' pour vide
                    remplis = int(largeur_barre * fraction)
                    barre = '#' * remplis + ' ' * (largeur_barre - remplis)
                else:
                    # Mode Unicode : █ (U+2588) et blocs partiels
                    blocs_partiels = [
                        '', '\u258F', '\u258E', '\u258D', '\u258C',
                        '\u258B', '\u258A', '\u2589',
                    ]
                    remplis = largeur_barre * fraction
                    pleins = int(remplis)
                    reste = int((remplis - pleins) * 8)

                    if pleins >= largeur_barre:
                        barre = '\u2588' * largeur_barre
                    elif reste == 0:
                        barre = ('\u2588' * pleins
                                 + ' ' * (largeur_barre - pleins))
                    else:
                        barre = ('\u2588' * pleins
                                 + blocs_partiels[reste - 1]
                                 + ' ' * (largeur_barre - pleins - 1))

                return f"{debut}{barre}{suffixe}"
            else:
                # Mode sans total connu
                if self.desc:
                    debut = f"{self.desc}: "
                else:
                    debut = ""

                if self.n > 0 and ecoule > 0:
                    taux = self.n / ecoule
                    if self.unit_scale:
                        if taux >= 1000:
                            taux_str = self._echelle(taux)
                        else:
                            taux_str = f"{int(taux)}"
                    else:
                        taux_str = f"{taux:6.2f}"
                    metriques = (
                        f" [{self._format_tps(ecoule)}, "
                        f"{taux_str}{self.unit}/s]"
                    )
                else:
                    metriques = (
                        f" [{self._format_tps(ecoule)}, "
                        f"?{self.unit}/s]"
                    )

                return f"{debut}{self.n} {self.unit}{metriques}"

        @staticmethod
        def _format_tps(secondes):
            """Convertit des secondes en chaîne mm:ss ou h:mm:ss.

            Paramètres
            ----------
            secondes : float
                Durée en secondes.

            Retour
            ------
            str
                Temps formaté (ex: '00:00', '01:23', '1:02:03').
            """
            try:
                s = int(secondes)
            except Exception:
                s = 0
            h = s // 3600
            m = (s % 3600) // 60
            s = s % 60
            if h:
                return f"{h:d}:{m:02d}:{s:02d}"
            return f"{m:02d}:{s:02d}"

        @staticmethod
        def _echelle(valeur):
            """Formate un nombre avec un préfixe d'unité (k, M, G, T).

            Exemples : 0 → '0.00', 71 → '71.0', 145 → '145',
            1030 → '1.03k', 2000 → '2.00k'.

            Paramètres
            ----------
            valeur : int ou float
                Nombre à formater.

            Retour
            ------
            str
                Nombre formaté avec préfixe.
            """
            unites = ['', 'k', 'M', 'G', 'T']
            idx = 0
            n = float(valeur)
            while abs(n) >= 1000.0 and idx < len(unites) - 1:
                n /= 1000.0
                idx += 1
            if idx > 0:
                return f"{n:.2f}{unites[idx]}"
            if n == 0:
                return "0.00"
            if n < 10:
                return f"{n:.2f}"
            if n < 100:
                return f"{n:.1f}"
            return f"{n:.0f}"

        def _effacer_ligne(self):
            """Efface la ligne courante dans le terminal."""
            try:
                largeur = self.ncols or shutil.get_terminal_size().columns
                print(' ' * largeur, end='\r', file=self.file)
                self.file.flush()
            except Exception:
                pass

        def close(self):
            """Ferme la barre de progression.

            Si leave=True, la barre finale reste affichée.
            Si leave=False, la barre est effacée.
            """
            if not self.ferme:
                self._afficher()  # affiche l'état final
                if self.leave:
                    try:
                        print('', file=self.file)
                    except Exception:
                        pass
                else:
                    self._effacer_ligne()
                self.ferme = True

        def __enter__(self):
            """Entre dans le contexte 'with'."""
            self.debut = time.time()
            return self

        def __exit__(self, type_exc, valeur_exc, traceback):
            """Quitte le contexte 'with' et ferme la barre."""
            self.close()

    return _Tqdm(iterable, total, desc, leave, ncols, mininterval,
                 unit, unit_scale, file, ascii)
