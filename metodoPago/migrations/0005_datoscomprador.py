# Generated by Django 4.2.6 on 2024-04-05 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metodoPago', '0004_planpago_alumnos'),
    ]

    operations = [
        migrations.CreateModel(
            name='datosComprador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.CharField(max_length=255)),
                ('rutEmpresa', models.CharField(max_length=255)),
                ('razonSocial', models.CharField(max_length=255)),
                ('giro', models.CharField(max_length=255)),
                ('DireccionTributaria', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('comuna', models.CharField(max_length=255)),
                ('nombreComprador', models.CharField(max_length=255)),
                ('rutComprador', models.CharField(max_length=255)),
                ('correoComprador', models.CharField(max_length=255)),
                ('numeroContacto', models.CharField(max_length=255)),
                ('estadoPago', models.BooleanField(default=False)),
                ('id_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metodoPago.planpago')),
            ],
        ),
    ]
