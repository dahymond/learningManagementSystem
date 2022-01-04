# Generated by Django 4.0 on 2022-01-02 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_field', models.CharField(blank=True, max_length=2000, null=True)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.section')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.CharField(blank=True, max_length=2000)),
                ('skills', models.CharField(blank=True, max_length=2000)),
                ('aoi', models.CharField(blank=True, max_length=2000)),
                ('github', models.CharField(blank=True, max_length=2000)),
                ('linkedin', models.CharField(blank=True, max_length=2000)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.section')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ut1', models.CharField(blank=True, max_length=200)),
                ('ut2', models.CharField(blank=True, max_length=200)),
                ('ut3', models.CharField(blank=True, max_length=200)),
                ('ut1p', models.ImageField(blank=True, upload_to='plots')),
                ('ut2p', models.ImageField(blank=True, upload_to='plots')),
                ('ut3p', models.ImageField(blank=True, upload_to='plots')),
                ('ut1pb', models.ImageField(blank=True, upload_to='plots')),
                ('ut2pb', models.ImageField(blank=True, upload_to='plots')),
                ('ut3pb', models.ImageField(blank=True, upload_to='plots')),
                ('ut12', models.ImageField(blank=True, upload_to='plots')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_field', models.CharField(blank=True, max_length=2000, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
