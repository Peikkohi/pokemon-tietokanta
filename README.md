# Pokémon tietokanta (Pokédex?)
Työkalu Pokémonien tietojen etsimiseen. Tarkoitettu käyttötarkoitus on pokémon fanipelin "infinite fusion" pelaamiseen.

## Sovelluksen käyttöönotto
1. Lataa vaatimukset: `pip3 install -r requirements.txt`
2. On syytä myös asentaa version PostgreSQL:stä
3. Lisää `.env` tiedosto johon määrittele ympäristö muuttuja `DATABASE_URL`, joka on reitti tietokantaasi
4. Alusta tietokannan taulukot: `psql -d [tietokanta] < schema.sql`
5. Käynnistä komennolla: `flask run`

Voi myös lisätä kokeiludataa: `psql -d [tietokanta] < test-data.sql`. En saata toimia tällä hetkellä, joten joutuu lisäämään arvot sovelluksessa :S

## Tietokantaan tiedon lisäämiset
- [ ] Tietokantaan voi lisätä Pokèmoneja - Laji, Tyyppi1, Tyyppi2, Kyky1, Kyky2, Vireys, Voima, Kestävyys, Mielenvoima, Mielenkestävyys, Ketteryys
  - [x] Laji
  - [x] Tyyppi1 ja tyyppi2 
  - [ ] Kyvyt 
  - [x] Tilastot
- [ ] Tietokantaan voi lisätä Kykyjä - Nimi, [Kuvaus]
- [ ] Tietokantaan voi lisätä Iskuja - Nimi, Tyyppi, Voima, Määrä, Tarkkuus, Vaikutuksen todennäköisyys, Vaikutus)
  - [x] Nimi, Tyyppi, Voima, Määrä, Tarkkuus, Vaikutus (teksti)
- [ ] Tietokantaan voi lisätä Iskun vaikutuksia (Kuvaus)
- [ ] Pokémoneille voi lisätä Iskuja (Pokémon, Isku, Oppimistaso)
- [x] Pokémoneille voi lisätä Kehittymisiä (Mistä, Mihin, Kehitystaso/-kuvaus)

## Tietokannasta tiedon hakeminen
- [x] Pokèmoneja voi hakea predikaatin (totuuslausekkeen) suhteen
- [ ] Pokémonilta voi hakea kehitysmuodot
  - [x] Pokémonin voi hakea. Myöhemmin kehitysmuoto näkyy siellä `/pokémon/[name]`
- [ ] Iskuja voi hakea predikaatin suhteen
- [ ] Hakujen tulokset voi uudelleenjärjestää ominaisuuden suhteen

## Muita kommentteja
Alkuperäisessä suunnitelmassa ei ollut taulukkoja tyypityksille ja tajusin et mulle on tärkeempi saada sen ominaisuudet (kuin esim iskut). Siihen liittyy myös tyyppien hyvyys toisiinsa, johon oon upottanut aikaa
