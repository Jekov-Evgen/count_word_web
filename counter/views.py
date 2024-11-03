from django.shortcuts import render
from textblob import TextBlob

def analysis(text : str):
    al = TextBlob(text)
    result =  al.sentiment
    
    if result[0] < -0.5:
        return 'Очень негативный текст'
    elif result[0] <= 0 and result[0] >= -0.5:
        return 'Негативный текст'
    elif result[0] >= 0 and result[0] <= 0.5:
        return 'Нейтральный текст'
    elif result[0] > 0.5 and result[0] <= 0.8:
        return 'Позитивный текст'
    elif result[0] > 0.8:
        return 'Очень позитивный текст'

def count_word_text(request):
    if request.method == 'GET' and 'text' in request.GET:
        input_text = request.GET['text']
        if input_text:
            len_res = input_text.split()
            len_offer = input_text.split('.')
            len_symbol = [i for i in range(len(input_text)) if input_text[i] != ' ']
            
            word_count = len(len_res)
            offer = len(len_offer)
            symbol = len(len_symbol)
            mood = analysis(input_text)
            
            if ' ' in len_offer:
                offer -= 1
        else:
            word_count = 0
            offer = 0
            symbol = 0
            mood = '-'
    else:
        word_count = 0
        offer = 0
        symbol = 0
        mood = '-'

    return render(request, 'counter/home.html', {'len': word_count, 'off' : offer - 1, 's' : symbol, "ml" : mood})
    
