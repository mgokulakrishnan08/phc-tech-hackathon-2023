from django.db import models

# Create your models here.


class PHC(models.Model):
    phc_id = models.CharField(primary_key=True,max_length=50)
    phc_name = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=500, null=True)
    password = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    mobile = models.IntegerField()
    no_of_beds = models.IntegerField()
    gmap_link = models.CharField(max_length=100, null=True)


class medician(models.Model):
    medician_id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()


class designation(models.Model):
    phc_id = models.ForeignKey(PHC, on_delete=models.CASCADE)
    medician_id = models.ForeignKey(medician, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)


class admission(models.Model):
    admission_no = models.IntegerField()
    phc_id = models.ForeignKey(PHC, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    cause = models.CharField(max_length=50)
    admission_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    discharge_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    discharge_status = models.CharField(max_length=50)
    report = models.FileField(upload_to="pdf")


class immunisation(models.Model):
    phc_id = models.ForeignKey(PHC, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=50)
    vaccine_name = models.CharField(max_length=50)
    no_of_vaccines = models.IntegerField()
