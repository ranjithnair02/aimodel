from transformers import BertTokenizer, BertForSequenceClassification
from transformers import TextClassificationPipeline

def getresult():
	tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
	model = BertForSequenceClassification.from_pretrained(".")

	pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True)
	txt=input("Enter the text to classify")
	results=pipe(txt)
	return results