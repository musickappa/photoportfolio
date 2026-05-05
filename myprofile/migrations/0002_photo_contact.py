from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Myprofile',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='photos/', verbose_name='画像')),
                ('category', models.CharField(
                    choices=[
                        ('portrait', 'ポートレート'),
                        ('landscape', '風景'),
                        ('wedding', 'ウェディング'),
                        ('commercial', 'コマーシャル'),
                        ('event', 'イベント'),
                    ],
                    default='portrait',
                    max_length=20,
                    verbose_name='カテゴリ',
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='お名前')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('message', models.TextField(max_length=1000, verbose_name='メッセージ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
