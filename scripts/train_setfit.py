import spacy
import typer
from setfit import SetFitClassifier


def main(base_model: str, model_name: str, data: str, data_iter: int = 5):
    nlp = spacy.blank("en")
    doc_bin = spacy.tokens.DocBin().from_disk(data)
    data = [(doc.text, doc.cats["POSITIVE"]) for doc in doc_bin.get_docs(nlp.vocab)]
    docs, labels = zip(*data)
    clf = SetFitClassifier(base_model)
    clf.fit(docs, labels, data_iter=data_iter)
    clf.save(model_name)


if __name__ == "__main__":
    typer.run(main)
