#!/usr/bin/env python

#from scrape_linkedin import ProfileScraper
import datetime
import random


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

sagish = {
    'python': 101,
    'docker': 29,
    'ansible': 29,
    'puppet': 11,
    'apache':14,
    'linux': 31,
}

oleg_shn = {
    'python': 18,
    'docker': 18,
    'android': 75,
}

# def skills_of(username):
#
#     with ProfileScraper() as scraper:
#         profile = scraper.scrape(user=username)
#     d = profile.to_dict()
#     jobs = d['experiences']['jobs']
#     return jobs

def get_period(s):
    d1 = " ".join(s.split()[:2])
    d2 = " ".join(s.split()[-2:])
    if 'Present' in d2:
        date2 = datetime.datetime.now()
    else:
        date2 = datetime.datetime.strptime(d2, "%b %Y")
    date1 = datetime.datetime.strptime(d1, "%b %Y")
    return (date2 - date1).days / 30


# def parse(jobs):
#     d = dict([(k, 0) for k in TECHS])
#     for job in jobs:
#         months = get_period(job['date_range'])
#         for t in TECHS:
#             title = job['title'] or ''
#             desc = job['description'] or ''
#             full = title + desc
#             if t in full.lower():
#                 d[t] += int(months)
#     return d

def generate():
    d = dict([(k, 0) for k in TECHS])
    amount = random.randrange(12, 18)
    t = TECHS[:]
    random.shuffle(t)
    projs = t[:amount + 1]
    for p in projs:
        d[p] = random.randrange(20, 100)
    return d

def generate_list():
    t = TECHS[:]
    random.shuffle(t)
    return t

def get_info(link):
    # if 'sagish' in link:
    #     return sagish.keys()
    # elif 'oleg' in link:
    #     return oleg_shn.keys()
    return generate_list()
    #return parse(skills_of(link.strip("/").split("/")[-1]))