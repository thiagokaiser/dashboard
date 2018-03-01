from .models import Mensagem

def base_html(request):
	#import pdb; pdb.set_trace()
	args = {}
	
	if request.user.username != '':	
		num_msgs = Mensagem.objects.filter(lida=False).filter(destinatario=request.user).count()
		msgs = Mensagem.objects.filter(destinatario=request.user).order_by('-dt_mensagem') [:5]
		args = {'num_msgs': num_msgs,
				'msgs': msgs}
				
	return args