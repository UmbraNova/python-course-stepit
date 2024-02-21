# pip install textblob



from textblob import TextBlob



text = "I love programming. It is the best thing ever"



blob = TextBlob(text)



print(blob.sentiment)



# polarity
# sub 0 negativ
# peste 0 pozitiv
# subiectiviate -> 0-1