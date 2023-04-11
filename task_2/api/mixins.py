from rest_framework import mixins, viewsets


class ReadOnlyViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass
