from django.shortcuts import render

def count_word_text(request):
    if request.method == 'GET' and 'text' in request.GET:
        input_text = request.GET['text']
        if input_text:
            len_res = input_text.split()
            word_count = len(len_res)
        else:
            word_count = 0
    else:
        word_count = 0

    return render(request, 'counter/home.html', {'len': word_count})
    
