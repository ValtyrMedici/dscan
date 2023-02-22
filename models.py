# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Invtypes(models.Model):
    typeid = models.TextField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    groupid = models.TextField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    typename = models.TextField(db_column='typeName', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    mass = models.TextField(blank=True, null=True)
    volume = models.TextField(blank=True, null=True)
    capacity = models.TextField(blank=True, null=True)
    portionsize = models.TextField(db_column='portionSize', blank=True, null=True)  # Field name made lowercase.
    raceid = models.TextField(db_column='raceID', blank=True, null=True)  # Field name made lowercase.
    baseprice = models.TextField(db_column='basePrice', blank=True, null=True)  # Field name made lowercase.
    published = models.TextField(blank=True, null=True)
    marketgroupid = models.TextField(db_column='marketGroupID', blank=True, null=True)  # Field name made lowercase.
    iconid = models.TextField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    soundid = models.TextField(db_column='soundID', blank=True, null=True)  # Field name made lowercase.
    graphicid = models.TextField(db_column='graphicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invTypes'


class ScanAlliance(models.Model):
    allianceid = models.BigIntegerField(db_column='allianceID')  # Field name made lowercase.
    ticker = models.TextField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'scan_alliance'


class ScanCharacter(models.Model):
    characterid = models.BigIntegerField(db_column='characterID', unique=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=200)  # Field name made lowercase.
    corpid = models.BigIntegerField(db_column='corpID')  # Field name made lowercase.
    corpname = models.CharField(db_column='corpName', max_length=200)  # Field name made lowercase.
    allianceid = models.BigIntegerField(db_column='allianceID', blank=True, null=True)  # Field name made lowercase.
    alliancename = models.CharField(db_column='allianceName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scan_character'


class ScanCorporation(models.Model):
    corpid = models.BigIntegerField(db_column='corpID')  # Field name made lowercase.
    ticker = models.TextField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'scan_corporation'


class ScanInvgroup(models.Model):
    groupid = models.BigIntegerField(db_column='groupID', unique=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=200)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='categoryID')  # Field name made lowercase.
    capital = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'scan_invgroup'


class ScanInvtype(models.Model):
    typeid = models.BigIntegerField(db_column='typeID', unique=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=200)  # Field name made lowercase.
    group_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'scan_invtype'


class ScanScan(models.Model):
    created = models.DateTimeField()
    token = models.CharField(max_length=6)
    solarsystem = models.TextField(db_column='solarSystem', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField()
    summarytext = models.TextField(db_column='summaryText', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField()
    raw = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scan_scan'
