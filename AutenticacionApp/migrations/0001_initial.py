# Generated by Django 4.2.6 on 2024-04-09 13:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=50, unique=True)),
                ('giro', models.CharField(choices=[('Construccion', 'Construcción'), ('Comercial', 'Comercial o Comercio al por menor'), ('Manufacturero', 'Manufacturero'), ('Servicios', 'Servicios'), ('Tecnologia', 'Tecnología de la Información (TI)'), ('Alimenticio', 'Alimenticio'), ('Educativo', 'Educativo'), ('Salud', 'Salud y Cuidado Personal'), ('Financiero', 'Financiero'), ('Energia', 'Energía'), ('Transporte', 'Transporte y Logística'), ('Medios', 'Medios de Comunicación y Entretenimiento')], max_length=50)),
                ('numero_colaboradores', models.IntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('estado_cuenta', models.CharField(choices=[('activo', 'Activa'), ('inactivo', 'Inactiva')], default='activa', max_length=20)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('rut', models.CharField(max_length=12, null=True, unique=True, verbose_name='RUT')),
                ('tipo_usuario', models.CharField(blank=True, choices=[('', 'Selecciona el tipo de usuario'), ('Administrador', 'Administrador'), ('Alumno', 'Alumno'), ('Administrador Kabasis', 'Administrador Kabasis'), ('Asistente Administrativo', 'Asistente Administrativo')], default='', max_length=50, verbose_name='Tipo de Usuario')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='usuarios/', verbose_name='Imagen de Perfil')),
                ('is_first_login', models.BooleanField(default=True)),
                ('is_certificado', models.BooleanField(default=False, verbose_name='Está Certificado')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='AutenticacionApp.area')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AutenticacionApp.empresa')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario Personalizado',
                'verbose_name_plural': 'Usuarios Personalizados',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VerificationToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas_relacionadas', to='AutenticacionApp.empresa'),
        ),
        migrations.AlterUniqueTogether(
            name='area',
            unique_together={('nombre', 'empresa')},
        ),
    ]
