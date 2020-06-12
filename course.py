from bs4 import BeautifulSoup
from scrape import simple_get
import re

class Course:
    prefix = 'http://www.ucalendar.uwaterloo.ca/2021/COURSE/course-'

    def __init__(self, code, num, types, credit, id, name, description, prereq, antireq):
        self.code = code
        self.num = num
        self.types = types
        self.credit = credit
        self.id = id
        self.name = name
        self.description = description
        self.prereq = prereq
        self.antireq = antireq
    
    def __str__(self):
        l1 = f'{self.code} {self.num} - {self.name} {self.types} {self.credit}, {self.id}\n\n'
        l2 = f'{self.description}\n\n'
        l3 = f'Prerequisite: {self.prereq}\n'
        l4 = f'Antirequisite: {self.antireq}\n'
        return l1 + l2 + l3 + l4

def get_course(code, num):
    raw_html = simple_get('{0}{1}.html'.format(Course.prefix, code))

    if raw_html is None: 
        return None
    
    html = BeautifulSoup(raw_html, 'html.parser')
    for course in html.select('center'):
        data = course.find_all(text=True)

        if str(num).strip() == data[0].split(' ')[1].strip():
            return parse(data)
    
    return None

def parse(lines):
    code, num, types, credit = [token.strip() for token in lines[0].split()]
    num, credit = int(num), float(credit)

    id = lines[1].split()[2].strip()
    name = lines[2].strip()
    description = lines[3].strip()

    prereq = lines[5].replace('Prereq: ', '').strip()
    antireq = lines[6].replace('Antireq: ', '').strip()
    return Course(code, num, types, credit, id, name, description, prereq, antireq)