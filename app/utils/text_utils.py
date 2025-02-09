from transformers import pipeline, LayoutLMForSequenceClassification, LayoutLMTokenizer # type: ignore

# Initialisation des pipelines Hugging Face
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", )
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Initialisation du pipeline de classification avec LayoutLM
tokenizer = LayoutLMTokenizer.from_pretrained("microsoft/layoutlm-base-uncased")
model = LayoutLMForSequenceClassification.from_pretrained("microsoft/layoutlm-base-uncased")
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def anonymize(text):
    entities = ner_pipeline(text)
    for entity in entities:
        text = text.replace(entity['word'], f"[{entity['entity_group']}]")
    return text

def label(text):
    return classifier(text)[0]['label']

def summarize(text):
    return summarizer(text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']

""" def describe(text):
    return "Description générale du document."
 """