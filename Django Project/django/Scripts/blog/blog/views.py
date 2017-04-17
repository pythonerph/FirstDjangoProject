from django.http import HttpResponse

def home(request,id):
	return HttpResponse('id is %s' % id)      
	#返回'hey, my world!'字符串，HttpResponse方法只能返回字符串，如输入其他类型时会自动转换为字符串