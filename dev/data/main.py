#!/usr/bin/env python

import jinja2 as jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


def load_data():
  # Opening JSON file
  f = open('data.json')

  # returns JSON object as
  # a dictionary
  data = json.load(f)

  # Closing file
  f.close()

  return data


def write_to_file(filename, data):
  file_path = f'../src/{filename}'
  file = open(file_path, "w")
  file.write(data)
  file.close()

  return print(f'file saved to {file_path}')


def create_index(templateEnv, data):
  template = templateEnv.get_template('index.html.j2')
  file = template.render(data=data['projects'])  # this is where to put args to the template renderer

  write_to_file('index.html', file)


def create_project_pages(templateEnv, data):
  for project in data['projects']:
    template = templateEnv.get_template('project.html.j2')
    file = template.render(project=project, data=data['projects'])
    write_to_file(f"{project['url']}.html", file)


def create_filter_pages(templateEnv, data):
  filters = []
  projects = data['projects']
  for project in projects:
    tags = project['tags']
    filters.extend(tags)
  filters = list(set(filters))

  filter_pages = []
  for filter_page in filters:
    for project in projects:
      if filter_page in project['tags']:
          # f'{filter_page}' = {}
          filter_pages.append(f'{filter_page}')
  print(filter_pages)


def create_info_page(templateEnv, data):
  # for project in data['projects']:
  template = templateEnv.get_template('info.html.j2')
  file = template.render(data=data['projects'])
  write_to_file(f"info.html", file)


def main():
  data = load_data()

  # print(data)

  templateLoader = FileSystemLoader(searchpath='./templates')
  templateEnv = Environment(
    loader=templateLoader,
    autoescape=True,
  )

  create_index(templateEnv, data)

  create_project_pages(templateEnv, data)

  create_info_page(templateEnv, data)
  # create_filter_pages(templateEnv, data)


if __name__ == '__main__':
  main()
