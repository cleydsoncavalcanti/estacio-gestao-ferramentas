from django.contrib import admin
from .models import ToolType
from .models import Team
from .models import Tool
from .models import UserDetails
from .models import Booking
from .models import Maintenance

admin.site.register(ToolType)
admin.site.register(Team)
admin.site.register(Tool)
admin.site.register(UserDetails)
admin.site.register(Booking)
admin.site.register(Maintenance)
