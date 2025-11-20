from django.db import models
import string, random

class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)
    last_clicked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(characters, k=6))
            if not URL.objects.filter(short_code=code).exists():
                return code
