# Generated by Django 2.0.6 on 2018-06-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landinfo',
            old_name='buildcove',
            new_name='build_cov_area_ratio',
        ),
        migrations.RenameField(
            model_name='landinfo',
            old_name='geography',
            new_name='building_coverage',
        ),
        migrations.RenameField(
            model_name='landinfo',
            old_name='cont_add',
            new_name='conditions_etc',
        ),
        migrations.RenameField(
            model_name='landinfo',
            old_name='cont_num',
            new_name='contact_infomation',
        ),
        migrations.RemoveField(
            model_name='landinfo',
            name='ldarea_cap',
        ),
        migrations.RemoveField(
            model_name='landinfo',
            name='ldarea_low_lim',
        ),
        migrations.RemoveField(
            model_name='landinfo',
            name='price_ceil',
        ),
        migrations.RemoveField(
            model_name='landinfo',
            name='price_low_lim',
        ),
        migrations.AddField(
            model_name='landinfo',
            name='city_planning',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='contact_info',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='current_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='delivery',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='development_permission_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='estab_completion_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='facility',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='floor_area_ratio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='floor_space',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landinfo',
            name='geograpy',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='info_provider',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='info_release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='info_update_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='land_area',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landinfo',
            name='land_law_notification',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='land_rights',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='lease_period_rent',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='maintenance_costs_etc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='most_popular_price_range',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='next_info_update_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='notices',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='optimal_use',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='other_expenses',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='parking',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landinfo',
            name='private_road_burden',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='property_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='property_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='remarks',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='right_money',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='sales_divisions',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='scheduled_sales',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='security_deposit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='seller',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='setback',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='topography',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='total_blocks',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='tsubo_unit_price',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='units_sold_total_units',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='location',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='title',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='traffic',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='url',
            field=models.URLField(max_length=250),
        ),
    ]
