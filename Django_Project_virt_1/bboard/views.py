from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from bboard.models import Bb


# def index(request):
# 		return HttpResponse("Здесь будет текст.")

# def index(request): # 41
# 	s = 'Список объявлений\r\n\r\n\r\n'
# 	for bb in Bb.objects.order_by('-published'):
# 		s += bb.title + '\r\n' + bb.content + '\r\n'
# 	return HttpResponse(s, content_type='text/plain; charset=utf-8')


# def index(request): # 43
# 	template = loader.get_template('bboard/index.html') # загружаем шаблон
# 														# с помощью функции get_template
# 	bbs = Bb.objects.order_by('-published') #
# 	context = {'bbs': bbs} # контекст - в виде словаря Питона
# 							# элемент bbs будет преобразован в переменную bbs
# 	return HttpResponse(template.render(context, request)) #
# 															# выполняем рендеринг шаблона

# def index(request): # 45
# 	bbs = Bb.objects.order_by('-published')
# 	return render(request, 'bboard/index.html', {'bbs': bbs}) # с функцией сокращения render


def index(request): #  стр. 51
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})

