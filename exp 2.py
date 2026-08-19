from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
# 1. Zero-shot prompt
zero_shot_prompt="ClassifythesentimentofthisreviewasPositiveorNegative: 'Theproductqualityis
excellent!'\nSentiment:"
#2.Few-shotprompt
few_shot_prompt="""Review: 'Ilovedthismovie,itwasfantastic.'
Sentiment:Positive
Review: 'Theservicewasslowanddisappointing.'
Sentiment:Negative
Review: 'Theproductqualityisexcellent!'
Sentiment:"""
#3.Chain-of-Thoughtprompt
cot_prompt="""Q:Ashophad15apples.Itsold6andthenreceived10more.Howmanyapplesnow?
A:Let'sthinkstepbystep.15-6=9.9+10=19.Theansweris19.
Q:Alibraryhad120books.Itlentout45andbought30newbooks.Howmanybooksnow?
A:Let'sthinkstepbystep."""
forname,pin[("Zero-shot",zero_shot_prompt),
("Few-shot",few_shot_prompt),
("Chain-of-Thought",cot_prompt)]:
out=generator(p,max_length=len(p.split())+40,num_return_sequences=1,do_sample=False)
print(f"==={name}===")
print(out[0]["generated_text"])
print()
