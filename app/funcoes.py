from .models import Mensagem

def header_base(request):
	num_msgs = Mensagem.objects.filter(lida=False).filter(user=request.user).count()
	msgs = Mensagem.objects.filter(user=request.user)[:5]
	args = {'num_msgs': num_msgs,
			'msgs': msgs}
	return args