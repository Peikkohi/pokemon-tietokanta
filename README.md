# Pokémon tietokanta (Pokédex?)
Työkalu Pokémonien tietojen etsimiseen. Tarkoitettu käyttötarkoitus on pokémon fanipelin "infinite fusion" pelaamiseen.

## Sovelluksen käyttöönotto
1. Lataa vaatimukset: `pip3 install -r requirements.txt`
2. On syytä myös asentaa version PostgreSQL:stä
3. Alusta tietokannan taulukot: `psql < schema.sql`
4. Käynnistä komennolla: `flask run`

Voi myös lisätä kokeiludataa: `psql < test-data.sql`

## Tietokantaan tiedon lisäämiset
- [ ] Tietokantaan voi lisätä Pokèmoneja - Laji, Tyyppi1, Tyyppi2, Kyky1, Kyky2, Vireys, Voima, Kestävyys, Mielenvoima, Mielenkestävyys, Ketteryys
  - [x] Laji
  - [x] Tyyppi1 ja tyyppi2 (mietin että tän voi erotella omaksi listaksi, koska kaikilla pokémoneilla ei oo kahta tyyppiä :S)
  - [ ] Kyvyt (sama on siis kyvyillä)
  - [ ] Loput...
- [x] Tietokantaan voi lisätä Kykyjä - Nimi, [Kuvaus]
- [ ] Tietokantaan voi lisätä Iskuja (Tyyppi, Voima, Osumisen todennäköisyys, Vaikutuksen todennäköisyys, Vaikutus)
- [ ] Tietokantaan voi lisätä Iskun vaikutuksia (Kuvaus)
- [ ] Pokémoneille voi lisätä Iskuja (Pokémon, Isku, Oppimistaso)
- [ ] Pokémoneille voi lisätä Kehittymisiä (Mistä, Mihin, Kehitystaso/-kuvaus)

## Tietokannasta tiedon hakeminen
- [ ] Pokèmoneja voi hakea predikaatin (totuuslausekkeen) suhteen
  - [x] Nimen suhteen "/search/name=<inserted-name>".
  - [ ] Muut lausekkeet (tietoalueet ja epäyhtälöt)
  - [ ] Hakemiskenttä
- [ ] Pokémonilta voi hakea kehitysmuodot
- [ ] Iskuja voi hakea predikaatin suhteen
- [ ] Hakujen tulokset voi uudelleenjärjestää ominaisuuden suhteen
