from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL = "cardiffnlp/twitter-roberta-base-hate-latest"


def download_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    tokenizer.save_pretrained("./llm_model/")
    return


def download_model():
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained("./llm_model/")
    return


def main():
    download_tokenizer()
    download_model()
    return


if __name__ == "__main__":
    main()
