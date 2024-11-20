"""
Amanuensi 🖋️

In un recondito monastero, gli e e le amanuensi hanno il compito di custodire la conoscenza sottoforma di manoscritti cartacei, ricopiando a mano
noti testi letterari da varie fonti. 
Questi sono raccolti in libri organizzati per tema, che devono essere custoditi inalterati. Ma il monastero incoraggia anche a prendere spunto
dai testi, per poi modificarli e crearne di nuovi. Inoltre, è importante crearne delle copie da spedire ai monasteri di tutto il mondo, 
per quanto più diffonderne gli importanti contenuti culturali.

Creare un programma che permetta di 
- organizzare i testi all'interno di libri tematici 
- analizzare i libri per numero di manoscritti, di righe e di caratteri che contengono
- creare nuove versioni dei manoscritti, garantendo che i libri originali restino inalterati
- creare copie degli originali da mandare ad altri monasteri

"""


# Alla Sera - Foscolo
import copy


manoscritto1 = """Forse perché della fatal quiete
Tu sei l’immago a me sì cara, vieni,
O Sera! E quando ti corteggian liete
Le nubi estive e i zeffiri sereni,
E quando dal nevoso aere inquiete
Tenebre, e lunghe, all’universo meni,
Sempre scendi invocata, e le secrete
Vie del mio cor soavemente tieni.
Vagar mi fai co’ miei pensier su l’orme
Che vanno al nulla eterno; e intanto fugge
Questo reo tempo, e van con lui le torme
Delle cure, onde meco egli si strugge;
E mentre io guardo la tua pace, dorme
Quello spirto guerrier ch’entro mi rugge."""

# A Song of Opposites - Keats
manoscritto2 = """Welcome joy, and welcome sorrow,
Lethe’s weed and Hermes’ feather;
Come to-day, and come to-morrow,
I do love you both together!
I love to mark sad faces in fair weather;
And hear a merry laugh amid the thunder;
Fair and foul I love together.
Meadows sweet where flames are under,
And a giggle at a wonder;
Visage sage at pantomine;
Funeral, and steeple-chime;
Infant playing with a skull;
Morning fair, and shipwreck’d hull;
Nightshade with the woodbine kissing;
Serpents in red roses hissing;
Cleopatra regal-dress’d
With the aspic at her breast;
Dancing music, music sad,
Both together, sane and mad;
Muses bright and muses pale;
Sombre Saturn, Momus hale; –
Laugh and sigh, and laugh again;
Oh the sweetness of the pain!
Muses bright, and muses pale,
Bare your faces of the veil;
Let me see; and let me write
Of the day, and of the night –
Both together: – let me slake
All my thirst for sweet heart-ache!
Let my bower be of yew,
Interwreath’d with myrtles new;
Pines and lime-trees full in bloom,
And my couch a low grass-tomb."""

# Still I Rise - Angelou
manoscritto3 = """You may write me down in history
With your bitter, twisted lies,
You may trod me in the very dirt
But still, like dust, I'll rise.
Does my sassiness upset you?
Why are you beset with gloom?
’Cause I walk like I've got oil wells
Pumping in my living room.
Just like moons and like suns,
With the certainty of tides,
Just like hopes springing high,
Still I'll rise.
Did you want to see me broken?
Bowed head and lowered eyes?
Shoulders falling down like teardrops,
Weakened by my soulful cries?
Does my haughtiness offend you?
Don't you take it awful hard
’Cause I laugh like I've got gold mines
Diggin’ in my own backyard.
You may shoot me with your words,
You may cut me with your eyes,
You may kill me with your hatefulness,
But still, like air, I’ll rise.
Does my sexiness upset you?
Does it come as a surprise
That I dance like I've got diamonds
At the meeting of my thighs?
Out of the huts of history’s shame
I rise
Up from a past that’s rooted in pain
I rise
I'm a black ocean, leaping and wide,
Welling and swelling I bear in the tide.
Leaving behind nights of terror and fear
I rise
Into a daybreak that’s wondrously clear
I rise
Bringing the gifts that my ancestors gave,
I am the dream and the hope of the slave.
I rise
I rise
I rise."""

# Odi et amo - Catullo
manoscritto4 = """Odi et amo. Quare id faciam fortasse requiris.
Nescio, sed fieri sentio, et excrucior."""
