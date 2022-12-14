from pelitehdas import Pelitehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if not vastaus.endswith(("a", "b", "c")):
            break

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        # Annetaan parametriksi vastaus-muuttujan viimeinen merkki eli joko k, p tai s
        peli = Pelitehdas.luo(vastaus[-1])
        peli.pelaa()

if __name__ == "__main__":
    main()
