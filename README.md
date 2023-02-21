# Pokémon tietokanta (Pokédex?)
Työkalu Pokémonien tietojen etsimiseen. Tarkoitettu käyttötarkoitus on pokémon fanipelin "infinite fusion" pelaamiseen.

Olen muuttanut sovelluksen rakennetta. Sovellus ei tule sisältämään iskuja, niiden oppimista ja kykyjä, mutta tilalle taulut tyypitykset, niiden teho toisiinsa ja mitkä tyypit pokemonilla on. Tämä pitää taulujen määrä kurssin halutussa viidessä (jos muistan ohjeet oikein) ja on ominaisuudet, jotka itse haluan sovellukselta.

## Sovelluksen käyttöönotto
1. Lataa vaatimukset: `pip3 install -r requirements.txt`
2. On syytä myös asentaa version PostgreSQL:stä
3. Lisää `.env` tiedosto johon määrittele ympäristö muuttuja `DATABASE_URL`, joka on reitti tietokantaasi
4. Alusta tietokannan taulukot: `psql -d [tietokanta] < schema.sql`
5. Käynnistä komennolla: `flask run`

Voi myös lisätä kokeiludataa: `psql -d [tietokanta] < test-data.sql`.

## Tietokantaan tiedon lisäämiset
- [x] Tietokantaan voi lisätä Pokèmoneja - Laji, Vireys, Voima, Kestävyys, Mielenvoima, Mielenkestävyys, Ketteryys
- [x] Pokémoneille voi lisätä Kehittymisiä - Mistä, Mihin, Kehitystaso
- [x] Pokémoneille voi lisätä yhdestä kahteen tyypitystä
- [x] Tietokantaan voi lisätä Tyypityksiä - Nimi
- [x] Tietokantaan voi lisätä tyypitysten vaikutukset toisiinsa - Hyökkääjä, Puolustaja, Vaikutuksen teho (Onko hyvä? -> muuten huono)

## Tietokannasta tiedon hakeminen
- [x] Pokèmoneja voi hakea predikaatin (totuuslausekkeen) suhteen - Tällä hetkellä toimii lisäämällä sql kyselyyn `where` kohtaan juttuja
- [x] Voi katsoa pokémonin heikkoudet eli tyypit joille pokémon on heikko.
- [x] Voi katsoa pokémonin kehitykset
- [x] Taulukko, jossa näkyy kaikkien tyyppien vaikutukset toisiinsa.

## Tulevaisuuden lisäyksiä
- [x] Tietokantaan voi lisätä Iskuja - Nimi, Tyyppi, Voima, Määrä, Tarkkuus, Vaikutus (teksti)
- [ ] Hakujen tulokset voi uudelleenjärjestää ominaisuuden suhteen

