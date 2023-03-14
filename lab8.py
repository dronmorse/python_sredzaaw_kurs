#!/usr/bin/env python3

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for p,l in zip(projects,leaders):
    print("Project: ", p, "Leader: ", l)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for pos,(date,p,l) in enumerate(zip(dates,projects,leaders)):
    print(pos+1, "- The leader of", p, "started", date, "is", l)

