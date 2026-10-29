# Contenido de la demo Casa Jam Barcelona (es/ca/en/fr). Hechos de casajambarcelona.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación doble o twin','Habitación familiar','Dormitorio compartido'],'ca':['Habitació doble o twin','Habitació familiar','Dormitori compartit'],'en':['Double or twin room','Family room','Shared dorm'],'fr':['Chambre double ou twin','Chambre familiale','Dortoir partagé']}
RD={
'es':['Cama doble o dos camas, baño privado, toalla y sábanas incluidas; con vistas a la terraza privada.','De 2 a 5 personas, con baño privado; cunas gratis hasta los 2 años, trona y bañera para bebé.','Mixto o femenino, de 4 o 6 camas, con baño privado o compartido, taquilla y luz y enchufe propios.'],
'ca':['Llit doble o dos llits, bany privat, tovallola i llençols inclosos; amb vistes a la terrassa privada.','De 2 a 5 persones, amb bany privat; bressols gratis fins als 2 anys, trona i banyera per a nadons.','Mixt o femení, de 4 o 6 llits, amb bany privat o compartit, taquilla i llum i endoll propis.'],
'en':['Double bed or twin beds, private bathroom, towel and bed linen included; overlooking the private terrace.','For 2 to 5 people, with private bathroom; free cots up to 2 years old, high chair and baby bath.','Mixed or female, 4 or 6 beds, with private or shared bathroom, personal locker, light and plug.'],
'fr':['Lit double ou lits jumeaux, salle de bains privée, serviette et draps inclus ; vue sur la terrasse privée.','De 2 à 5 personnes, salle de bains privée ; lits bébé gratuits jusqu\'à 2 ans, chaise haute et baignoire bébé.','Mixte ou féminin, 4 ou 6 lits, salle de bains privée ou partagée, casier, lumière et prise individuels.']}
ART={
'hero':('hills',3101,['#e3ead9','#f1e7c8','#f4cf8c','#9fbf96','#6f9a72','#4d7550']),
'intro':('columns',3102,['#e7efe4','#f2f6ef','#b8893e','#3f5e3e','#25381f']),
'r1':('arches',3111,['#e6eee2','#c4d6bd','#86a780','#3f5e3e','#25381f']),
'r2':('hills',3112,['#e8ecd6','#f3e6c2','#f6cf8a','#a9c19e','#80a085','#587767']),
'r3':('columns',3113,['#e5ede1','#f1f5ee','#c08c40','#46664a','#2a3d2b']),
'g1':('arches',3121,['#e7eee3','#c7d8c0','#8aa984','#3f5e3e','#25381f']),
'g2':('skyline',3122,['#36513b','#e2a160','#f6d59e','#34503a','#26402c','#18291d']),
'g3':('hills',3123,['#e3ead9','#f1e7c8','#f4cf8c','#9fbf96','#6f9a72','#4d7550']),
'g4':('columns',3124,['#e6eee2','#f2f6ef','#b8893e','#3f5e3e','#25381f']),
'g5':('arches',3125,['#e5ede1','#c2d4ba','#83a47d','#3f5e3e','#25381f']),
'g6':('skyline',3126,['#2f4a39','#e48a5f','#f9d19b','#2e4838','#213628','#15231a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Casa Jam Barcelona · Albergue familiar y sostenible en el barrio de Gràcia',see_rooms='Ver habitaciones',hero_k='Barcelona · Gràcia',hero_t='Siéntete como en casa en Gràcia',hero_s='Un alojamiento pequeño, social y ecológico, con todas las habitaciones tranquilas y abiertas a su terraza privada.',
 intro_t='Slow travel en un barrio con vida',intro_p1='Casa Jam está en el Carrer de Montmany 38-42, en Gràcia. Lucia y Damià la construyeron en 2014 con materiales reciclados y ecológicos en un antiguo almacén de curtidos.',
 intro_p2='Ofrece habitaciones dobles o twin, familiares de 2 a 5 personas y dormitorios compartidos, con cocina compartida, terraza con yoga por la mañana y recepción abierta 24h/7.',
 stats=['Barrio de Gràcia','Terraza privada','Recepción 24h/7','Para familias'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Los tres tipos de habitación de Casa Jam.',
 svcs=['WiFi 600mb gratuito','A/C frío y calor','Cocina compartida','Café y té de comercio justo gratis','Consigna de equipaje gratuita','Cunas, tronas y bañeras para bebé','Aparcamiento de bicis','Parking concertado cercano'],
 loc_p='Carrer de Montmany 38-42 · 08012 Barcelona, en Gràcia, junto a la estación de metro Joanic (L4).',
 chips=['¿Qué habitaciones tiene?','¿Es para familias?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Casa Jam Barcelona · Alberg familiar i sostenible al barri de Gràcia',see_rooms='Veure habitacions',hero_k='Barcelona · Gràcia',hero_t='Sent-te com a casa a Gràcia',hero_s='Un allotjament petit, social i ecològic, amb totes les habitacions tranquil·les i obertes a la seva terrassa privada.',
 intro_t='Slow travel en un barri amb vida',intro_p1='Casa Jam és al Carrer de Montmany 38-42, a Gràcia. La Lucia i el Damià la van construir el 2014 amb materials reciclats i ecològics en un antic magatzem d\'adoberia.',
 intro_p2='Ofereix habitacions dobles o twin, familiars de 2 a 5 persones i dormitoris compartits, amb cuina compartida, terrassa amb ioga al matí i recepció oberta 24h/7.',
 stats=['Barri de Gràcia','Terrassa privada','Recepció 24h/7','Per a famílies'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Els tres tipus d\'habitació de Casa Jam.',
 svcs=['WiFi 600mb gratuït','A/C fred i calor','Cuina compartida','Cafè i te de comerç just gratis','Consigna d\'equipatge gratuïta','Bressols, trones i banyeres per a nadons','Aparcament de bicis','Pàrquing concertat a prop'],
 loc_p='Carrer de Montmany 38-42 · 08012 Barcelona, a Gràcia, al costat de l\'estació de metro Joanic (L4).',
 chips=['Quines habitacions té?','És per a famílies?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Casa Jam Barcelona · Family-friendly, sustainable hostel in the Gràcia district',see_rooms='See the rooms',hero_k='Barcelona · Gràcia',hero_t='Feel at home in Gràcia',hero_s='A small, social and ecological place to stay, with every room quiet and facing its private terrace.',
 intro_t='Slow travel in a lively neighbourhood',intro_p1='Casa Jam is at Carrer de Montmany 38-42, in Gràcia. Lucia and Damià built it in 2014 with recycled and organic materials in an old leather tanning warehouse.',
 intro_p2='It offers double or twin rooms, family rooms for 2 to 5 people and shared dorms, with a guest kitchen, a terrace with morning yoga and a reception open 24h/7.',
 stats=['Gràcia district','Private terrace','Reception 24h/7','Family-friendly'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Casa Jam\'s three room types.',
 svcs=['Free WiFi 600mb','A/C, cooling and heating','Guest kitchen','Free fair-trade coffee and tea','Free luggage storage','Baby cots, high chairs and baths','Bike parking','Partner car park nearby'],
 loc_p='Carrer de Montmany 38-42 · 08012 Barcelona, in Gràcia, next to Joanic metro station (L4).',
 chips=['What rooms does it have?','Is it good for families?','Is there parking?','How do I book?']),
'fr':dict(title='Casa Jam Barcelona · Auberge familiale et durable dans le quartier de Gràcia',see_rooms='Voir les chambres',hero_k='Barcelone · Gràcia',hero_t='Comme à la maison à Gràcia',hero_s='Un petit hébergement social et écologique, aux chambres calmes donnant toutes sur sa terrasse privée.',
 intro_t='Slow travel dans un quartier vivant',intro_p1='Casa Jam se trouve Carrer de Montmany 38-42, à Gràcia. Lucia et Damià l\'ont construite en 2014 avec des matériaux recyclés et écologiques dans un ancien entrepôt de tannerie.',
 intro_p2='Elle propose des chambres doubles ou twin, des chambres familiales de 2 à 5 personnes et des dortoirs partagés, avec cuisine commune, terrasse avec yoga le matin et réception ouverte 24h/7.',
 stats=['Quartier de Gràcia','Terrasse privée','Réception 24h/7','Pour les familles'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Les trois types de chambre de Casa Jam.',
 svcs=['WiFi 600mb gratuit','Climatisation chaud et froid','Cuisine commune','Café et thé équitables gratuits','Consigne à bagages gratuite','Lits, chaises hautes et baignoires bébé','Parking à vélos','Parking partenaire à proximité'],
 loc_p='Carrer de Montmany 38-42 · 08012 Barcelone, à Gràcia, près de la station de métro Joanic (L4).',
 chips=['Quelles chambres a-t-il ?','Est-ce adapté aux familles ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
R='https://hostels32.assd.com/crs4.php?goto=10&cust=200250&type=020&langcrs='
BOOK=dict(mode='engine',url={'es':R+'S','ca':R+'S','en':R+'E','fr':R+'F'})
D=dict(name='Casa Jam Barcelona',ac='#3f5e3e',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Carrer de Montmany 38-42 · 08012 Barcelona',phones=['+34 933 155 338'],emails=['info@casajambarcelona.com'],maps='Casa Jam Barcelona, Carrer de Montmany 38, Barcelona',t=T)
META=dict(repo='demo-hostal-jam-barcelona',name='Casa Jam Barcelona',legal_name='Jam Luda S.L. (JamLudaSL)',registry_ids=['CIF B66127366','Registro Mercantil de Barcelona, hoja B-442853','AJ000598'],
 url='https://www.casajambarcelona.com/',domain='casajambarcelona.com',municipality='Barcelona',province='Barcelona',sector='albergue familiar en Gràcia',
 read_at='2026-10-29T08:05:00+01:00',created_at='2026-10-29T08:15:00+01:00',built_at='2026-10-29T08:15:00+01:00',audit_date='2026-10-29T07:46:00+01:00',
 rating=dict(value=4.7,coincide=['telefono','web'],date='2026-10-29T06:55:53+01:00',url='https://www.google.com/maps/place/Casa+Jam+Barcelona/@41.4047637,2.0877015,13z/data=!4m13!1m2!2m1!1sJam+Barcelona!3m9!1s0x12a4a2bc2011234d:0x4c317468c0182b62!5m2!4m1!1i2!8m2!3d41.4047637!4d2.1597993!15sCg1KYW0gQmFyY2Vsb25hWg8iDWphbSBiYXJjZWxvbmGSAQZob3N0ZWyaASNDaFpEU1VoTk1HOW5TMFZKUTBGblRVTkJOamN6VUZaM0VBReABAPoBBQieAxBC!16s%2Fg%2F11b6cslqft?hl=es&entry=ttu&g_ep=EgoyMDI2MTAyMC4wIKXMDSoASAFQAw%3D%3D'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas que usa su propia web (formulario BOOK NOW de casajambarcelona.com -> hostels32.assd.com, cliente 200250); el motor no tiene catalan y se enlaza en castellano. La demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Tienen cunas para bebés?','K03'),('¿Hay parking?','K04'),('¿Es accesible para personas con discapacidad?','K05'),('¿Admiten mascotas?','K06'),('¿Dónde está?','K07'),('¿Cómo llegar desde el aeropuerto?','K08'),('¿Cómo es la terraza?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el correo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Hay desayuno?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Què tenen les habitacions?','K02'),('Teniu bressols per a nadons?','K03'),('Hi ha pàrquing?','K04'),('És accessible per a persones amb discapacitat?','K05'),('Admeteu mascotes?','K06'),('On és?','K07'),('Com arribar des de l\'aeroport?','K08'),('Com és la terrassa?','K09'),('Com reservo?','K10'),('Quin és el correu?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Hi ha esmorzar?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What do the rooms have?','K02'),('Do you have baby cots?','K03'),('Is there parking?','K04'),('Is it accessible for disabled people?','K05'),('Are pets allowed?','K06'),('Where is it?','K07'),('How to get there from the airport?','K08'),('What is the terrace like?','K09'),('How do I book?','K10'),('What is the email?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Is breakfast served?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Qu\'ont les chambres ?','K02'),('Avez-vous des lits bébé ?','K03'),('Y a-t-il un parking ?','K04'),('Est-ce accessible aux personnes handicapées ?','K05'),('Les animaux sont-ils admis ?','K06'),('Où est-ce ?','K07'),('Comment venir depuis l\'aéroport ?','K08'),('Comment est la terrasse ?','K09'),('Comment réserver ?','K10'),('Quel est l\'e-mail ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Le petit-déjeuner est-il servi ?',None),('Y a-t-il une piscine ?',None)]}
