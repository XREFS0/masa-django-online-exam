"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="status",
        ),
    ]
