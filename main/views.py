from django.shortcuts import render
from .models import Table
from .forms import SendEmail
from django.core.mail import send_mail
import datetime

count = 0
table_number = 0
reservation_date_choice = ''
# Create your views here.
def home(response):
	global count, table_number, reservation_date_choice
	table_list = Table.objects.all()
	table_numbers_list = []
	for item in table_list:
		table_numbers_list.append(item.number)
	
	if response.method == "POST":
		key = list(response.POST.keys())

		if response.POST.get("CurDay") == "clicked":
			now = datetime.datetime.now()
			reservation_date_choice = now.strftime("%Y-%m-%d")
			count = 0

		elif response.POST.get("PrevDay") == "clicked":
			now = datetime.datetime.now() - datetime.timedelta(days=1)
			reservation_date_choice = now.strftime("%Y-%m-%d")
			count = 0

		elif response.POST.get("NextDay") == "clicked":
			now = datetime.datetime.now() + datetime.timedelta(days=1)
			reservation_date_choice = now.strftime("%Y-%m-%d")
			count = 0

		elif response.POST.get("Ok") == "Ok":
			reservation_date_choice = response.POST.get('reservation date')
			count = 0


		elif response.POST.get("reserve") == "reserved":
			table_list[table_number-1].reserved = True
			if reservation_date_choice != '':
				table_list[table_number-1].date_reserved = reservation_date_choice
			else:
				now = datetime.datetime.now()
				reservation_date_choice = datetime.datetime.now().strftime("%Y-%m-%d")
				table_list[table_number-1].date_reserved = now.strftime("%Y-%m-%d")

			table_list[table_number-1].save()
			send_mail('Table reservation','Dear '+ response.POST.get("name") + '\nYou have reserved a table for ' + reservation_date_choice, 'tableReservationService@localhost.com', [response.POST.get("email")], fail_silently=False)
		
		elif response.POST.get(key[1]) == "clicked":
		# if key_table in table_numbers_list:
			count +=1
			table_number = int(key[1])
			if count % 2 == 0:
				count = 0
				return render(response, "main/home.html", {"table_list":table_list, "selected": False, "id":table_number})
			else:
				form = SendEmail(response.POST)
				return render(response, "main/home.html", {"table_list":table_list, "selected": True, "id":table_number,"form":form})

	
	return render(response, "main/home.html", {"table_list":table_list})
