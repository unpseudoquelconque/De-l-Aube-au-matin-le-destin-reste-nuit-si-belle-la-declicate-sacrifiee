﻿# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image dirty dream = "dirty_dream.JPG"
image opening night = "opening_night.JPG"
# Déclarez les personnages utilisés dans le jeu.
define a = Character('Zar', color="#4FE849")
define b = Character('Witt', color="#99938E")
define c = Character('Goras', color="#9B1C99")
define d = Character('Leuze', color="#0A074D")
define e = Character('Rendt', color="#c8ffc8")
define f = Character('Noza', color="#AED6F1")
define g = Character('Artre')
define h = Character('Gaard')
define i = Character('Arx')
define j = Character('Stote')
define k = Character('Etszche')
define l = Character('Heid', color="#E43009")
define m = Character('Cault')
define n = Character('Deb')
define o = Character('Menide')
define p = Character('Mus')
define q = Character('Ume')
define r = Character('?', color="095BE4")
define s = Character('Lac')
define t = Character('Gels')
define u = Character('Gust')
define v = Character('Rèle')
define w = Character('Mund')
define x = Character('Obe')
define y = Character('Liclès')
define z = Character('Mac')
define aa = Character('Manu')
define ab = Character('Ran')
define ac = Character('Cio')
define ad = Character('Clite')
define ae = Character('Rousse')
define af = Character('Cartes')
define ag = Character('Cure')
define ah = Character('Russ')
define ai = Character('Scal')
define aj = Character('Ade')
define ak = Character('Proud')
define al = Character('Gale')
define am = Character('Nèque')
define an = Character('Conf')
define ao = Character('Ocke')
define ap = Character('Van')
define aq = Character('Hoegel')
define ar = Character('Schopi')
define as = Character('Slavoj Zizek')
define at = Character('Jordan Peterson')
define au = Character('Smith')

