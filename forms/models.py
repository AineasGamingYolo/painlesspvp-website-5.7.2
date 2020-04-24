from django.db import models
#from django.forms import ModelForm
'''
RANKS = [
    ('Helper'),
    ('Moderator'),
    ('Builder'),
    ('Developer'),
]

MATURITY = [
	('1'),
	('2'),
	('3'),
	('4'),
	('5'),
	('6'),
    ('7'),
    ('8'),
    ('9'),
    ('10'),
]

class ApplyForStaff(models.Model):
    name = models.CharField(max_length=50)
    maturity = models.CharField(choices=MATURITY)
    age = models.IntegerField(blank=True, null=True)
    staff = models.CharField(choices=RANKS)
    reason = models.CharField(min_length=50, max_length=1000)
'''