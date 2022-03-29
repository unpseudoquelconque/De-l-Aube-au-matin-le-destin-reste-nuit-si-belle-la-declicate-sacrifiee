# Vous pouvez placer le script de votre jeu dans ce fichier.

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
    r "Le saule s'élève a nouveau, touche déjà le ciel."
    r "Défait des illusions de son feuillage,"
    r "Ses branches se consument, et bientôt seul le tronc subsiste."

    l "Tu penses qu'il dort encore ?"
    e "Possible. C'est une feignasse après tout."
    l "Dans tous les cas, c'est lui qui a les clés."
    scene dirty dream
    with Dissolve(.5)
    r "On le voit lentement se fondre dans les nuages."
    e "Oh et puis merde, je défonce la porte. Ca sera à ses frais."
    l "Si tu pouvais éviter, j'ai pas particulièrement envie de finir dans le viseur du doyen."
    l "Plus qu'à espérer qu'il se reveille avant les cours."
    r "Déjà leur laine bientôt atrophiée et si vite abandonnée."
    r "Cet eternel errance cessera-t-elle un jour ?"
    # Choix 1
    r "Maintenant seul le bruit des gonds branlants resonnent, loin du rêve."
    r "En espérant que vous pourrez bientôt profiter de sa singulière majesté..."
    "Il s'y remettent ce matin ? Encore une fois ? "
    "Pas envie de perdre la porte mais flemme de me lever. Presque sur qu'elle a les clés en plus."
    "Ah oui, le dossier putain. C’était à la soirée hier. Mais j’ai une de ces flemme … et un putain de mal de tête. Faut que je me lève.
    Ben, pas de chance, je n'ouvrirai pas."
    "  (crack)"
    "Elle avait pas les clés"
    "Bon la porte va finir par céder."
    e "Regardez moi ca. Comment vous portez vous, Maitre Gueule en bois ?"
    "Sache que je suis presque sobre."
    l "Formidable. Et nous avons cours dans... "
    l "Avions. Il y a 15 minutes."
    e "Formidable. Ou est le papier ?"
    "Sous la fenêtre."
    e "J'espère pour toi qu'il est intact, J’ai passé un temps fou là-dessus"
    "Aucune idée. Oupsi."
    l "être dans le cirage t’empêche pas de nous parler"
    "Je veux dire, vous entendez littéralement tout ce qui me passe par la tête ?"
    l "Oh non, le mutant fait sa diva aujourd'hui !"
    e "Je maudis ces incroyables pouvoirs, qui me condamnent à une vie de solitude !"
    l "Un destin si tragique ! Ô, si seulement tu pouvais faire du sommeil ton compagnon d'infortune !"
    e "Nulle présence ne saurait, je le crains, me préserver des horreurs qui me hantent ! Ô, quelle souffrance ! Je ne serai bientot plus que l'ombre d'une ombre !"
    e "Commençon par faire entrer la lumière, ca t'aidera à dessouler"
    "La lumière m'aveugle ! Ca bruuuuullle !"
    e "On t'attendra au cours de Nèque!"
    "Parfait. Retour au dodo."
    l "Dans 30 minutes Zar. Bouge toi"
    " C’est comme ça que vous traitez un pote dans le mal ? Je verrai si je viens…"
    "Si ça se trouve vous m’avez interrompu et je parlais avec Dieu hein"
    "Et maintenant plus rien."
    "Ils sont déjà partis, hein ?"
    "Un petit moment seul perdu avec mes pensée. Ca se fête."
    "Flemme d'ouvrir les yeux par contre."
    "    "
    "Attends, il est quelle heure ?"
    "Je suis sûrement à la bourre."
    "Enfin, ça a pas d’importance."
    " Je devrais peut être vérifier."
    "    "
    "Faut que je me réveille."
    "Il pleut dehors ; j’entends rien : merci l’isolation."
    "Y a un truc à manger dans le frigo ?"
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
    "à ce qu’il parait y a une théorie comme quoi les soprani du même quartier finissent par coordonner leur routines.C’est flippant."
    "Prions que ca n'arrive jamais. Si ce truc commence a arriver chaque jours, je vais vriller"
    "Les gens savent vraiment pas conduire ici."
    "Et il me fait un doigt."
    "Possible qu'il m'ait entendu. Pas sur."
    "Ma zone d'impact semble avoir augmenté avec le temps.  Elle faisait quoi, un mètre de rayon au collège ?"
    "C'était marrant de la mesurer avec Witt. Ca date ca par contre."
    "Toujours aussi chiant les 40 minutes de marche."
    "Je sue à mort avec ce putain de soleil. Et dire qu'il pleuvait y a pas une heure."
    "Pas de bus. C’était relou ça."
    "Vierzon, une ville des chauffeurs ivre et d'étudiant ivre mort. J’adore.."
    "Merde, c'est question réponse aujourd'hui avec Nèque ! Une petite révision de dernière minute s'impose. En vrai, si je me débrouille bien, je loupe l'interro tranquillemet."
    "Parions là dessus. Je suis à 10 minutes de retard, et il reste vingt minute de marche..."
    "Comme c’est un créneau de deux heures, et qu'il essaye toujours, et sans succès, d'obtenir une salle pleine avant de commencer."
    "C'est du 50/50. Donc tout ce calcul était une perte de temps. Bon je suis une chanceuse, donc ca va passer."
    "Ce rêve était vraiment bizarre."
    "Faudrait que j'en parle avec le psi , et que je remercie Leuze de m’avoir filé son numéro.."
    "Ah non, ca c'est pas moi. Ahahaha, tout va bien. Putain."

    "Je déteste les Unités d’habitation. Pire truc d’après guerres. Le néo-haussmanien c’est pas ouf non plus mais vu que personnne peut se le payer c’est propre.  Mais les grandes idées sans budget ça donne rarement un truc bien."
    "Soit ce gars est d'accord avec moi, soit il pense que faire semblant le rend sympa, et dans tout les cas il faut que bosse. Je suis incapable de me concentrer, c'est insupportable."
    "Ca devrait couvrir le début de la guerre aujourd'hui. Essayons de retaper ca."
    "Quatrième génération d'Eugénosophie en 85E. Effondrement de l'ONU en 85F. Montée des Néo-utilitaristes de 85B à 865. Discours de Kuradrot en 86A."
    "Ultimatum de l'Oligarch en 86C. Ou 6B ?"
    #8d0 Date de début de l'intrigue
    "C'est déjà un début. On est en semaine 5, il risque pas de mettre des questions trop pointues."
    "Le batiment principal ressemble toujours un ventilateur géant. L'heure de vérité. Après un cours passage en salle de prêt, bien évidemment."
    "Et c’est reparti…"
    a "J’adore passer pour un abruti en chuchotant en public devant toute l’université… "
    a "Encore une super journée qui commence. Faites que l'ascenseur fonctionne,. Je trace dans le hall, je trace dans le hall."
    a "Merde, il y a Cault par là. Mieux vaut éviter de la croiser dans cet état. Je rase le mur et je cours"
    a "Tout va bien. Tout va bien. Tout va bien. En réparation ? Formidable. Putain, encore 3 étages."
    a "Et la porte qui s'ouvre pas. Pourquoi ? Faut la graisser non ? Se dépecher, se dépecher."
    f "Eh mais ca serait pas le ce cher Zara ? Je me disais bien que cette voix me disait quelque chose."
    a "Hey, comment ca va ? Ca te dirait de monter ces escaliers avec moi et continuer cette incroyable conversation"
    f "Mais bien sur ! Tu veux que je t'ouvre la porte pendant que j'y suis ?"
    a "Avec Joie Merci."
    f "Et du coup comment vas tu ? Comment avance ta candidature de libre-penseur ?"
    a "Eh bien, pas vraiment. Enfin il me reste encore pas mal de temps donc tout va bien. Et toi, comment va Parait que ça se passe bien avec Leuze."
    f "Oui, je dirais que ça se passe bien. Sinon, mes recherches théoriques avancent sans difficultés, donc le moral est bon. "
    a "Tu es diplomé dans pas longtemps en plus, nan ? Tu penses être bien classé ?"
    f "J’ai pas trop envie d’en parler, on verra à l'occasion. C'est pas si ouf que ça en fait"
    f "Donc la pression monte, et puis, vivre avec quelqu'un est plus prenant que ce que je pensais, "
    a "Ca va aller t’inquiètes. Faut que je te laisse, je vais aller récuperer mon équipement, enfin on se rattrape à l'occasion. Tu m'expliquera tout ça."
    f "Il y a pas grand chose à dire, mais pourquoi pas."
    a "Super. Je cours, je suis en retard..."
    a "Aaaaa Pllllllluuuus"
    a "Elle avait l'air crevée. Elle s’est habillée dans le noir ou quoi ? ,"
    a "et les vallises qu’elle a sous les yeux… Ca m’étonne limite qu’elle vienne en cours. "
    a "Et ses cheveux aussi quel enfer. Bref. Se concentrer. Mon casier. Prendre l'absorbruit. Prendre le masque. On y va."
    a "On se détend. Ordre et Harmonie du corp et l'âme pendant au moins cinq heures. Meme pas excité. Juste content."
    a "Et c'est partie pour le 12ème étage. Putain d’ascenseur."
    a l'escaier et toujour dan un sale etat, hein. Quelqu'un va casser se la gueule un de ces quatres."
    "..."
    #Première révision
    "Putain, la porte. Reprendre son souffle. Je rentre, je suis déjà bien à la bourre."
    "Allez on rentre."
    "Nèque me voit pas. Heid et Rendt se sont foutu au dernier rang. Pratique."
    "Heid me lance un sourire narquois."
    l "On t'a gardé une place, désolé pour la porte."
    l "Comme ça on est quite ?"
    "Pas envie de débattre, j'ai toujours mal à la tête. Putain je suis peut être encore un peu bourré."
    "Un sourire crispé et c'est parti..."
    a "C'est parfait, merci."
    "C'est ça, oui. Ca va pas me rembourser la porte par contre."
    "Bon je essayer de suivre le cours, ca me changera les idées."
    "Le prof déblatère. Je sais pas combien de temps je vais tenir cette fois."
    am "Le troisième facteur aggravant nous ayant conduit à chercher l'autarcie dans les Néoasis, c'est évidemment la démultiplication des variants du virus Atra-B."
    am "Evidemment, une crise sanitaire de cette ampleur n'a fait qu'aggraver le piteux état de l'économie d'après-guerre."
    am "Rapidement, les nouvelles entités gouvernementales ont fait le choix d'une fragmentation des lieux de commandement."
    am "C'est autour de ces nouvelles bases que s'est développée la géographie du pays comme nous la connaissons aujourd'hui."
    am "D'ailleurs c'est par crainte d'une reprise des hostilités que les communications ont été suspendus entre les différents Néoasis."
    am "Même aujourd'hui, après 64 ans de paix, la menace de la guerre, si elle n'est pas tangible, reste du moins pregnante."
    am "D'autant plus que certains complotiste défendent encore aujourd'hui mordicum que l'épidémie qui a suivi en était un leg immédiat."
    am "Théories qui souvent rappelle les effets les plus étranges de certains variants, notamment sur les sopranos."
    am "Certains illuminés ont même soutenu que le virus était une forme de mal spirituel, qui s'en prenait directement à l'âme de ses victimes."
    "Même de là ou je suis, je peux voir son petit sourire."
    "Il se renfrogne immédiatement. Probablement une main levée."
    am "Mme Gaard, qu'est ce qui vous agite de si bon matin ?"
    "Bingo"
    h "Avec tout le respect que je vous dois Monsieur, c'était pour une question."
    h "Imaginons, dans une perspective tout à fait hypothétique, qu'un des variants traverse les barrières de la Néoasis"
    h "Qu'est ce que nous risquerions ?"
    #CHOIX MAJEUR : SIMP OR LIFE
    am "Eh bien, la première problématique qui se poserait serait celle de la panique moral."
    am "En effet..."
    "Elle a changé de coiffure ou quoi ?"
    "En tout cas, ca lui va bien !"
    "Content qu'elle le reprenne, je commençais à décrocher."
    "Ce nouveau corset lui va bien. J'avais pas remarqué le chapelet sur son poignet gauche, c'est un peu de trop."
    "Je devrais lui parler un jours... Ca dois quand même bien faire deux ans qu'on est en cours ensemble."
    "Putain ce prof me soûle."
    "Si j'avais un baillon sous la main."
    "Qu'est que c'était que ce bruit. Oh non. Non non non."
    "Le masque s'est éteint. Putain de batterie."
    "Putain, les gens se retournent autour. Heid, c'est dégeulasse, arrête. Taper sur le masque devrait le rallumer."
    "Gaard est étonnamment calme. Faite qu'elle ne se retourne pas. Ca marche pas, faut que je sorte."
    "Soit discret, soit discret. Marcher rapidement vers la sortie."
    "Je suis pas discret, tout le monde me regarde. Vite la porte. Penser à rien, penser à rien."
    "Trouver les toilettes. Il y en a pas à l\'étage, raser les murs, croiser personne"
    return
