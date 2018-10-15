from django.db import models

class Prize(models.Model):

    class Meta:
        verbose_name_plural = "Prize"

    type_of_contest = models.CharField(verbose_name="Type of contest", max_length=100)
    number_of_countries = models.CharField(verbose_name="Number of countries participated", max_length=100)
    number_of_participants = models.CharField(verbose_name="Number of participants", max_length=100, blank=True)
    date_of_the_contest = models.CharField(verbose_name="Date of the contest", max_length=100)
    place_of_the_contest = models.CharField(verbose_name="Place of the contest", max_length=100)
    kind_of_the_prize = models.CharField(verbose_name="Kind of the price", max_length=100)

    def __str__(self):
        return self.type_of_contest

class Files(models.Model):

    class Meta:
        verbose_name_plural = "Files"

    filename = models.CharField(verbose_name="File name", max_length=100)
    docs = models.FileField(upload_to='docs/')
    prize = models.ForeignKey('Prize', on_delete=models.CASCADE)
    def __str__(self):

        return self.filename

class Participant(models.Model):

    name = models.CharField(verbose_name="Name", max_length=100)
    address = models.CharField(verbose_name="Address", max_length=200)
    school_grade = models.CharField(verbose_name="School and grade", max_length=200)
    phone = models.CharField(verbose_name="Phone", max_length=100)
    email = models.CharField(verbose_name="E-mail", max_length=100)
    date_of_birth = models.CharField(verbose_name="Date of birth", max_length=100)
    contact_person = models.CharField(verbose_name="Contact person", max_length=100)
    parent_name = models.CharField(verbose_name="Name of coach/parent", max_length=100)
    parent_phone = models.CharField(verbose_name="Phone of coach/parent", max_length=100)
    parent_email = models.CharField(verbose_name="E-mail of coach/parent", max_length=100)
    prize = models.ManyToManyField('Prize')

    def __str__(self):
        return self.name
    

class Sport(Participant):

    class Meta:
        verbose_name_plural = "Sport"

class Science(Participant):

    class Meta:
        verbose_name_plural = "Science"

class Art(Participant):
    
    class Meta:
        verbose_name_plural = "Art"

