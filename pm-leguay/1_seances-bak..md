Cours d\'électrocinétique. FAS. 2021-2022

16 séances de 2h. Soit environ 6 séances sur les 2 premiers chapitres, 4
pour le transitoire, 6 pour l\'alternatif et les filtres.

Fil rouge : l\'échange d\'énergie. Il faut vraiment centrer le cours
dessus : presque à chaque exercice calculer l\'énergie et commenter son
signe.

Séances 1 Introduire l\'intérêt de l\'élec, poser les concepts de
caractéristique, point de fonctionnement. Je vais vite, mais fais du
soutien pour les étudiants qui ont des lacunes.

Séance nécessairement un peu théorique mais reste assez concrète quand
on l\'organise autour du concept d\'énergie.

\* Photo 01 de Robert Forstemann, champion de vitesse de cyclisme. De
quoi on va parler ?

\* Vidéo cycliste et grille pain (à partir de 45\')

https://www.youtube.com/watch?time_continue=1&v=S4O5voOCqAQ&feature=emb_title

Notre niveau de vie (et de confort) repose sur le fait d\'utiliser de
grandes quantités d\'énergie facilement. C\'est impossible à produire
avec ses muscles.

\* Photo 03 du mixEnergetiqueFrance : Quelles sont les sources
d\'énergie, on voit qu\'environ la moitié nécessite du transport -\>
électricité. Gros avantage de l\'électricité : transport facile de
l\'énergie. On produit à un endroit, on utilise à un autre. Bref l\'élec
est une solution technique indispensable à nos sociétés, donc un
ingénieur doit la maîtriser.

\* Puissance et énergie : on rappelle P = dE/dt, bien définir les
termes. Ou E = int P dt. Watt, kWh. QQ exemples (plaque élec 2kW,
chargeur téléphone 10 W, Robert le champion de cyclisme à fond : 700 W)

Thème 3 : Electrocinétique

**Chap 1. L\'élec en régime continu** (les renvoyer vers chap 1 et 2 du
poly, les encourager à faire les applications qui sont corrigées.
Expliquer que je ne suis pas exactement l\'ordre et que je vais un peu
vite sur certains points mais que globalement on suit tout\...)

1\. Les grandeurs de l\'électricité

En électricité la puissance (rapidité d\'échange d\'énergie) peut
toujours être calculée par la relation

P = u \* i. *A quoi correspondent ces grandeurs ?*

a\. L\'intensité du courant :

\* Quantifie le courant qui traverse un fil électrique, c\'est à dire le
mouvement d\'ensemble des charges dans un fil électrique \[schéma avec i
en rouge(on gardera le code couleur)\]. Par convention, dans le sens des
charges + (Donc opposé au déplacement des e-, on le note pour ne plus y
penser).

\* Mesure ? On rentre dans le fil pour compter le nombre de charges qui
passent par unité de temps i = dq/dt. On choisit dans quel sens on
compte ces charges, donc on met une flèche. C\'est unr grandeur
algébrique : si I>0, les charges s\'écoulent. Si I\<0, elles remontent.

