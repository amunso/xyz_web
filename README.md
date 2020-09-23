# xyz_web
#Webpage for XYZ factor
Som beskrevet innledningsvis er det snakk om en helt primitiv «statisk» side med mulighet for å dele inn etter innslag, hvorav innslaget enten er en YT/Vimeo embed, et bilde eller en tekst.

# Oppsett
Jeg tror ikke det er hensiktsmessig at vi skal micromanage nøyaktig hvordan dette blir bygget opp. Legger ved en veldig grov mockup av hvordan det eksempelvis kan se ut – altså å smelle på litt Bootstrap og dele opp i innslag <a href="https://getbootstrap.com/docs/4.0/examples/album/">https://getbootstrap.com/docs/4.0/examples/album/</a>. Hvorvidt innslagene er samlet på grid med thumbnail og man må trykke seg inn, eller bare dukker opp kronologisk nedover, er veldig samme sak så implementer det dere foretrekker 😊 Samme gjelder Nabla navbar

# Avstemming
Det skal være mulig å kunne stemme på innslag, det er en fordel om man kan begrense til at samme bruker kun kan avgi stemme én gang (f.eks. ved bekreftelse på epost eller angi sitt NTNU-brukernavn). Jeg tenker det er rimelig å ha et litt tillitsbasert stemmesystem som ikke er altfor rigid, da det ikke er snakk om særlig vanvittige premier til vinnerne. Jeg tror det er fordelaktig at man kan stemme (1. valg, 2. valg, 3. valg) på alle innslagene, f.eks. ved å ha de tre alternativene som en input type="radio" for hvert innslag. Dette er selvfølgelig bare forslag, dere vet tross alt bedre hvordan man kan implementere slike løsninger. 
Obs: Stemmefunksjonen trenger ikke være på plass riktig ennå, da vi helst vil ha stemmegivning aktiv kun 23-25 oktober.

# Legge til innslag
Jeg ser for meg at det kan være utfordrende å ha en automatisert prosess på å legge inn innsendte innslag. Den letteste måten er kanskje å be de som sender inn innslag å sende dem som vedlegg til en epostadresse, og at en av oss linjeledere eller en i webkom legger det inn manuelt. Dere vet nok mer om hva som er mest realistisk i forhold til tidsskjemaet, så tar gjerne imot innspill her.