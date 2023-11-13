# Generated by Django 4.2.3 on 2023-08-01 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import plane.db.models.project
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0039_auto_20230723_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmember',
            name='preferences',
            field=models.JSONField(default=plane.db.models.project.get_default_preferences),
        ),
        migrations.AddField(
            model_name='user',
            name='cover_image',
            field=models.URLField(blank=True, max_length=800, null=True),
        ),
        migrations.CreateModel(
            name='IssueReaction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('reaction', models.CharField(max_length=20)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_reactions', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_reactions', to='db.issue')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_%(class)s', to='db.project')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace_%(class)s', to='db.workspace')),
            ],
            options={
                'verbose_name': 'Issue Reaction',
                'verbose_name_plural': 'Issue Reactions',
                'db_table': 'issue_reactions',
                'ordering': ('-created_at',),
                'unique_together': {('issue', 'actor', 'reaction')},
            },
        ),
        migrations.CreateModel(
            name='CommentReaction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('reaction', models.CharField(max_length=20)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_reactions', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_reactions', to='db.issuecomment')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_%(class)s', to='db.project')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace_%(class)s', to='db.workspace')),
            ],
            options={
                'verbose_name': 'Comment Reaction',
                'verbose_name_plural': 'Comment Reactions',
                'db_table': 'comment_reactions',
                'ordering': ('-created_at',),
                'unique_together': {('comment', 'actor', 'reaction')},
            },
        ),       
        migrations.AlterField(
            model_name='project',
            name='identifier',
            field=models.CharField(max_length=12, verbose_name='Project Identifier'),
        ),
        migrations.AlterField(
            model_name='projectidentifier',
            name='name',
            field=models.CharField(max_length=12),
        ),
    ]
