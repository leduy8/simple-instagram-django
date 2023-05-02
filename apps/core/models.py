from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<Tag {self.pk}>"


class Photo(BaseModel):
    url = models.URLField()
    tags = models.ManyToManyField(Tag, related_name="tag_photos")

    def __str__(self):
        return f"<Photo {self.pk}>"


class User(BaseModel, AbstractUser):
    display_name = models.CharField(max_length=50, null=False)
    full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=10, null=True)
    birth_date = models.DateField(null=True)
    bio = models.TextField(null=True)
    location = models.CharField(max_length=50, null=True)
    photos = models.ForeignKey(
        Photo, related_name="user_photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"<User {self.pk}>"


class Follow(BaseModel):
    follower_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )
    followee_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followees"
    )

    class Meta:
        unique_together = ("follower_user", "followee_user")

    def __str__(self):
        return f"<Follow {self.pk}>"


class Comment(BaseModel):
    content = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="comment_photos"
    )
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="replies"
    )

    def __str__(self):
        return f"<Comment {self.pk}>"


class PhotoLike(BaseModel):
    # Likes of photo
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "photo")

    def __str__(self):
        return f"<Like {self.pk}>"


class CommentLike(BaseModel):
    # Likes of comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "comment")

    def __str__(self):
        return f"<Like {self.pk}>"
