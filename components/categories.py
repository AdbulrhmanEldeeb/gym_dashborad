import os

class ChartCategories:
    def __init__(self, vis_folder):
        self.vis_folder = vis_folder
        self.chart_categories = self._categorize_charts()

    def _categorize_charts(self):
        all_charts = [f for f in os.listdir(self.vis_folder) if f.endswith('.html')]
        
        return {
            "Demographic Overview": [
                'Gender_Distribution.html',
                'Age_Distribution.html',
                'Age_Distribution_with_Density_Curve.html',
                'Gender_Age_Distribution_by_Group.html',
                'members_by_age_abonoment.html'
            ],
            "Membership & Subscription": [
                'abonoment_type.html',
                'avg_visits_by_age_abonoment.html',
                'heatmap_visits_by_age_abonoment.html',
                'visit_per_week_count.html'
            ],
            "Gym Attendance & Time Patterns": [
                'Gym_Visits_by_Day_of_Week.html',
                'gym_visits_by_day.html',
                'Hourly_Gym_Attendance_Trend.html',
                'avg_time_check_in.html',
                'avg_time_check_out.html',
                # 'check_in_hours_scatter.html',
                # 'check_out_hours_scatter.html',
                'avg_time_in_gym_Distribution.html',
                'avg_time_in_gym_Histogram.html'
            ],
            "Group Lessons & Training": [
                'Lessons_Count.html',
                'female_Lessons_Count.html',
                'male_Lessons_Count.html',
                'Distribution_of_Group_Lessons_by_Age_Group.html',
                'Heatmap_Distribution_of_Group_Lessons_by_Age_Group.html',
                'Percentage_Distribution_of_Group_Lessons_by_Age_Group.html',
                'group_lesson_attendance.html',
                'group_lesson_attendance_heatmap.html',
                'Personal_Training_Age_Distribution_by_Group.html',
                'personal_training_distribution.html',
                'personal_trainer_distribution.html'
            ],
            "Trainer & Staff Analysis": [
                'Trainer_Age_Distribution_by_Group.html',
                'female_trainers_distribution.html',
                'male_trainers_distribution.html'
            ],
            "Additional Insights": [
                'avg_gym_time_by_abo_gender_bar.html',
                'avg_gym_time_by_abo_gender_heatmap.html',
                'avg_gym_time_by_abo_gender_pie.html',
                'attend_group_lesson_count.html'
            ],
            "Sauna & Amenities Usage": [
                'sauna_usage_distribution.html',
                'sauna_usage_by_gender_percentage.html',
                'sauna_usage_by_gender_pie.html',
                'sauna_usage_by_gender_stacked.html',
                'females_using_sauna.html',
                'males_using_sauna.html'
            ]
        }