# Le jeu commence ici
label start:
    scene opening night
    r "Le saule s'élève a nouveau, touche déjà le ciel."
    r "Défait des illusions de son feuillage,"
    r "Ses branches se consumment, et bientôt seul le tronc subsiste."
    r "D'ailleurs je ne le vois plus."
    r "Sans hésiter, les racines croisent délicatement l'aurée de l'aurore."
    l "Tu penses qu'il pionce encore ?"
    e "Possible. C'est une sacrée feignasse après tout."
    l "Dans tout les cas, c'est lui qui a les clés."
    scene dirty dream
    with Dissolve(.5)
    r "On la voit lentement se fondre dans les nuages."
    e "Oh et puis merde, je défonce la porte. Ca sera à ses frais."
    l "Si tu pouvais éviter, j'ai pas particulièrement envie de finir dans le viseur du doyen."
    l "Plus qu'à espérer qu'il se reveille avant les cours."
    r "Déjà leur laine bientôt atrophiée et si vite abandonnée."
    r "Cet eternel errance cessera-t-elle un jour ?"
    # Choix 1
    r "Bientôt seul le crissement du verrous resonnent, loin du rêve."
    r "En espérant que vous pourrez bientôt profiter sa singulière majesté..."
    "Il s'y remettent ce matin ?"
    "On va les faire tourner en bourrique un peu. Presque sur qu'elle a les clés en plus."
    "La chambre est ensevelie sous une masses imposante de, ouais, de dechets."
    "Une masse dont ils sont propriétaire. Et semble determiné a récupérer apparemment."
    "Ben, pas de chance, je n'ouvrirai pas. D'ailleurs c'est la dernière porte que j'ouvre de me longue existence."
    "Muahaha, observez la déchéance des puissants. Longue vie au nouveau maitre des lieux."
    "   "
    "Bon la porte va finir par céder."
    e "Regardez moi ca. Comment vous portez vous, Maitre Gueule en bois ?"
    "Sache que je suis presque sobre."
    l "Formidable. Et nous avons cours dans... "
    l "Avions cours il y a 15 minutes."
    e "Formidable. Ou est le papier ?"
    "Sous la fenêtre."
    e "J'espère pour toi qu'il est intact, cette merde est introuvable en ville."
    "Aucune idée. *Ponk*"
    l "Ton état ne t'empêche pas de faire l'effort de parler."
    "Et pourquoi devrais je faire cette effort, puisque vous entendez littéralement tout ce qui me passe par la tête ?"
    l "Oh non, le mutant fait sa diva aujourd'hui !"
    e "Je maudis ces incroyable pouvoirs, qui par leur présence me condamne à solitude et tempérance !"
    l "Un destin si tragique ! Ô, si seulement tu pouvais faire du sommeil ton compagnon d'infortune !"
    e "Nulle alliance ne pourrait, je le crains, soutenir l'horreur du moi tempétueux ! Ô, que de souffrance ! Je ne serai bientot plus que l'ombre d'une ombre !"
    e "Commençon par faire entrer la lumière, ca t'aidera a rejoindre la réalité."
    "La lumière m'aveugle ! Mes yeux bruuuuullle !"
    e "On t'attendra au cours de Lorfelin!"
    "Parfait. Retour au dodo."
    l "Dans 30 minutes Zar. Bouge ton cul."
    "Pourquoi tant de grossièretés aujourd'hui ? Môman vous a pas appris que c'était pôs bien de jurer ?"
    "Sachez qu'il est bien possible que vous ayez interrompu une discussion avec Dieu lui même ! !"
    "Et maintenant plus rien."
    "Et ils sont déjà partis, hein ?"
    "Un petit moment seul perdu dans mes pensée. Assez rare pour être célébré."
    "Flemme d'ouvrir les yeux néanmoins."
    "    "
    "Attendez, quelle heure est il ?"
    "Je suis probablement à la bourre."
    "Non pas que ce soit grave."
    "Devrai peut etre vérifier."
    "    "
    "Reveillons nous."
    "Il pleut dehors, et personne n'entend rien dans le batiment. Le progrès est un echec."
    "Quoique ce soit a manger dans le frigo ?"
    play music "219825__mattc90__creepy-classical-vinyl-glitched.mp3" fadein 1.0
    "Va pour le yaourt."
    "Si ca se trouve, la terre EST plate. Mais du coup, comment est ce que les frontières seraient définies ? Un mur serait la solution la plus évidente, mais un mur pourrait avoir des fissures."
    "D’un autre coté, peut être que ces fissures pourraient expliquer certains aspects du changement climatique."
    "Merde, Goras est réveillé. Il faut que je me tire en vitesse."
    "Mais si la terre est plate, ou est ce que les farfadets habitent ? Il utilisent peut-être des dimensions parallèle pour se cacher … Ou peut-être sont ils assez petit pour vivre dans le sol ?"
    "Mon dieu, écouter cet abruti va me faire péter une durite."
    "Essayons d’enfiler ca aujourd’hui. Ou est mon sac ?"
    "J’espère que Hoegel va me rappeler. Le rendez vous de la semaine dernière était super. Je crois qu’elle m’aime bien. Bien sur que non. Elle est salement bonne."
    "Un. Deux. Trois. Quatre. Ciiiinq. Siiiiiix. Seeeeeeeeepppptttttt. Hui… Merde."
    "Qui c’est ca ? Qu’est ce que qui s’est passé la nuit dernière ? Réfléchie. Réfléchie. Ne panique pas."
    "Encore ce rêve. Faut juste que je dorme. Peut être contacter le psi. . Et la putain de machine est encore en panne, et on remercie la bande de sac à merde en charge de l’entretien. . Je vais lui demander sa main. . J’arrive pas à pisser."
    "Oh non ca recommence. Miam miam petit déjeuner anglais ce matin. Je sais qu’ils en ont tous après moi, ces normies avec leur masques et leur propagande progressiste. Ma mère est morte. MERDE LE COIN DE TABLE ET MA TASSE QUI TOMBE A. Une petite révision de dernière minute au cas où."
    "enfin une bonne nuit de sommeil merde il pleut encore que peut être que si le temps dépend de la rotation Hoegel vient de me bloquer quel est le numéro de téléphone maman me l’a envoyé et je ne peux même pas aller a l’enterrement il faut que je me ressaisisse sept c’est pathétique comme une fiotte."
    "..."
    stop music
    "..."
    "Faut que je déménage."
    "C'est vrai qu'il y avait cette théorie comme quoi tout les soprani du même quartier finissent par coordonner leur routines."
    "Prions que ca n'arrive jamais. Si ce truc commence a arriver chaque jours, je vais vriller"
    "Les gens savent vraiment pas conduire dans cet endroit."
    "Et il me fait un doigt."
    "Possible qu'il m'ait entendu. Pas sur."
    "Ma zone d'impact semble avoir augmenté au fil des années.  Elle faisait quoi, un mètre de rayon au collège ?"
    "C'était marrant de la mesurer avec Witt. Ca date ca par contre."
    "Toujours aussi éprouvante les 40 minutes de marche."
    "Je sue comme pas possible avec ce soleil d'enfer. Et dire qu'il pleuvait il y a pas une heure."
    "Pas de bus. Ca aussi c'était une sacrée catastrophe."
    "Vierzon, charmante petite ville de chauffeur ivre et d'étudiant ivre mort. Le paradis sur terre."
    "Merde, c'est question réponse aujourd'hui pour Lorfelin ! Une petite révision de dernière minute s'impose. Quoique si je me débrouille bien, je loupe sans difficulté l'interro."
    "Parions là dessus. On est a 10 minutes de retard, et il reste vingt minute de marche..."
    "En prenant en compte qu'il s'agit d'un crénau de deux heures, et qu'il essaye systématiquement, et sans succès, d'obtenir une salle remplie avant de commencer."
    "C'est du 50/50. Donc tout ce calcul était une perte de temps. Bon je suis une chanceuse, donc ca va passer."
    "Ce rêve était vraiment bizzare."
    "Faudrai que j'en parle avec le psi dont Leuze m'a filé le numéro."
    "Ah non, ca c'est pas moi. Ahahaha, tout va bien."
    "Ces \"Unité d'Habitation\" sont vraiment l'une des pire modes d'après guerre. Merde qu'elles sont moche. Non pas que les batiments Neo-Haussmanien soient des oeuvres d'art non plus."
    "Enfin vu que personne ne peut se les payer, au moins ils sont propres. De notre côté, on se retrouve bloqué avec une idée sympathique executé sur un budget café."
    "Et quand, surprise, le projet a été un échec, les entrepreneurs ont demarché les universités du coin avec des prix cassés, sur lesquelles elles ont sauté sans hésiter. Enfin vu la gueule de leurs locaux à ce moment là..."
    "Soit ce gars est d'accord avec moi, soit il pense que faire lui donne un air adorable, et dans tout les cas il faut que bosse. Je suis incapable de me concentrer, c'est infernal."
    "Il devrait couvrir le début de la guerre aujourd'hui. Essayons de retaper ca."
    "Quatrième génération d'Eugénosophie en 85E. Effondrement de l'ONU en 85F. Montée des Néo-utilitaristes de 85B à 865. Discours de Kuradrot en 86A."
    "Ultimatum de l'Oligarch en 86C. Ou 6B ?"
    "C'est déjà un début. On est en semaine 5, il risque pas de nous poser un exam vraiment pointu."
    "Le batiment principal ressemble toujours un ventilateur géant. L'heure de vérité. Après un cours passage en salle de prêt, bien évidemment."
    "Et maintenant, pour le clou du spectacle."
    a "Encore une fois c'est un honneur pour moi de chuchoter chacunes de mes pensées devant des centaines de mes pairs."
    a "Je ne saurai être plus heureux. Faites que l'ascenseur fonctionne, je vous en prie. Je trace dans le hall, je trace dans le hall."
    a "Merde, il y a Cault par là. Evitons plutôt de la croiser dans cet état. On rase le mur et on cours."
    a "Tout va bien. Tout va bien. Tout va bien. En réparation ? Très ennuyeux ça. Pauvre de moi, encore 3 étages d'enfer."
    a "Et cette satanée port qui s'ouvre pas. Pourquoi ? Faut graisser les ressorts ? Se dépecher, se dépecher."
    f "Eh mais ca serait pas le délicat petit Zara ? Je me disais bien que cette voix me disait quelque chose."
    a "Hey, comment ca va ? Ca te dirait de monter ces escaliers avec moi et continuer ce qui semble déjà être une conversation d'anthologie ?"
    f "Mais bien sur ! Tu veux que je t'ouvre la porte pendant que j'y suis ?"
    a "Avec Joie Merci."
    f "Et du coup comment vas tu ? Comment avance ta candidature de libre-penseur ?"
    a "Eh bien ca n'avance pas vraiment. Enfin il me reste encore pas mal de temps donc tout va bien. Et toi, comment va ? On raconte que vous avez bien matché avec Leuze ? Aventureuse, m'a t on dit."
    f "Effectivement, \"Aventureuse\" c'est le mot. Enfin je suis pas la vierge marie non plus, donc on y gagne tout les deux au change. Sinon, mes recherches théoriques avancent sans difficultés, donc le moral est bon. "
    a "Tu es diplomé dans pas longtemps en plus, nan ? Tu penses être bien classé ?"
    f "C'est un sujet que j'essay d'éviter en ce moment, on pourra en reparler a l'occasion. C'est pas complètement la merde, mais mes notes sont pas en hausse on va dire."
    f "Donc la pression monte, et il s'avère que vivre avec quelqu'un est plus prenant que ce que je pensais, et je suis un poil en dépression en ce moment..."
    a "Tu trouveras bien quelque chose. Faut que je te laisse pour aller récuperer mon équipement, enfin on peut se rattraper à l'occasion. Tu m'expliquera a ce moment là."
    f "Il y a pas grand chose à dire, mais pourquoi pas."
    a "Parfait. Je cours, je suis déjà bien en retard pour le cours de Lorfelin..."
    a "Aaaaa Pllllllluuuus"
    a "Il avait l'air bien fatigué par contre. Entre le polo qui ressemble a un mauvais assemblage d'abas jours composé par un forgeron éméché par un soir de nouvelle lune,"
    a "et le puits de 40 centimètres autour des yeux, c'était la fête à la maison. Je suis presque étonné qu'il soit en capacité de parler."
    a "Et ses cheveux aussi quel enfer. Bref. Se concentrer. Mon casier. Prendre l'absorbruit. Prendre le masque. On y va."
    a "On se détend. Ordre et Harmonie du corp et l'âme pendant au moins cinq heures. Meme pas excité. Juste content."
    a "Et c'est partie pour le 12ème étage. Fichu ascenseur."
    a "Cette marche est toujours pas réparé, hein. Quelqu'un va casser la gueule un de ces quatres."
    a ""





    return
