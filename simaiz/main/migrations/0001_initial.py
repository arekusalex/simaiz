# Generated by Django 2.0.5 on 2018-05-28 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_fertilizante', models.FloatField(null=True)),
                ('fecha', models.DateField()),
                ('nitrogeno_req', models.FloatField()),
                ('fosforo_req', models.FloatField()),
                ('potasio_req', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_maiz', models.FloatField()),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=20)),
                ('porcentaje', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_depto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_elemento', models.CharField(max_length=20)),
                ('simbolo', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fertilizante', models.CharField(max_length=50)),
                ('tipo_fertilizante', models.CharField(max_length=50)),
                ('configuracion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Configuracion')),
            ],
        ),
        migrations.CreateModel(
            name='Humedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=15)),
                ('valor', models.FloatField()),
                ('promedio', models.FloatField()),
                ('porcentaje', models.FloatField()),
                ('depto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_planta', models.CharField(max_length=20)),
                ('especie', models.CharField(max_length=20)),
                ('dias_ciclo', models.IntegerField()),
                ('agua_req', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estacion', models.CharField(max_length=20)),
                ('zona', models.CharField(max_length=20)),
                ('depto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Simulacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sim', models.CharField(max_length=50)),
                ('fecha_siembra', models.DateField()),
                ('rendimiento', models.FloatField()),
                ('total', models.FloatField()),
                ('compartir', models.BooleanField(default=False)),
                ('planta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Planta')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_suelo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Terreno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('depto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Departamento')),
                ('suelo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Suelo')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_medida', models.CharField(max_length=20)),
                ('prefijo', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='terreno',
            name='unidad',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.UnidadMedida'),
        ),
        migrations.AddField(
            model_name='humedad',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Region'),
        ),
        migrations.AddField(
            model_name='contenido',
            name='elemento',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Elemento'),
        ),
        migrations.AddField(
            model_name='contenido',
            name='fertilizante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Fertilizante'),
        ),
        migrations.AddField(
            model_name='contenido',
            name='suelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Suelo'),
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='fertilizante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Fertilizante'),
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='planta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Planta'),
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='simulacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Simulacion'),
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='terreno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Terreno'),
        ),
    ]
