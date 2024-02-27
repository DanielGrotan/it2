import os

import pandas as pd

MAPPE_STI = os.path.dirname(os.path.abspath(__file__))


def hent_absolutt_sti(relativ_sti: str) -> str:
    """
    Returnerer den absolutte stien ved å kombinere den gitte relative stien med MAPPE_STI.

    Args:
        relativ_sti (str): Den relative stien som skal kombineres med MAPPE_STI.

    Returns:
        str: Den absolutte stien som er oppnådd ved å kombinere MAPPE_STI og relativ_sti.
    """
    return os.path.join(MAPPE_STI, relativ_sti)


def last_inn_datasett(filnavn: str) -> pd.DataFrame:
    """
    Laster inn et datasett fra en CSV-fil.

    Args:
        filnavn (str): Stien til CSV-filen.

    Returns:
        pd.DataFrame: Det innlastede datasettet som en pandas DataFrame.
    """
    return pd.read_csv(hent_absolutt_sti(filnavn))


def prosesser_data(df: pd.DataFrame) -> None:
    """
    Prosesserer den gitte DataFrame for å beregne og skrive ut gjennomsnittlig vurdering og gjennomsnittlig installasjoner
    for de tre øverste kategoriene basert på antall apper.

    Args:
        df (pd.DataFrame): Den inndata DataFrame som inneholder appdataen.

    Returns:
        None
    """
    # Fjern dupliserte rader basert på kolonnen "App"
    df.drop_duplicates(subset="App", inplace=True)

    # Beregn antall apper i hver kategori og få de tre øverste kategoriene
    kategori_tellinger = df["Category"].value_counts().head(3)
    print(kategori_tellinger)

    # Filtrer DataFrame for å inkludere bare appene fra de tre øverste kategoriene
    df_topp_tre_kategorier = df[df["Category"].isin(kategori_tellinger.index)].copy()

    # Beregn gjennomsnittlig vurdering for hver kategori
    gjennomsnittlig_vurdering = df_topp_tre_kategorier.groupby("Category")[
        "Rating"
    ].mean()

    # Rens kolonnen "Installs" ved å fjerne "+" og ","
    df_topp_tre_kategorier["Installs"] = df_topp_tre_kategorier["Installs"].apply(
        lambda x: int(x.replace("+", "").replace(",", ""))
    )

    # Beregn gjennomsnittlig installasjoner for hver kategori
    gjennomsnittlig_installasjoner = df_topp_tre_kategorier.groupby("Category")[
        "Installs"
    ].mean()

    # Gå gjennom de tre øverste kategoriene og skriv ut gjennomsnittlig vurdering og gjennomsnittlig installasjoner
    for kategori in kategori_tellinger.index:
        print("\n")
        print(
            f"Kategori: {kategori}, Gjennomsnittlig Vurdering: {gjennomsnittlig_vurdering[kategori]:.2f}, Gjennomsnittlig Installasjoner: {gjennomsnittlig_installasjoner[kategori]:.2f}"
        )

        # Filtrer DataFrame for å inkludere bare appene fra gjeldende kategori
        kategori_df = df_topp_tre_kategorier[
            df_topp_tre_kategorier["Category"] == kategori
        ]

        # Få de tre øverste appene med flest installasjoner i gjeldende kategori
        topp_tre_apper = kategori_df.nlargest(3, "Installs")

        # Skriv ut de tre øverste appene i gjeldende kategori
        print(f"De tre øverste appene i kategorien {kategori}:")
        for _, rad in topp_tre_apper.iterrows():
            app_navn = rad["App"]
            installasjoner = rad["Installs"]
            print(f"App: {app_navn}, Installasjoner: {installasjoner}")


def hoved() -> None:
    """
    Programmet sitt startpunkt.

    Laster inn datasettet fra den angitte filstien og prosesserer dataene.
    """
    df = last_inn_datasett("data/googleplaystore.csv")
    prosesser_data(df)


if __name__ == "__main__":
    hoved()
