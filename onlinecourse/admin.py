
"""Admin configuration for the OnlineCourse application."""

from django.contrib import admin
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Enrollment,
    Question,
    Choice,
)


class ChoiceInline(admin.StackedInline):
    """Display choices inside a question."""
    model = Choice
    extra = 4


class QuestionInline(admin.StackedInline):
    """Display questions inside a lesson."""
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """Configure the question admin interface."""
    inlines = [ChoiceInline]
    list_display = ("question_text", "lesson", "grade")


class LessonAdmin(admin.ModelAdmin):
    """Configure the lesson admin interface."""
    inlines = [QuestionInline]


admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
