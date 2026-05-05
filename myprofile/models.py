from django.db import models


class Photo(models.Model):
    CATEGORY_CHOICES = [
        ('portrait', 'ポートレート'),
        ('landscape', '風景'),
        ('wedding', 'ウェディング'),
        ('commercial', 'コマーシャル'),
        ('event', 'イベント'),
    ]
    title = models.CharField('タイトル', max_length=100, blank=True)
    image = models.ImageField('画像', upload_to='photos/')
    category = models.CharField('カテゴリ', max_length=20, choices=CATEGORY_CHOICES, default='portrait')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title or f'Photo {self.id}'


class Contact(models.Model):
    name = models.CharField('お名前', max_length=50)
    email = models.EmailField('メールアドレス')
    message = models.TextField('メッセージ', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'
