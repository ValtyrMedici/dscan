from django.db import models

# Create your models here.
class Scan(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=6)

    solarSystem = models.TextField(null=True)
    data = models.TextField()

    summaryText = models.TextField(null=True)

    DSCAN = 0
    LOCALSCAN = 1
    SCAN_TYPE = (
        (DSCAN, 'dscan'),
        (LOCALSCAN, 'Local Scan'),
    )
    type = models.IntegerField(choices=SCAN_TYPE)

    raw = models.TextField(null=True)

class Corporation(models.Model):
    corpID = models.BigIntegerField()
    ticker = models.TextField()
    name = models.TextField()

class Alliance(models.Model):
    allianceID = models.BigIntegerField()
    ticker = models.TextField()
    name = models.TextField()

class InvType(models.Model):
    typeID = models.TextField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    groupID = models.TextField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    typeName = models.TextField(db_column='typeName', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invTypes'

class InvGroup(models.Model):
    groupID = models.BigIntegerField(unique=True)
    groupName = models.CharField(max_length=200)
    categoryID = models.BigIntegerField()

    capital = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'invGroups'

class Character(models.Model):
    characterID = models.BigIntegerField(unique=True)
    charName = models.CharField(max_length=200)

    corpID = models.BigIntegerField()
    corpName = models.CharField(max_length=200)

    allianceID = models.BigIntegerField(null=True)
    allianceName = models.CharField(max_length=100)