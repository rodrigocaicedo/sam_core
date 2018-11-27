from usuarios_sam.models import CustomUser as User
from usuarios_sam.authhelper import *
from usuarios_sam.outlookservice import get_me, get_my_photo


class Office365Backend:

	def authenticate(self, email, token, first_name, last_name, name, request):


		try:
			token = token
		except:
			return None

		try:
			user = User.objects.get(email = email)
			return user
		except:
			user= User.objects.create_user(email = email, first_name = first_name, father_last_name = last_name, mother_last_name="")
			#photo = get_my_photo(token)
			#return photo

			#user.user_photo = photo
			#user.save()
			return user


	def get_user(self, user_id):
	    try:
	        return User.objects.get(pk=user_id)
	    except User.DoesNotExist:
	        return None


