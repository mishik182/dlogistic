import uuid
from django.db import models


class Account(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    accounttypeid = models.ForeignKey('Accounttype', models.DO_NOTHING, db_column='AccountTypeID', blank=True, null=True)  
    addresstypeid = models.ForeignKey('Addresstype', models.DO_NOTHING, db_column='AddressTypeID', blank=True, null=True)  
    cityid = models.ForeignKey('City', models.DO_NOTHING, db_column='CityID', blank=True, null=True)  
    stateid = models.ForeignKey('State', models.DO_NOTHING, db_column='StateID', blank=True, null=True)  
    countryid = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='StatusID', blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  
    street = models.CharField(db_column='Street', max_length=45, blank=True, null=True)  
    house = models.CharField(db_column='House', max_length=10, blank=True, null=True)  
    frame = models.CharField(db_column='Frame', max_length=10, blank=True, null=True)  
    flat = models.CharField(db_column='Flat', max_length=10, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Account'


class Accounttype(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    createon = models.DateTimeField(db_column='CreateOn', auto_now_add=True)
    modifiedon = models.DateTimeField(db_column='ModifiedOn', auto_now=True)
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=45)

    class Meta:
        managed = False
        db_table = 'AccountType'

    def __str__(self):
        return self.name


class AccountHasContact(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='Account_ID')  
    contact = models.ForeignKey('Contact', models.DO_NOTHING, db_column='Contact_ID')  

    class Meta:
        managed = False
        db_table = 'Account_has_Contact'


class AccountHasTrucktype(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='Account_ID')  
    trucktype = models.ForeignKey('Trucktype', models.DO_NOTHING, db_column='TruckType_ID')  

    class Meta:
        managed = False
        db_table = 'Account_has_TruckType'


class Addresstype(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=45)  

    class Meta:
        managed = False
        db_table = 'AddressType'


class City(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    countryid = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  
    stateid = models.ForeignKey('State', models.DO_NOTHING, db_column='StateID', blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=45)  

    class Meta:
        managed = False
        db_table = 'City'


class Contact(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=100)  
    departmentid = models.CharField(db_column='DepartmentID', max_length=36, blank=True, null=True)  
    jobid = models.CharField(db_column='JobID', max_length=36, blank=True, null=True)  
    addresstypeid = models.CharField(db_column='AddressTypeID', max_length=36, blank=True, null=True)  
    cityid = models.CharField(db_column='CityID', max_length=36, blank=True, null=True)  
    stateid = models.CharField(db_column='StateID', max_length=36, blank=True, null=True)  
    countryid = models.CharField(db_column='CountryID', max_length=36, blank=True, null=True)  
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30, blank=True, null=True)  
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=30, blank=True, null=True)  
    skype = models.CharField(db_column='Skype', max_length=45, blank=True, null=True)  
    street = models.CharField(db_column='Street', max_length=45, blank=True, null=True)  
    house = models.CharField(db_column='House', max_length=10, blank=True, null=True)  
    frame = models.CharField(db_column='Frame', max_length=10, blank=True, null=True)  
    flat = models.CharField(db_column='Flat', max_length=10, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Contact'


class Country(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=45)  
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Country'


class State(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    countryid = models.ForeignKey(Country, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=45)  

    class Meta:
        managed = False
        db_table = 'State'


class Status(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=45)  

    class Meta:
        managed = False
        db_table = 'Status'


class Trucktype(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  
    createon = models.DateTimeField(db_column='CreateOn')  
    modifiedon = models.DateTimeField(db_column='ModifiedOn')  
    createbyid = models.CharField(db_column='CreateByID', max_length=36, blank=True, null=True)  
    modifiedbyid = models.CharField(db_column='ModifiedByID', max_length=36, blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=45)  

    class Meta:
        managed = False
        db_table = 'TruckType'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

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


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


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
