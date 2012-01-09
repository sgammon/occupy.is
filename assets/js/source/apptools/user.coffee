

class CoreUserAPI extends CoreAPI

	constructor: (apptools) ->

		@current_user = {}

		@setUserInfo: (userinfo) ->
			$.apptools.dev.log('UserAPI', 'Setting server-injected userinfo.', userinfo)

			@current_user.username = userinfo.current_user
			@current_user.is_user_admin = userinfo.is_user_admin
			@current_user.login_url = userinfo.login_url
			@current_user.logout_url = userinfo.logout_url