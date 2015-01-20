from django.conf import settings
from tastypie.api import Api
from api.resources import (VestingOrgResource,
                           LinkResource,
                           FolderResource,
                           AssetResource,
                           RegistrarResource,
                           CurrentUserResource,
                           CurrentUserLinkResource,
                           CurrentUserFolderResource,
                           CurrentUserVestingOrgResource)

v1_api = Api(api_name='v%s' % settings.API_VERSION)
v1_api.register(VestingOrgResource())
v1_api.register(LinkResource())
v1_api.register(FolderResource())
v1_api.register(AssetResource())
v1_api.register(RegistrarResource())
# /user and /user/sub_resource urls
v1_api.register(CurrentUserResource())
v1_api.register(CurrentUserLinkResource())
v1_api.register(CurrentUserFolderResource())
v1_api.register(CurrentUserVestingOrgResource())

urlpatterns = v1_api.urls
