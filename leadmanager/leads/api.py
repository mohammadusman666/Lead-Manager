from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# ViewSets to define CRUD operations on objects
# Lead ViewSet
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny  # for now
    ]
    serializer_class = LeadSerializer
