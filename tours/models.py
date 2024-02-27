from django.db import models

# Create your models here.
SEASONS = (('Summer', 'Summer'),
           ('Fall', 'Fall'), ('Winter', 'Winter'),
           ('Spring', 'Spring'),)


class TourCategories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tours(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(TourCategories, related_name='tours')
    location = models.CharField(max_length=300)
    description = models.TextField()
    season = models.CharField(max_length=200, choices=SEASONS, default='Summer')
    image = models.ImageField(upload_to='tour_photos')
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    tour_name = models.ForeignKey(Tours, related_name='reservations', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)
    order_comment = models.TextField()
    people_num = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.tour_name} reservation for {self.phone_number}'


class Reviews(models.Model):
    tour = models.ForeignKey(Tours, related_name='reviews', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    image = models.ImageField(upload_to='user_photos')
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review of {self.nickname} for {self.tour}'






