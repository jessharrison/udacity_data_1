import unicodecsv
from datatime import datetime as dt
    
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
    
enrollments = read_csv('./enrollments.csv')
daily_engagement = read_csv('./daily_engagement.csv')
project_submissions = read_csv('./project_submissions.csv')

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date,'%Y-%m-%d')
    
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)
    
def parse_boolean(string):
    if string == 'True':
        return True
    elif string == 'False':
        return False
    else:
        return None


for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = parse_boolean(enrollment['is_canceled'])
    enrollment['is_udacity'] = parse_boolean(enrollment['is_udacity'])
    enrollment['join_date'] = parse_date(enrollment['join_date'])



for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = int(float(engagement_record['total_minutes_visited']))
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])


for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

enrollments[0]

daily_engagement[0]

project_submissions[0]