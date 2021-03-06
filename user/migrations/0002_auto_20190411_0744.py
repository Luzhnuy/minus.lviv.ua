# Generated by Django 2.1.5 on 2019-04-11 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsFriendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'friends_friendship',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FriendsFriendshipFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_friendship_id', models.IntegerField()),
                ('to_friendship_id', models.IntegerField()),
            ],
            options={
                'db_table': 'friends_friendship_friends',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FriendsFriendshiprequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user_id', models.IntegerField()),
                ('to_user_id', models.IntegerField()),
                ('message', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.IntegerField()),
            ],
            options={
                'db_table': 'friends_friendshiprequest',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FriendsUserblocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'friends_userblocks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FriendsUserblocksBlocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userblocks_id', models.IntegerField()),
                ('user_id', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'friends_userblocks_blocks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserActivitys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('l', 'like'), ('d', 'dislike'), ('c', 'comment'), ('s', 'subscribe')], max_length=255, null=True)),
                ('to_user_id', models.IntegerField()),
                ('activity_to', models.IntegerField()),
                ('from_user', models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'useractivitys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/user-post-img/')),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(blank=True, max_length=128, null=True)),
                ('avatar', models.CharField(blank=True, max_length=128, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('hide_birthdate', models.IntegerField(blank=True, null=True)),
                ('icq', models.CharField(blank=True, max_length=10, null=True)),
                ('jabber', models.CharField(blank=True, max_length=128, null=True)),
                ('skype', models.CharField(blank=True, max_length=128, null=True)),
                ('website', models.CharField(blank=True, max_length=128, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('is_admin_subscribed', models.IntegerField()),
                ('status_title', models.CharField(blank=True, max_length=20, null=True)),
                ('status_css', models.CharField(blank=True, max_length=20, null=True)),
                ('banned', models.IntegerField()),
                ('banned_until', models.DateField(blank=True, null=True)),
                ('seen_rules', models.IntegerField()),
                ('is_business', models.BooleanField(default=0)),
                ('is_user_online', models.BooleanField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userprofile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsersStaffticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type_id', models.IntegerField()),
                ('object_id', models.IntegerField()),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('pub_date', models.DateTimeField()),
                ('is_done', models.IntegerField()),
                ('user', models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users_staffticket',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsersUseractivity',
            fields=[
                ('last_activity_ip', models.CharField(max_length=15)),
                ('last_activity_date', models.DateTimeField()),
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users_useractivity',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsersUserrating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('average_minus_rating', models.IntegerField()),
                ('user', models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users_userrating',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='userpost',
            name='userprofile',
            field=models.ForeignKey(on_delete='CASCADE', to='user.Userprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='friendsuserblocksblocks',
            unique_together={('userblocks_id', 'user_id')},
        ),
        migrations.AlterUniqueTogether(
            name='friendsfriendshiprequest',
            unique_together={('to_user_id', 'from_user_id')},
        ),
        migrations.AlterUniqueTogether(
            name='friendsfriendshipfriends',
            unique_together={('from_friendship_id', 'to_friendship_id')},
        ),
    ]
