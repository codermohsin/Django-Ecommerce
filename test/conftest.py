import os
import sys
import django

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

# Setup Django
django.setup()