\* Unité Ampère, appareil Ampèremètre, qui se branche en série dans un
circuit (cad on \"coupe le fil\"). Schéma avec A et COM (cf p 8)

\* on parle donc de courant \"à travers\", \"circulant dans\"\...

b\. La tension

\* Analogie rivière : le même courant en plaine ou en montagne ne fait
pas la même rivière. Donc on a besoin de savoir comment varie la
hauteur. En élec, on a besoin de savoir comment varie le potentiel V.
Pas abordé ici, mais dépend de la position, et donc de l\'énergie
potentielle.

\* Mesure : on compare (soustrait) le potentiel avant et après u = VA-
VB. Grandeur algébrique : le signe a un sens. Permet de prévoir le sens
du courant comme dans un fleuve. \[Schéma avec u en bleu\]

\* Unité Volt Appareil de mesure : Voltmètre, branché en dérivation (on
se place en retrait pour mesurer la hauteur de chute !). Schéma p 9

\* Vocabulaire : On parle de tension \"aux bornes de\", \"entre \... et
\...\"

2\. Caractéristique d\'un dipôle et point de fonctionnement

Leur faire citer plein de dipôles du quotidien. Définition : composant
électrique comportant 2 pôles (ou bornes ou fils).

Peut-on prévoir le fonctionnement d\'un dipôle quand le branche dans un
circuit ?

a\. Convention de signe

On peut a priori décider de compter i et u de 2 manières.

\* **Convention récepteur (R)** : dans le sens contraire.

\* **Convention géné(G) **: dans le même sens.

NB : ce choix est arbitraire, et n\'influe pas sur le \"vrai\" signe de
ces grandeurs, et on peut choisir de décrire un géné en convension R, on
aura juste soit i soit u qui sera négatif.

On constate que i qui le traverse est relié à la tension u à ses bornes.
La loi qui les relie est la **caractéristique** du dipôle.

b\. Quelques caractéristiques communes

*\[On fera toujours dans un coin un schéma du dipôle pour indiquer la
convention choisie. Toujours i en ordonnée et en rouge et u en abscisse
et en bleu\]*

-\> Fil, interrupteur fermé : u = 0

-\> interrupteur ouvert : i = 0

-\> Résisteur en convention récept: droite linéaire. On peut modéliser
un résisteur par la **loi d\'Ohm** i = k u. Ou u = R i. On apprend à
calculer k.

-\> Géné, en convention géné : droite de pente négative. On peut
modéliser un géné par la loi i = I0 -- u/r, avec I0 le **courant
électromoteur** (courant de court circuit pour les FAS)et r la
résistance interne. On peut aussi le modéliser par la loi u = E0 -- rI,
avec E0 la **fem** (Cf partie 4 de ce chapitre).

Ex : tracer les caracs d\'un résisteur et d\'un géné dans l\'autre
convention.

-\> Pour simplifier, on peut négliger la résistance interne, et on
définit deux dipôles \"parfaits\" : source idéale de tension (les fas
aiment le terme générateur idéal de tension) u = E, et source idéale de
courant i = I0.

-\> diode réelle et modélisée de 2 façons différentes pour
\"linéariser\"

Quelques définitions, donner un exemple à chaque fois parmi les
précédents :

**Passif/actif** (tension nulle à ses bornes quand le dipôle est
débranché)

**Linéaire** (caractéristique est une droite)

**Polarisé** (se comporte différamment selon le sens de branchement)

Séance 2. Suite : point de fonctionnement et zone de fonctionnement.

Ajouter une question sur l\'énergie à chaque exo

Wooclap ELECINTRO sur le parallèle avec le barrage.

c\. Point de fonctionnement d\'un circuit

Exemple avec un géné et un interrupteur ouvert.

\* Si on branche ensemble deux dipôles en série, leur tension u est
identique et le courant i qui les traverse aussi (à condition d\'être
respectivement dans les conventions différentes). i et u doivent donc
respecter leurs deux caractéristiques. Graphiquement seule
l\'intersection des 2 droites est valide. On appelle ce point le point
de fonctionnement.

Montrer qu\'on peut résoudre graphiquement ou analytiquement et qu\'on
obtient le même résultat (ici U= E)

Ex 2 puis 4 p 24. A la maison 1p39

\* Certains dipôles peuvent avoir soit un rôle de géné (donne de
l\'énergie au circuit) ou de récepteur (reçoit de l\'énergie du
circuit). On peut savoir son rôle en analysant son point de
fonctionnement

En convention R, si P= ui \>0 le dipôle reçoit de l\'énergie du circuit.
C\'est donc un récepteur.

Notion de zone de fonctionnement : Graphique 1.8 de la page 13. Si P =
ui \<0 alors il reçoit négativement du circuit. Bref il donne au
circuit.

NB : si on se place en convention géné les conclusions sont bien sûr
inversées.

Ex 3.

\
- Petit temps de correction de l\'IE

\* **Prochaine fois** : relire le cours, s\'aider du poly et savoir
faire les \"applications\" du cours. Si pb, s\'inscrire en soutien (2
séances mardi 13h, avec Mme Raffaelly et moi). Bien comprendre sinon on
va être perdus\...

Pas lundi mais prochaine fois Abdellah et Ibrahim Q+R

Récupérer les graphiques avec incertitudes

Séance 3 : Kirchhoff

\- Récupérer les graphiques avec incertitudes

