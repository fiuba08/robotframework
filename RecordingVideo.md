# Screen cast instructions #

## Tools ##
  * RecordMyDesktop
  * Pitivi Video Editor (+ mahdolliset codecit)
  * Sound Recorder
  * Joku piirtelysofta (kalvo-osiot)
  * Jos haluat nähdä oman naamasi niin sen kuvaamiseen voi käyttää esim. Cheesyä tai todella hifistellen voi tietty tehdä ihan oikeella kameralla (tai kännyl).

## Presentation ##
Esityksen voi ja kannattaa koostaa paloissa

  * Kannattaa laittaa screenresot sopivaks esim 740p kuvalle (1280×720), jolloin lopullinen reso
vastaa alkuperäistä (ei tuu turhia virheitä sen takia)
  * Fontit konsoleissa isoks
  * Ajat käyttiksestä piiloon (et halua näyttää et teit tämän kello 4 aikaan yöllä)
  * Selaimesta kaikki historiat ja kakut ja autokompletet pois (autocomplete jollain
mielenkiintoisilla personoiduilla vaihtoehdoilla ei oo se mitä haluut näyttää)
  * Selaimesta kaikki turhat palkit pois
  * Neutraali taustakuva ja kaikki työkalut defaulteilla (ei haluta että käyttäjä ajautuu
konffaamaan omia asetuksia kun ei näytä samalta kuin sulla)
  * Yhdessä blogissa suositeltiin lisäämään recordausta varten oma käyttäjä jolloin
asetukset on aina oikein

Musta on hyvä idea tehdä käsis.

Äänet ja kaiken muunkin voi tehdä jälkikäteen, joten puhu esityksen aikana kuten haluut.
Jos huomaat virheen jota haluat editoida videossa niin voit vaikka huutaa siinä kohtaan,
jotta muistat editoida sen kohdan myöhemmin.

Itse tein lopullisen puheen vastan kun kuvat oli valmiit ja sit tein taas ja taas ja taas.

## Editointi Pitivillä ##
Editori ei tee mitään alkuperäisille aineistoille, joten älä hätäile.
Tähän löytyy netistä aika paljon ohjeita.
Videoitan ja audioraitoja voi liimailla, leikkailla ja drag'n'droppailla haluamallaan
tavallaan (voin näyttää livenä).
Feidaukset on triviaaleja (googleta).
Yksittäisestä kuvasta saa helposti kalvon jonka päälle puhua tuomalla sen esitykseen.
Samoin videoita on helppo yhdistellä samaan aikaan esitettäviksi.

## Rendaus ##
Youtubeen seuraavat asetukset tuotti hyvää tulosta:

Video reso: 740p

Container: FLV muxer [flvmux](flvmux.md)

Audio: FFmpeg ADPCM Shockwave Flash encoder [ffenc\_adpcm\_swf](ffenc_adpcm_swf.md)

Video: FFmpeg Flash Video (FLV) encoder [ffenc\_flv](ffenc_flv.md)

Tuottivat myös ihan helkutin ison tiedoston (2.5 minuuttia --> 200 megaa WAT???).. Vois
vielä selvitellä et saisko lähemmäs sitä formaattia mitä youtube tukee.