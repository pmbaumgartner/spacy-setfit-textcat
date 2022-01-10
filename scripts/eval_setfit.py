import spacy
import typer
import wandb
from setfit import SetFitClassifier
from sklearn.metrics import accuracy_score

wandb.init(project="spacy-setfit-textcat", entity="peter-explosion-ai")


def main(model_name: str, data: str):
    nlp = spacy.blank("en")
    doc_bin = spacy.tokens.DocBin().from_disk(data)
    data = [(doc.text, doc.cats["POSITIVE"]) for doc in doc_bin.get_docs(nlp.vocab)]
    docs, labels = zip(*data)
    clf = SetFitClassifier.load(model_name)
    y_pred = clf.predict(docs)
    y_true = labels
    acc = accuracy_score(y_true, y_pred)
    wandb.log({"setfit/accuracy": acc})


if __name__ == "__main__":
    typer.run(main)