\- Attention, on va vite : avez-vous relu le cours, refait les
\"applications\" du cours ? Si pb, s\'inscrire en soutien (2 séances
mardi 13h, avec Mme Raffaelly et moi). Bien comprendre sinon on va être
perdus\...

\- Prochaine fois Abdellah et Ibrahim Q+R

10 -- Wooclap/ELECDIPOLE

30 -- Exo 5p24 Diode, exo dur mais bien pour finir sur les
caractéristiques.

30 -- Cours lois de Kirchoff

50 -- exos

**3. Lois de kirchhoff.**

Comment déterminer le point de fonctionnement d\'un dipôle dans un
circuit un peu plus complexe ?

Donner un exemple de circuit complexe : circuit électrique d\'une
voiture : SIT en série avec une résistance interne, en série avec 2
lampes en dérivation.

Définir en colorant. Expliquer les définitions avec le parallèle du
barrage. Île, confluence, bras.

Noeud (intersection d\'au moins 3 fils), branche (portion de circuit
entre 2 noeuds), maille (succession de mailles commençant et finissant
au même noeud).

\* Loi des mailles : définir sur le schéma différentes tension, et
montrer que la somme est nulle

La somme des tensions d\'une maille est nulle si on suit un sens de
parcours

\* Loi des noeuds : définir sur le schéma différentes tension, et
montrer que la somme est nulle

La somme des courants entrant dans un noeud est égale à la somme des
courants sortants.

\* Bilan de puissance : si on considère le circuit comme notre système
d\'étude, à chaque instant, la puissance fournie par les générateurs est
égale à la puissance consommée par les récepteurs.

Ex 5 p 41, Ex 10p 43. Leur expliquer que dans les cas complexes, le
système d\'équations est compliqué à résoudre (et non attendu, dans la
vraie vie on donne à un ordi) mais qu\'en revanche on attend d\'eux
d\'être capable de le poser (l\'ordi ne sait pas faire ça).

Séance 4 (lundi 14 nov)

Question pour l\'an prochain : entre la méthode de Kirchhoff et la
méthode des transfigurations ça prend un temps fou. Peut-être faut-il
faire des choix. Par exemple garder kirchhoff pour des cas simples et
(juste) montrer que dans des cas complexes c\'est long. Concentrer sur
des exos concrets par exemple le 15 ou le 16 (mais à reformuler)

Graphique à récupérer

A la fin convoquer le rang du fond pour leur demander de se séparer et
de se rapprocher\... C\'est vrai aussi en algèbre, info, OMSI\...

5 p41 à faire à la maison pour ajd. Exo hyper classique à savoir sur le
bout des doigts (et pas tout de suite par coeur\...)

Méthode de résolution

-\> On fait un schéma clair

-\> On nomme les grandeurs d\'intérêt : courants et tensions en
choisissant un sens (arbitrairement, mais en respectant si possible les
conventions \"logiques\")

-\> On entoure les grandeurs qu\'on cherche (inconnues)

-\> On cherche autant d\'équations qu\'on a d\'inconnues :

- lois des mailles en chaque maille

- lois des noeuds pour tous les noeuds

- lois de chaque dipôle (Ohm pour résisteurs, U = E-RI pour source de
tension\...)

-\> On résout en essayant d\'isoler les inconnues (exigible dans les cas
simples)

Wooclap eleckir

4\. Simplification d\'un circuit (transfiguration)

Comment déterminer le point de fonctionnement d\'un dipôle dans un
circuit encore plus complexe ?

a\. Résistance équivalente de plusieurs résisteurs

Un dipôle constitué de plusieurs résistances peut être modélisé par une
résistance unique, appelée résistance équivalente

-\> Si elles sont en série : Req est la somme des résistances.\
Schéma. Démo : Loi des mailles avec les tensions qui s\'ajoutent, or I
est identique

-\> Si elles sont en dérivation : 1/Req est la somme des 1/R.

Schéma. Démo : Loi des noeuds avec les courants qui s\'ajoutent, pour U
identique

-\> Cas général : on fait par étape en isolant les R en série ou en
dérivation.

Ex 2 p 39

b\. Modèle de Thévenin et de Norton pour un générateur

\[Démo à l\'oral : Repartir de la carac, et des 2 lois U = e -- rI et I
= Icc -- u/r. Indiquer que ces 2 lois sont équivalentes et correspondent
respectivement à modèle de Thévenin et de Norton. On passe de l\'une à
l\'autre avec la même r_int est identique pour les deux, et E = r_int
I0\]

