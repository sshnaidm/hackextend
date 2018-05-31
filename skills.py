#!/usr/bin/env python

from scrape_linkedin import ProfileScraper
import datetime


TECHS = [
    'android',
    'nginx',
    'hadoop',
    'prometheus',
    'vue',
    'ansible',
    'mongo',
    'django',
    'docker',
    'apache',
    'grafana',
    'redis',
    'opencv',
    'python',
    'linux',
    'react',
    'kubernetes',
    'java',
    'angular',
    'puppet'
]

def skills_of(username):

    with ProfileScraper() as scraper:
        profile = scraper.scrape(user=username)
    d = profile.to_dict()
    jobs = d['experiences']['jobs']
    return jobs

def get_period(s):
    d1 = " ".join(s.split()[:2])
    d2 = " ".join(s.split()[-2:])
    if 'Present' in d2:
        date2 = datetime.datetime.now()
    else:
        date2 = datetime.datetime.strptime(d2, "%b %Y")
    date1 = datetime.datetime.strptime(d1, "%b %Y")
    return (date2 - date1).days / 30


def parse(jobs):
    d = dict([(k, 0) for k in TECHS])
    for job in jobs:
        months = get_period(job['date_range'])
        for t in TECHS:
            title = job['title'] or ''
            desc = job['description'] or ''
            full = title + desc
            if t in full.lower():
                d[t] += int(months)
    return d
