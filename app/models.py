from django.db import models

class Theme(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"Theme: {self.title}"

class Exam(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"Exam for Theme: {self.theme.title} (ID: {self.id})"

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"Question: {self.text[:50]}... (ID: {self.id})"

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"Choice: {self.text[:50]}... (Correct: {self.is_correct})"