Un générateur (tracer la carac) peut être modélisé de 2 façons :

-\> Modèle de Thévenin : r en série avec SIT.

-\> Modèle de Norton : r en dériv avec SIC.

-\> Ces deux représentations sont équivalents on a donc la possibilité
de passer de l\'un à l\'autre pour simplifier les circuits (Insister sur
le côté chouette en physique : on a 2 modèles pour décrire le même
objet)

Ex 3p40

Séance 5 (vendredi 19 nov)

Séparer le rang du fond si nécessaire

Proposer un retour de la réunion de mi-semestre aux tutorés

Q + R Abdellah et Ibrahim

Finir 3 p 40 (on a fait le 1er)

\[ce matin on a fait le TP Mesures CC\] Retour sur le TP. Wooclap
elec3mesures

Prochaine fois : répondre à la question : la lampe du TP se
comporte-t-elle comme un résisteur ?

Ex 10 et 11 à la kirchhoff. Bien insister sur la stratégie de résolution
: on veut faire disparaître les variables qu\'on vient d\'introduire.
Leur expliquer que c\'est à la limite du programme\... Bien vérifier
l\'homogénéité à la fin.

Séance 6 (lundi 22 nov) Fin chap 1 et 2, début du transitoire

Q+ R ? Personne ?

NB : faire des pauses pendant les cours de ce chapitre. Les calculs sont
lourds et fatiguants pour eux qui n\'ont pas l\'habitude. Il vaut mieux
perdre 5 minutes mais regagner l\'attention de tous\...

Ralentir un peu et les rassurer : oui on est allés vite sur le premier
chapitre, on va se calmer et s\'entraîner pour consolider. Carte mentale
à faire chez soi : je veux bien les regarder.

Ex 15 (pb ouvert), trop chouette. Insister sur le bilan de puissance.

Ex 10 (et pas 11 trop long) avec Simplification (transfiguration).

J\'ai commencé la séance suivante une quinzaine de minutes.

TO DO : réviser les équa diff

Séance 7 Régime transitoire (26 nov)

Prendre avec moi un condo et une bobine visibles\...

Chap 3. Les circuits électriques en régime transitoire

Que se passe-t-il dans un circuit juste après avoir fermé
l\'interrupteur ?

1\. Le condensateur (20 min)

\* dipôle constitué de 2 armatures (conducteurs) séparées par un
isolant.

\[on en parle mais c\'est pas notre échelle d\'étude : les armatures
peuvent accumuler des charges, proportionnellement à la tension q = Cu\]

\* En régime permanent, se comporte comme un interrupteur ouvert.

