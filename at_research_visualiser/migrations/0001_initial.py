# Generated by Django 3.1.1 on 2020-09-25 11:42

from django.db import migrations, models
import django.db.models.deletion
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approach', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AssistiveProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_type', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=500)),
                ('last_name', models.CharField(default='', max_length=500)),
                ('email_id', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GeoResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impairment_definition', models.CharField(default='', max_length=500)),
                ('impairment_definition_other', models.CharField(default='', max_length=500)),
                ('outcome_definition_other', models.CharField(default='', max_length=500)),
                ('proportion', models.FloatField()),
                ('n', models.IntegerField(default=1)),
                ('out_of_n', models.IntegerField(default=1)),
                ('out_of_population', models.CharField(default='', max_length=200)),
                ('ci_high', models.IntegerField(default=1)),
                ('ci_low', models.IntegerField(default=1)),
                ('ap_type', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='at_research_visualiser.assistiveproduct')),
            ],
        ),
        migrations.CreateModel(
            name='OutcomeDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome_definition', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Stratified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stratified', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_ID', models.IntegerField(default=1)),
                ('title', models.TextField()),
                ('url', models.URLField()),
                ('publication_date', models.DateField()),
                ('data_collection_start', models.DateField()),
                ('data_collection_end', models.DateField()),
                ('age_range_low', models.IntegerField(default=0)),
                ('age_range_high', models.IntegerField(default=100)),
                ('survey_name', models.CharField(default='', max_length=200)),
                ('dataset_used', models.CharField(default='', max_length=200)),
                ('study_design', models.CharField(default='', max_length=200)),
                ('sampling_method', models.CharField(default='', max_length=200)),
                ('sampling_frame', models.CharField(default='', max_length=200)),
                ('enumerated_sample_size', models.IntegerField(default=1)),
                ('quality', models.IntegerField(default=1)),
                ('approach', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='at_research_visualiser.approach')),
                ('author', sortedm2m.fields.SortedManyToManyField(help_text=None, to='at_research_visualiser.Author')),
                ('georesults', models.ManyToManyField(to='at_research_visualiser.GeoResult')),
                ('stratified', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='at_research_visualiser.stratified')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='at_research_visualiser.tool')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapbox_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('auto_parent', models.BooleanField(default=True)),
                ('parent_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='at_research_visualiser.location')),
            ],
        ),
        migrations.AddField(
            model_name='georesult',
            name='location',
            field=models.ManyToManyField(to='at_research_visualiser.Location'),
        ),
        migrations.AddField(
            model_name='georesult',
            name='outcome_definition',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='at_research_visualiser.tool'),
        ),
    ]
