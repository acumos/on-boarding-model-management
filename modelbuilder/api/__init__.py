import os

# TODO (pk9069): clean way of handling this
dir_path = os.path.dirname(os.path.join(os.path.realpath(__file__)))
properties_path = os.path.join(dir_path, '..', '..', 'properties')
os.environ['PROPERTIES_PATH'] = properties_path
