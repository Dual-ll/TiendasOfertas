# Generated by Django 2.1.2 on 2018-12-13 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idCiudad', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('idLista', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('costoPresupuesto', models.IntegerField(default=0)),
                ('costoReal', models.IntegerField(default=0)),
                ('notas', models.CharField(default='', max_length=500)),
                ('estado', models.CharField(default='Pendiente', max_length=50)),
                ('idLista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lista')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('idTienda', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('nombreSucursal', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Ciudad')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Region')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='idTienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tienda'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='idRegion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
    ]
