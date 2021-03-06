# Generated by Django 2.1.3 on 2018-12-09 20:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100, null=True)),
                ('street', models.CharField(blank=True, db_column='Street', max_length=45, null=True)),
                ('house', models.CharField(blank=True, db_column='House', max_length=10, null=True)),
                ('frame', models.CharField(blank=True, db_column='Frame', max_length=10, null=True)),
                ('flat', models.CharField(blank=True, db_column='Flat', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountHasContact',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
            ],
            options={
                'db_table': 'Account_has_Contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountHasTrucktype',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
            ],
            options={
                'db_table': 'Account_has_TruckType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Accounttype',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createon', models.DateTimeField(auto_now_add=True, db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(auto_now=True, db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'AccountType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Addresstype',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'AddressType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'City',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('departmentid', models.CharField(blank=True, db_column='DepartmentID', max_length=36, null=True)),
                ('jobid', models.CharField(blank=True, db_column='JobID', max_length=36, null=True)),
                ('addresstypeid', models.CharField(blank=True, db_column='AddressTypeID', max_length=36, null=True)),
                ('cityid', models.CharField(blank=True, db_column='CityID', max_length=36, null=True)),
                ('stateid', models.CharField(blank=True, db_column='StateID', max_length=36, null=True)),
                ('countryid', models.CharField(blank=True, db_column='CountryID', max_length=36, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=30, null=True)),
                ('mobilenumber', models.CharField(blank=True, db_column='MobileNumber', max_length=30, null=True)),
                ('skype', models.CharField(blank=True, db_column='Skype', max_length=45, null=True)),
                ('street', models.CharField(blank=True, db_column='Street', max_length=45, null=True)),
                ('house', models.CharField(blank=True, db_column='House', max_length=10, null=True)),
                ('frame', models.CharField(blank=True, db_column='Frame', max_length=10, null=True)),
                ('flat', models.CharField(blank=True, db_column='Flat', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'State',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'Status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trucktype',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=36, primary_key=True, serialize=False)),
                ('createon', models.DateTimeField(db_column='CreateOn')),
                ('modifiedon', models.DateTimeField(db_column='ModifiedOn')),
                ('createbyid', models.CharField(blank=True, db_column='CreateByID', max_length=36, null=True)),
                ('modifiedbyid', models.CharField(blank=True, db_column='ModifiedByID', max_length=36, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'TruckType',
                'managed': False,
            },
        ),
    ]
