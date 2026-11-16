
"""Django admin configuration for OnlineCourse."""

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
    """Allow choices to be edited inside a question."""
    model = Choice
    extra = 4


class QuestionInline(admin.StackedInline):
    """Allow questions to be edited inside a course."""
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """Configure the Question administration page."""
    inlines = [ChoiceInline]
    list_display = ("question_text", "course", "grade")


class LessonAdmin(admin.ModelAdmin):
    """Configure the Lesson administration page."""
    list_display = ("title", "course")


class CourseAdmin(admin.ModelAdmin):
    """Configure the Course administration page."""
    inlines = [QuestionInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
