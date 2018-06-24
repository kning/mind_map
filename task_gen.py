from mind_map import data
import json
import random

def pretty_print(category, subcategory, project=None):
  line_break = "#----------------------------------------------------#"

  print(line_break)
  print("CATEGORY")
  print(category)
  print()
  print("SUBCATEGORY OF THE WEEK")
  print(subcategory)

  if project:
    print("==> %s" % project['project_name'])
    print("==> %s" % project['description'])

  print(line_break)

def log_progress():
  """
  Write the results to a spreadsheet after each run for easy logging
  """

def draw_mind_map():
  #should be 4 categories: Music, Data Science, Social, and Physical
  cat_draw = random.randint(0, 3)

  category = list(data)[cat_draw]

  sub_cat_dict = data[category]
  sub_categories = list(sub_cat_dict)

  #draw random subcategory
  sc_draw = random.randint(0, len(sub_categories)-1)
  sub_category = sub_categories[sc_draw]
  
  #draw random project
  projects = sub_cat_dict.get(sub_category)
  proj_draw = random.randint(0, len(projects)-1)
  project = projects[proj_draw]

def draw_mind_map2():
  MIND_MAP2_PATH = "mind_map2.json"

  with open(MIND_MAP2_PATH, "r") as f:
    data = json.loads(f.read())

  #draw random category
  category_draw = random.randint(0,2)
  category = list(data.keys())[category_draw]

  #draw random subcategory
  sc_draw = random.randint(0, len(data[category])-1)
  sub_category = data[category][sc_draw]

  return category, sub_category

if __name__ == "__main__":
  #TODO: cron this to run every Sunday
  a,b = draw_mind_map2()
  pretty_print(a, b)

  print("log progress at: https://docs.google.com/spreadsheets/d/1P7gnigZ_36vtrPwM5niAd4cJl-d0_PIJBcOlqdPkbu4/edit#gid=1501612727")

  