from django.shortcuts import render
from django.views import View
from . import models

class ApplyView(View):

    def get(self, request):

        return render(request, 'apply/apply.html')

    def post(self, request):

        new_person = None
        request_dict = request.POST.dict()

        if request_dict['participant-category'].strip() == 'Art':

            new_person = models.Art(name=request_dict['participant-name'], 
            address=request_dict['participant-address'],
            school_grade=request_dict['participant-grade'],
            phone=request_dict['participant-phone'],
            email=request_dict['participant-mail'],
            date_of_birth=request_dict['participant-birth'],
            contact_person=request_dict['contact-type'],
            parent_name=request_dict['contact-name'],
            parent_phone=request_dict['contact-phone'],
            parent_email=request_dict['contact-mail'])

        elif request_dict['participant-category'].strip() == 'Sport':

            new_person = models.Sport(name=request_dict['participant-name'], 
            address=request_dict['participant-address'],
            school_grade=request_dict['participant-grade'],
            phone=request_dict['participant-phone'],
            email=request_dict['participant-mail'],
            date_of_birth=request_dict['participant-birth'],
            contact_person=request_dict['contact-type'],
            parent_name=request_dict['contact-name'],
            parent_phone=request_dict['contact-phone'],
            parent_email=request_dict['contact-mail'])
            print('K'*100)

        elif request_dict['participant-category'].strip() == 'Science':

            new_person = models.Science(name=request_dict['participant-name'], 
            address=request_dict['participant-address'],
            school_grade=request_dict['participant-grade'],
            phone=request_dict['participant-phone'],
            email=request_dict['participant-mail'],
            date_of_birth=request_dict['participant-birth'],
            contact_person=request_dict['contact-type'],
            parent_name=request_dict['contact-name'],
            parent_phone=request_dict['contact-phone'],
            parent_email=request_dict['contact-mail'])
        
        new_person.save()
        
        if 'worldwide-prize' in request_dict.keys():

            new_prize = models.Prize(type_of_contest="Worldwide",
                number_of_countries=request_dict['worldwide-countries'],
                date_of_the_contest=request_dict['worldwide-date'],
                place_of_the_contest=request_dict['worldwide-place'],
                kind_of_the_prize=request_dict['worldwide-prize'],
                number_of_participants=request_dict['worldwide-participants'])
            new_prize.save()

            for f in request.FILES.getlist('download-worldwide'):

                new_file = models.Files(filename=f.name, docs=f, prize=new_prize)
                new_file.save()

            new_person.prize.add(new_prize)

        if 'european-prize' in request_dict.keys():

            new_prize = models.Prize(type_of_contest="European",
                number_of_countries=request_dict['european-countries'],
                date_of_the_contest=request_dict['european-date'],
                place_of_the_contest=request_dict['european-place'],
                kind_of_the_prize=request_dict['european-prize'],
                number_of_participants=request_dict['european-participants'])
            new_prize.save()

            for f in request.FILES.getlist('download-european'):

                new_file = models.Files(filename=f.name, docs=f, prize=new_prize)
                new_file.save()

            new_person.prize.add(new_prize)

        if 'national-prize' in request_dict.keys():
            
            new_prize = models.Prize(type_of_contest="National",
                date_of_the_contest=request_dict['national-date'],
                place_of_the_contest=request_dict['national-place'],
                kind_of_the_prize=request_dict['national-prize'],
                number_of_participants=request_dict['national-participants'])
            new_prize.save()

            for f in request.FILES.getlist('download-national'):

                new_file = models.Files(filename=f.name, docs=f, prize=new_prize)
                new_file.save()

            new_person.prize.add(new_prize)

        return render(request, 'apply/success.html')