from rest_framework import permissions# Bauyrzhan Kappassov
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.exceptions import PermissionDenied
# Bauyrzhan Kappassov









#IsAdminUser+perm_map: # Bauyrzhan Kappassov
# Bauyrzhan Kappassov
# class IsDocPermission(DjangoModelPermissions): # Bauyrzhan Kappassov
#     perms_map = { # Bauyrzhan Kappassov
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTION': [],
#         'HEAD': [], # Bauyrzhan Kappassov
#         'POST': ['%(app_label)s.add_%(model_name)s'],
#         'PUT': ['%(app_label)s.change_%(model_name)s'],
#         'PATCH': ['%(app_label)s.change_%(model_name)s'],
#         'DElETE': ['%(app_label)s.delete_%(model_name)s'],
#     }
#
#Bauyrzhan Kappassov
















#

# class IsDocPermission(DjangoModelPermissions): # Bauyrzhan Kappassov
#     message_1=[ # Bauyrzhan Kappassov
#         'This is information is closed.'. upper(),
#         'Permission has been denied to you',
#     ]
#     message_2=[ # Bauyrzhan Kappassov
#         'You can not view this because you have forgotten to LOG IN',
#         'log in,please'.upper(),
#     ]
#     perms_map ={ # Bauyrzhan Kappassov
#          'GET':['%(app_label)s.view_%(model_name)s'],
#          'OPTION':[],
#          'HEAD':[],#Bauyrzhan Kappassov
#          'POST':['%(app_label)s.add_%(model_name)s'],
#          'PUT':['%(app_label)s.change_%(model_name)s'],
#         'PATCH':['%(app_label)s.change_%(model_name)s'],
#         'DELETE':['%(app_label)s.delete_%(model_name)s'],
#     }
#     def has_permission(self, request, view):# Bauyrzhan Kappassov
#         user=request.user #object which allows be attached to the HTTP and user can be authenticed or anonymous
#         # if not request.user.username=='Gabbase': #THIS ONE  CERTAIN USER !!!!
#         #    raise PermissionDenied(detail=self.message_1)# Bauyrzhan Kappassov
#         if not request.user.username =='Gabbase':
#             raise PermissionDenied(detail=" ".join(self.message_1))
#         elif not user.is_staff: # is_staff:=admin
#             raise PermissionDenied(detail=" ".join(self.message_2))  # rasing the message
#         else: # Bauyrzhan Kappassov
#             return super().has_permission(request,view) #  it checks all permissions in the chain,
#
#     def has_object_permission(self, request, view, obj): # Bauyrzhan Kappassov
#           if request.method in permissions.SAFE_METHODS:  # only read
#               return request.user.is_staff
#           else: # Bauyrzhan Kappassov
#               return request.user.username =='Gabbase' # user who log in  only
#                # return True ( any user can make changes includer anonymous )




















## it is 2 method of controling the rest API  form the DJ admin:( this permission not working if you use ForeignKey to (Owner) in your model.)

class IsDocPermission(DjangoModelPermissions): # Bauyrzhan Kappassov
    message=[ # Bauyrzhan Kappassov
        'This is information is closed.',
        'log in ,please'.upper()
    ]
    perms_map ={ # Bauyrzhan Kappassov
         'GET':['%(app_label)s.view_%(model_name)s'],
         'OPTION':[],
         'HEAD':[], # Bauyrzhan Kappassov
         'POST':['%(app_label)s.add_%(model_name)s'],
         'PUT':['%(app_label)s.change_%(model_name)s'],
        'PATCH':['%(app_label)s.change_%(model_name)s'],
        'DELETE':['%(app_label)s.delete_%(model_name)s'],
    } # Bauyrzhan Kappassov
    def has_permission(self, request, view): #Bauyrzhan Kappassov
        if request.method in permissions.SAFE_METHODS:
            if not request.user.is_authenticated:
                 raise PermissionDenied(detail=self.message) # Bauyrzhan Kappassov
            else: # Bauyrzhan Kappassov
                return True # otherwise which means u r log in u CAN
        else:# Bauyrzhan Kappassov
            return request.user.is_authenticated



















# class IsDocPermission(DjangoModelPermissions): # Bauyrzhan Kappassov
#     message=[ # Bauyrzhan Kappassov
#         'This is information is closed.',
#         'log in ,please'.upper()
#     ]
#     def has_permission(self, request, view):  # Bauyrzhan Kappassov
#         if request.method in permissions.SAFE_METHODS: # Bauyrzhan Kappassov
#             if not request.user.is_authenticated:# Bauyrzhan Kappassov
#                  raise PermissionDenied(detail=self.message) # rBauyrzhan Kappassov
#                #  return False # ( not for anonymouse user read )
#             else: # Bauyrzhan Kappassov
#                 return True # otherwise which means u r log in u CAN
#         else: # Bauyrzhan Kappassov
#             return request.user.is_authenticated
#
#
#     def has_object_permission(self, request, view, obj): # Bauyrzhan Kappassov
#         if request.method in permissions.SAFE_METHODS: # Bauyrzhan Kappassov
#             return True
#         else:# Bauyrzhan Kappassov
#             return  request.user.is_authenticated # Bauyrzhan Kappassov
#




