from typing import Optional
import spacy
from spacy.tokens import DocBin
import typer
import pandas as pd
from wasabi import msg


def process_sst(
    sst_tsv: str, output: str, sample: Optional[int] = None, seed: int = 1234
):
    df: pd.DataFrame = pd.read_csv(sst_tsv, delimiter="\t", header=None)
    msg.good(f"Loaded Data")
    if sample:
        df = df.sample(sample, random_state=seed)
        msg.good(f"Sampled {sample}, seed {seed}")
    docs = df[df.columns[0]].tolist()
    labels = df[df.columns[1]].tolist()
    training_data = list(zip(docs, labels))

    nlp = spacy.blank("en")
    db = DocBin()
    for text, category in training_data:
        doc = nlp(text)
        positive = category == 1
        doc.cats = {"POSITIVE": 1 if positive else 0, "NEGATIVE": 0 if positive else 1}
        db.add(doc)
    db.to_disk(output)


if __name__ == "__main__":
    typer.run(process_sst)
