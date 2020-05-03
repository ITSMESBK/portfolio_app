# ========================================================================================
# ! /usr/bin/env python
# Filename: manage.py

# Description:Adding Functionality to the WebApp

# Author: Bharathkumar S <bharath.kumar@namastecredit.com>
# Python Environment - python 3
# ==========================================================================================
#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
