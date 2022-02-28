from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,pre_migrate,post_migrate   
from django.core.signals import request_finished,request_started,got_request_exception
from django.db.backends.signals import  connection_created
# @receiver(user_logged_in,sender=User)
# def login_success(sender, request ,user,**kwargs):
#     print("==================================")
#     print("User logged in Signal")
#     print(f'sender: {sender}')
#     print(f'request: {request}')
#     print(f'user: {user}')
#     print(f'kwargs: {kwargs}')
# # user_logged_in.connect(login_success, sender=User) #one way of doing w/o decorator


# @receiver(user_logged_out,sender=User)
# def logout_success(sender, request ,user,**kwargs):
#     print("==================================")
#     print("User log-out in Signal")
#     print(f'sender: {sender}')
#     print(f'request: {request}')
#     print(f'user: {user}')
#     print(f'kwargs: {kwargs}')
# # user_logged_out.connect(logout_success, sender=User) 

# @receiver(user_login_failed)
# def login_failed(sender, request ,credentials,**kwargs):
#     print("==================================")
#     print("User login failed in Signal")
#     print(f'sender: {sender}')
#     print(f'request: {request}')
#     print(f'credentials : {credentials}')
#     print(f'kwargs: {kwargs}')
# # user_login_failed.connect(login_failed)


# #############################################################3

# # Model signals

# @receiver(pre_save,sender=User)
# def at_beginning_save(sender,instance,**kwargs):
#     print("==================================")
#     print("User pre_save Signal")
#     print(f'sender: {sender}')
#     print(f'instance: {instance}')
#     print(f'kwargs: {kwargs}')
# # pre_save.connect(at_beginning_save,sender=User)


# @receiver(post_save,sender=User)
# def at_ending_save(sender,instance,created,**kwargs):
#     if created == True:
#         print("==================================")
#         print("User post_save Signal")
#         print(f"New User created: {instance}")
#         print(f'sender: {sender}')
#         print(f'created: {created}')
#         print(f'kwargs: {kwargs}')
#     else:
#         print("==================================")
#         print("User post_save Signal")
#         print(f"User updated: {instance}")
#         print(f'sender: {sender}')
#         print(f'created: {created}')
#         print(f'kwargs: {kwargs}')
# # post_save.connect(at_ending_save,sender=User)

# @receiver(pre_delete,sender=User)
# def at_beginning_delete(sender,instance,**kwargs):
#     print("==================================")
#     print("User pre_delete Signal")
#     print(f'sender: {sender}')
#     print(f'instance: {instance}')
#     print(f'kwargs: {kwargs}')
# # pre_delete.connect(at_beginning_delete,sender=User)


# @receiver(post_delete,sender=User)
# def at_ending_delete(sender,instance,**kwargs):
#     print("==================================")
#     print("User post_delete Signal")
#     print(f'sender: {sender}')
#     print(f'instance: {instance}')
#     print(f'kwargs: {kwargs}')
# # post_delete.connect(at_ending_delete,sender=User)


# @receiver(pre_init,sender=User)
# def at_beginning_init(sender,*args,**kwargs):
#     print("==================================")
#     print(" pre_init Signal")
#     print(f'sender: {sender}')
#     print(f'Args: {args}')
#     print(f'kwargs: {kwargs}')
# # pre_init.connect(at_beginning_init,sender=User)

# @receiver(post_init,sender=User)
# def at_ending_init(sender,*args,**kwargs):
#     print("==================================")
#     print(" post_init Signal")
#     print(f'sender: {sender}')
#     print(f'Args: {args}')
#     print(f'kwargs: {kwargs}')


# @receiver(request_started)
# def at_beginning_request(sender,environ ,**kwargs):
#     print("==================================")
#     print(" request_started Signal")
#     print(f'sender: {sender}')
#     print(f'environ: {environ}')
#     print(f'kwargs: {kwargs}')
# # request_started.connect(at_beginning_request)

# @receiver(request_finished)
# def at_ending_request(sender,**kwargs):
#     print("==================================")
#     print(" request_finished Signal")
#     print(f'sender: {sender}')
#     print(f'kwargs: {kwargs}')
# # request_finished.connect(at_ending_request)


# @receiver(got_request_exception)
# def at_request_exception(sender,request,**kwargs):
#     print("==================================")
#     print(" got_request_exception Signal")
#     print(f'sender: {sender}')
#     print(f'request: {request}')
#     print(f'kwargs: {kwargs}')

# # got_request_exception.connect(at_request_exception)


# @receiver(pre_migrate)
# def at_beginning_migrate(sender,app_config,verbosity,**kwargs):
#     print("==================================")
#     print(" pre_migrate Signal")
#     print(f'sender: {sender}')
#     print(f'app_config: {app_config}')
#     print(f'verbosity: {verbosity}')
#     print(f'kwargs: {kwargs}')
# # pre_migrate.connect(at_beginning_migrate)

# @receiver(post_migrate)
# def at_ending_migrate(sender,app_config,verbosity,**kwargs):
#     print("==================================")
#     print(" post_migrate Signal")
#     print(f'sender: {sender}')
#     print(f'app_config: {app_config}')
#     print(f'verbosity: {verbosity}')
#     print(f'kwargs: {kwargs}')
# # post_migrate.connect(at_ending_migrate)


# @receiver(connection_created)
# def at_connection_created(sender,connection,**kwargs):
#     print("==================================")
#     print(" connection_created Signal after connection established to DB")
#     print(f'sender: {sender}')
#     print(f'connection: {connection}')
#     print(f'kwargs: {kwargs}')
# # connection_created.connect(at_connection_created)


######################Custom Signals#####################################


from django.dispatch.dispatcher import Signal

notification = Signal() # Creating Signal


@receiver(notification)
def show_notification(sender, **kwargs):
    print(f'Notification Signal:')
    print(f'Sender: {sender}')
    print(f'kwargs: {kwargs}')
    







