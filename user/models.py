# usr/bin/env python3
# -*- coding:utf-8- -*-
from django.db import models


class Student(models.Model):
    gender = [
        ("m", "Male"),
        ("f", "Female")
    ]

    name = models.CharField(max_length=50, verbose_name="Name")
    gender = models.CharField(max_length=10, choices=gender, default='m', verbose_name="Gender")
    birthday = models.DateField(verbose_name="Birthday")
    email = models.EmailField(verbose_name="Email")
    info = models.CharField(max_length=255, verbose_name="Student Introduction", help_text="Introduce yourself in one sentence, no more than 250 words")

    grade = models.CharField(max_length=4, verbose_name="Grade")
    number = models.CharField(max_length=6, verbose_name="Number")
    password = models.CharField(max_length=30, verbose_name="Password")

    class Meta:
        constraints = [
            # 复合主键：保证 grade和number组合的student_id唯一
            models.UniqueConstraint(fields=['grade', 'number'], name='student_id'),
        ]

    def get_id(self):
        return self.grade + self.number

    def __str__(self):
        return "%s (%s)" % (self.grade + self.number, self.name)


class Teacher(models.Model):
    genders = [
        ("m", "Male"),
        ("f", "Female")
    ]

    name = models.CharField(max_length=50, verbose_name="Name")
    gender = models.CharField(max_length=10, choices=genders, default='m', verbose_name="Gender")
    birthday = models.DateField(verbose_name="Birthday")
    email = models.EmailField(verbose_name="Email")
    info = models.CharField(max_length=255, verbose_name="Faculty Introduction", help_text="Introduce yourself in one sentence, no more than 250 words")

    department_no = models.CharField(max_length=3, verbose_name="Department Number")
    number = models.CharField(max_length=7, verbose_name="Number")
    password = models.CharField(max_length=30, verbose_name="Password")

    class Meta:
        constraints = [
            # 复合主键：保证 department_no 和number组合的 teacher_id 唯一
            models.UniqueConstraint(fields=['department_no', 'number'], name='teacher_id'),
        ]