\* Hors du régime permanent, on observe un courant proportionnel à la
variation du courant \[la charge varie aussi et tout se passe comme si
un courant s\'établissait\] : i = C du/dt. Capacité en Farad

\[Prendre du temps pour discuter de la variation de C dans l\'animation
suivante :

<http://www.sciences.univ-nantes.fr/sites/genevieve_tulloue/Elec/Transitoire/Condensateur.php>
\]

\* On observe que sa tension ne saute pas brutalement, mais varie
toujours de manière continue : c\'est l\'effet capacitif. Graphique
temporel. On trouve des condos dans le tube néon, les chargeurs
d\'ordi\...

2\. La bobine (10 min)

\* dipôle constitué d\'un enroulement de fils (montrer des photos)
présent dans les transfos, moteurs, chargeurs\...

\* En régime permanent, se comporte comme un fil.\
\* En dehors, on observe une tension proportionnelle à la variation du
courant u = L di/dt. Inductance en Henry.

\* De même on observe que son courant varie de manière continue, c\'est
l\'effet inductif.

**3. Exemple de circuit RC (30 min)**

On fait un exemple d\'étude détaillée en expliquant bien chaque étape et
en collant aux notations de maths des équa diffs (je leur demande de
m\'expliquer). En expliquant qu\'on posera la méthode générale juste
après. A la fin constater que la solution générale correspond au *régime
transitoire* (s\'annule aux temps longs). Et que la solution
particulière correspond au *régime forcé* par le géné, le *régime
permanent*.

**4. Méthode générale de résolution (10 min)**

a\. Faire le schéma et le paramétrer

b\. Ecrire les lois de l\'électricité (mailles, noeuds, ohm, bobine,
condo)

c\. simplifier ce système en ne gardant que les grandeurs qui sont
continues : u_c et i_bobine on obtient une équa diff

{Pour les aider à faire le lien avec les maths, préciser toujours ce qui
dépend du temps f(t)}

d\. Trouver la solution générale qui correspond au régime forcé

{en maths : (équation E~0~ sans 2nd membre) avec A(t) la primitive de
a(t)}

e\. Trouver la solution particulière du même type que le 2nd membre :
régime forcé

f\. Sommer ces 2 solutions puis déterminer la constante avec les CI.

g\. Tracer la courbe d\'évolution temporelle.

Exercice : les laisser 1h en autonomie déterminer l\'évolution du
courant dans un circuit RL. Ceux qui arrivent vite se lèvent et aident
les autres.

**Séance 8**. (29 nov) Exercices d\'application sur le régime
transitoire

Exos trouvés durs par les étudiants. Certains ont traîné et se sont
découragés, du coup ça n\'a pas beaucoup avancé. Peut être remplacer le
2 par le 1 qui évite de perdre du temps sur les transfi. Rythmer en
donnant des résultats intermédiaires régulièrement\...

\- Prévenir des kholles : EDT et programme. Demander si volontaires pour
les Q+R.

Ex 2 puis 5

**Séance 9**. (30 nov) Energie et régime transitoire : cours et exos.

Revenir à notre point de départ : P = ui\...

**5. Bilan de puissance en régime transitoire.**\
Revenons à notre exemple (tracer le schéma, paramétrer avec des couleurs
rouge géné, vert résisteur, bleu condo) \[les couleurs serviront pour le
tracé tout à l\'heure\]

On peut calculer la puissance échangée par ces dipôles

![](./ObjectReplacements/Object 3){width="6.378cm" height="1.813cm"}

On peut tracer avec un logiciel.

Ces 3 puissances sont positives : la première est la puissance gagnée
par le circuit par le géné (positive pour le circuit car en conv G), la
deuxième est la puissance perdue par le circuit par le résisteur
(positive pour l\'extérieur du circuit car en conv R), la 3ème est la
puissance perdue par le circuit par le condo (conv R). On constate que
la somme des Pgagnées est égale à la somme des Pperdues. Normal pour un
bilan de puissance.

On peut faire un schéma bilan de puissance.

6\. Transferts d\'énergie

L\'énergie correspondante vient respectivement du secteur, est dissipé
par effet Joule. Mais que devient l\'énergie perdue par le circuit dans
le condo ?

On repart de i = C du/dt, d\'où c\'est la dérivée \"exacte\" de la
fonction 1/2 Cu\^2

On en déduit que

L\'énergie échangée est donc la variation de la grandeur 1/2 Cu\^2.
Cette grandeur ressemble à l\'énergie potentielle qu\'on peut donc
stocker ou déstocker. L\'énergie est en fait stockée dans les charges
possédées par le condo. Elle pourra ensuite être déstockée.

Démontrer que la bobine aussi stocke de l\'énergie, et qu\'on peut écire
sous la forme 1/2 Li\^2.

Exercice 4.

**Séance 10** Fin du chap transitoire. Co-animation avec Laure.

TO DO prochaine fois : réviser les complexes

Ex 1 : 30 min. On présente la correction au tableau.

Pause.

Puis bascule sur l\'exo 8, après avoir vu la vidéo
<https://www.youtube.com/watch?v=kcKPvR-93Es> à partir de 20\'

Ex 8 (changer la question 2).

Interprétation énergétique : la bobine a stocké beaucoup d\'énergie dans
son courant, et on coupe bruquement le courant. Elle refuse une
variation trop brutale et maintient un courant fort -\> forte tension
aux bornes de l\'interrupteur -\> étincelle de rupture. Dangereux pour
le circuit.

Séance 11. Début sinusoidal

\- Rappel : bossez les complexes (module et argument) pour la prochaine
séance.

Q+R Baptiste + Sergen.

\- ex 2.6 : découverte de la masse (c\'est pas bien passé l\'an dernier)
?

\- Début du cours : photo Tesla Edison Parler de la controverse autour
de 1900 Tesla/Edison. Edison était un riche industriel, installe, régime
continu. Tesla un petit immigré d\'origine serbe qui a bossé à Paris et
Strasbourg avant de partir pour New York pour bosser pour Edison. Il
avait trouvé un régime chouette : faibles pertes par effet Joule et
facile pour convertir en énergie mécanique (moteur vu au S2).

\- Pour l\'an prochain : préparer une intro sexy au concept d\'impédance
: partir des représentations temporelles de u et i dans un résisteur,
dans un condo et dans une bobine : constater qu\'il y a deux modifs :
amplitude et déphasage. Besoin de réunir tout dans une seule grandeurs
(et d\'un truc plus simple que la dérivation/intégration. => Eveiller
l\'envie des complexes. Pourquoi pas partir du concept de filtre pour
faire naître l\'envie ?

Chap 4. Circuits en régime sinusoïdal

\"AC, régime sinusoïdal forcé, régime permanent\".

**1. Caractéristiques d\'un signal sinusoïsal**

1\. Rappels

Graphique temporel, on le représente par

s(t) = Sm cos (wt + phi)

avec Sm (Smax) : amplitude. wt+phi : phase. w pulsation. phi phase à
l\'origine..

Fréquence : f = w/2pi. Période T = 1/f

-\> Application : \[Schéma d\'un oscillogramme\] représenter les
grandeurs sur l\'écran.

**2. Moyenne et val. efficace :**

Moyenne nulle, valeur efficace Seff = Sm/racine(2) plus physique :
permet de caculer l\'énergie.

-\> Application : représenter le signal à la maison, f = 50 Hz et U_eff
= 230 V. (*Umax = 325V*)

3\. Déphasage entre 2 signaux

Deux signaux s1(t) et s2(t)sont synchrones s\'ils ont la même
pulsation/freq/période \[Schéma\]

On peut alors représenter le déphasage phi_2/1 = phi2 -- phi1, en
radians

déphasage \>0 : 2 en avance de phase : s2 atteint son max avant s1

déphasage \<0 : 2 en retard de phase

-\> Application : tracer s1 et s2 s3 et

s4 synchrones, d\'amplitudes 1, 2, 3, 4 (s4 est notre référence, son phi
est nul)

s1 étant en retard de phase de pi/2 rad (on parle de quadrature) par
rapport à s4.

s2 étant en retard de 0 rad (\"en phase\")

s3 en retard de pi rad (en \"opposition de phase\")

2\. La représentation complexe simplifie les calculs.

Soit un circuit série : source idéale de tension, R, L, C. On pose
ensemble les lois de kirchhoff, en remarquant que u_L = L di/dt et i = C
du_C/dt.

Résolution compliquée : on obtient une équation différentielle avec des
dérivées et des intégrales, et la source est sinusoïdale.

{Au brouillon :

-\> Idée du physicien : on va chercher chez les mathématiciens un outil
qui simplifie.

-\> Pour comparer 2 signaux, il y a 2 grandeurs qu\'on regarde :
l\'amplitude, et la phase. Ca ne vous rappelle rien ? Comment faire pour
représenter 2 infos dans un même nombre ?

s(t) = Sm cos (wt + phi) sera noté ***s***(t) = Sm e\^ i(wt + phi). Pb :
i est confondu avec l\'intensité. Pas de souci on note j.

-\> Calcul rapide de dérivée et intégrale : multiplier (et diviser) par
jw.}

Séance 12. Impédances

Wooclap ELECSIN

Q+R Baptiste + Sergen.

1\. Représentation complexe d\'un signal sinusoïdal

-\> Afin de représenter l\'amplitude et la phase d\'un signal
sinusoïdal, on utilise la notation complexe.

-\> Le nombre imaginaire i est noté j en physique pour éviter de le
confondre avec l\'intensité j²=-1

-\> au signal s(t) = Sm cos(wt+phi) on associe le signal complexe noté
(souligné)

*s*(t) = Sm e\^j(wt+phi) ou encore *s*(t) = *Sm* e\^j(wt) avec *Sm* = Sm
e\^jphi amplitude complexe.

RQ : tension et intensité étant des grandeurs réelles, on les retrouve
en calculant la partie réelle.

Application 1 p 75 (correction p 88)

2\. Impédances complexes des dipôles élémentaires idéaux

Pour chaque dipôle, on souhaite retrouver une loi analogue à la loi
d\'Ohm permettant de relier u(t) à i(t). C\'est là que la représentation
complexe est puissante : on définit pour chaque dipôle l\'impédance
complexe, la quantité *z *= *u*/*i* telle que *u* = *z i*

-\> Pour un résisteur u = R i.

En notation réelle, si i(t) = Im cos (wt) alors u(t) = Ri(t) = Rim
cos(wt).

En notation complexe, *i*(t) = Im e(jwt) alors *u*(t) = R*i*(t) = Rim
e(jwt).

Impédance du résisteur : z_res(t) = *u(t)*/*i(t)* = R => On écrit *u* =
R *i*. Elle est réelle : tension et intensité sont proportionnelles
(même phase, amplitude Um = R Im)

-\> Pour une bobine

En notation réelle, si i(t) = Im cos (wt) alors u(t) = L di/dt. Pénible

En notation complexe, *i*(t) = Im e(jwt) alors *u*(t) = Lwj *i*(t) .

Impédance de la bobine : z_bobine(t) = *u(t)*/*i(t)* = Lwj => On écrit
*u* = Lwj *i*. Elle est imaginaire pure : Par rapport au courant, la
tension est déphasée de pi/2, et son amplitude multipliée par Lw

-\> Pour un condensateur i = C du/dt.

I = C du/dt donc u(t) = 1/C \* int{i(t)}. Pénible

En notation complexe, *i*(t) = Im e(jwt) alors *u*(t) = 1/Cwj *i*(t) .

Impédance du condensateur : z_cond(t) = *u(t)*/*i(t)* = 1/Cwj ( = -j/Cw)
=> On écrit *u* = 1/Cwj *i*. Elle est imaginaire pure : Par rapport au
courant, la tension est déphasée de -pi/2, elle est donc en retard et
son amplitude divisée par Cw

3\. Impédance d\'un circuit

-\> Généralisation : impédance d\'un circuit

Si on calcule l\'impédance d\'un circuit elle s\'écrira sous la forme

z = Re(z) + j Im(z) = R + j X. En identifiant avec ce qui vient d\'être
écrit

Re(z) est la résistance équivalente du circuit

Im(z) est positif si le circuit est plutôt inductif (comme une bobine).

Im(z) est négatif si le circuit est plutôt capacitif (comme un
condensateur)

Im(z) est appelé la réactance

Application 5 : quelle est l\'impédance équivalente à deux dipôles en
série et en dérivation ?

Exercice 2 et 3 p 89 : Leq = L1L2/(L1+L2). Bof, le 3 est calculatoire et
pas passionnant

Applications 5 et 3.

**Séance 13** (juste avant les vacances, tout le monde est crevé, donc
c\'était compliqué de garder tout le monde concentré)

Info sur l\'éval à la rentrée : chapitre mesure, chapitre d\'élec
jusqu\'aux impédances et ce qu\'on fera ajd (puissance), mais pas les
filtres.

NB : organiser son tableau pour n\'avoir pas à tout réécrire mais juste
à modifier ce qui change.

**3. La puissance en régime sinusoïdal**

Comme la tension et l\'intensité dépendent du temps, la puissance dépend
du temps :

P(t) = u(t) \* i(t).

**a. Puissance pour un résisteur**

tracé sur 3 graphiques ayant le même axe horiz de i(t) sinusoïdal, u(t)
= R\*i(t) synchrone et en phase, et p(t) le produit des 2. On constate
que p(t) est périodique, mais de fréquence (donc pulsation) double, et
de moyenne non nulle (graphique p 87). La résistance va dissiper
périodiquement plus ou moins).

Mathématiquement si on pose i(t) = Im cos (wt), on a

p(t) = u(t) \* i(t) = RIm \*Im \* cos (wt)\*cos(wt).

On utilise un résultat de maths : cos(a)cos(b) = 1/2 \[cos (a+b) + cos
(a-b)\], pour obtenir que

![](./ObjectReplacements/Object 9){width="6.091cm" height="0.591cm"}On
retrouve ce qu\'on avait intuité graphiquement. On a 2 termes. Le
premier a une moyenne nulle (donc nous intéresse peu). Si on regarde sur
un temps long, on s\'intéresse à la moyenne :

P_moy = \<p(t)> = R Im\^2 /2. Qu\'on peut aussi présenter sous la forme
ressemble à ce qu\'on connaît pour le courant continu. NB : p>0 donc le
résisteur prend de l\'énergie au circuit et le donne à l\'extérieur.

**b. Puissance pour une bobine, ou un condensateur**

Tracé similaire, i est en retard de phase par rapport à u (son max est
après)

Le tracé de p(t) est toujours sinusoidal avec la fréquence double, mais
la valeur moyenne est nulle.

Mathématiquement, si on pose i(t) = Im cos (wt), on a u(t) = L di/dt =
Lw Im \* -sin (wt), qu\'on peut aussi écrire u(t) = Lw Im \* cos (wt +
phi) avec phi = pi/2. On a alors

. De nouveau le premier terme est nul et la moyenne vautqu\'on peut
présenter tout la forme . Comme phi vaut pi/2, la puissance moyenne est
nulle. En fait la bobine puise de la puissance pour stocker l\'énergie
puis la redonne (ce qu\'on peut illustrer graphiquement).

NB : on peut bien sûr retrouver le même résultat pour un condo, avec un
raisonnement similaire.

**c. Puissance pour un circuit électrique**

On peut généraliser le raisonnement à n\'importe quel dipôle : on a
toujours (on vérifie que ça marche aussi pour le résisteur), et ce quel
que soit l\'impédance. On appelle cos phi le facteur de puissance, et Z
Ieff\^2 la puissance apparente.

Ex 10

**d. Adaptation d\'impédance pour optimiser la puissance reçue**

On peut représenter l\'alimentation à la maison : un géné (EDF), une
résistance (pertes en ligne), et une impédance (tous les dipôles de la
maison)

Bilan de puissance : toute la puissance délivrée par EDF est dissipée
par soit la résistance, soit l\'impédance.

-\> Si cos phi est proche de 0 (exemple moteur). On peut calculer
l\'efficacité du transport : d\'où rien n\'est dissipé chez moi, et
toute l\'énergie est dissipée par la ligne. EDF pas content.

-\> Si cos phi est proche de 1, EDF est content. On peut calculer
l\'efficacité du transport :

EDF impose donc à ses clients ayant un facteur de puissance trop faible
de l\'augmenter, par exemple en plaçant un condo en dérivation. But :
baisser le phi pour retrouver un cos phi proche de 1.

Séance 14 (à la rentrée)

Rappel rapide sur les impédances, puis on passe aux filtres.\
On peut tracer le gain en échelle linéaire et voir qu\'on voit rien.
Puis le tracer en échelle semi-log.

**4. Les filtres**

Les filtres sont des circuits électroniques largement utilisés. Exemple
: dans les télécoms (téléphone, visio), le signal est bruité, et on veut
éviter que ce bruit. En informatique on est amené à convertir des
signaux analogiques en numériques. Encore une fois il faut se débarasser
du bruit.

La filtration (hors de l\'élec) est aussi un phénomène naturel (on
n\'entend que de 20 Hz à 20kHz), parfois c\'est une perte.

Schéma de base : ue-\> Filtre -\> us

**a. Comportement limite des bobines et condos**

Comportement aux limites BF et HF des condo et bobine

QQ exemples de filtres simples, on regarde la tension de sortie aux
limites BF et HF, on constate qu\'ils sont passe bas ou passe haut. On
peut aussi place un condo et une bobine en dérivation, la tension à leur
borne est nulle pour les 2 limites, mais pas au milieu : passe bande.

**b. Exemple du filtre RC**

Etude détaillées, fonction de transfert, diagramme de Bode. C\'est le
même filtre qu\'en TP

Travail sur du papier semi-log. Je peux utiliser inkscape pour montrer
précisément comment je trace sur le papier.

**Séance 15**. Co-animation avec Laure

Les étudiants font l\'étude détaillée d\'un filtre RL en autonomie. Puis
ex 8 (filtration d\'un signal)

\
Séance 16 Révisions

On fait un exo de puissance avec le cos phi. Puis les étudiants se
répartissent en fonction des goûts sur plusieurs exos ou sur une carte
mentale, ou sur un problème ouvert.
