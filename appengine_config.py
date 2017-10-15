import os
# [START vendor]
from google.appengine.ext import vendor


# pip install -t lib -r requirements.txt
# Add any libraries installed in the "lib" folder.
vendor.add('lib')
# vendor.add('lib/google-cloud')
# vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
# [END vendor]
