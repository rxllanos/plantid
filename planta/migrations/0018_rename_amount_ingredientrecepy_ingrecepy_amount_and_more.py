# Generated by Django 4.2.9 on 2024-05-26 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0017_rename_id_recepy_recepy_recepy_id_recepy_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='amount',
            new_name='ingrecepy_amount',
        ),
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='id_ingredientrecepy',
            new_name='ingrecepy_id_ingredientrecepy',
        ),
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='image',
            new_name='ingrecepy_image',
        ),
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='is_missed',
            new_name='ingrecepy_is_missed',
        ),
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='meta',
            new_name='ingrecepy_meta',
        ),
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='name',
            new_name='ingrecepy_name',
        ),
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='recepy',
            new_name='ingrecepy_recepy',
        ),
        migrations.RenameField(
            model_name='ingredientrecepy',
            old_name='unit',
            new_name='ingrecepy_unit',
        ),
    ]
