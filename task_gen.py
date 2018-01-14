from mind_map import data
import random

def pretty_print(category, subcategory, project):
  line_break = "#----------------------------------------------------#"

  print line_break
  print "CATEGORY"
  print category

  print "SUBCATEGORY OF THE WEEK"
  print sub_category

  print "==> %s" % project['project_name']
  print "==> %s" % project['description']

  print line_break

def log_progress():
  """
  Write the results to a spreadsheet after each run for easy logging
  """

if __name__ == "__main__":
  #TODO: cron this to run every Sunday

  #should be 4 categories: Music, Data Science, Social, and Physical
  cat_draw = random.randint(0, 3)

  category = data.keys()[cat_draw]

  sub_cat_dict = data[category]
  sub_categories = sub_cat_dict.keys()

  #draw random subcategory
  sc_draw = random.randint(0, len(sub_categories)-1)
  sub_category = sub_cat_dict.keys()[sc_draw]
  
  #draw random project
  projects = sub_cat_dict.get(sub_category)
  proj_draw = random.randint(0, len(projects)-1)
  project = projects[proj_draw]
  
  pretty_print(category, sub_category, project)

  print "log progress at: https://docs.google.com/spreadsheets/d/1P7gnigZ_36vtrPwM5niAd4cJl-d0_PIJBcOlqdPkbu4/edit#gid=1501612727"

  