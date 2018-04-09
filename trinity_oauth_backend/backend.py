"""
The Texas Gateway OAuth 2 backend.
"""

try:
    from social.backends.oauth import BaseOAuth2
    from social.exceptions import AuthException
except ImportError:
    from social_core.backends.oauth import BaseOAuth2
    from social_core.exceptions import AuthException

from urllib import urlencode


class TrinityOauth2(BaseOAuth2):
    name = 'trinity'
    REDIRECT_STATE = False
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('email', 'email'),
        ('username', 'username'),
        ('fullname', 'fullname'),
        ('district', 'district'),
    ]

    @property
    def base_url(self):
        env = self.setting('ENVIRONMENT', default='production')

        if env == 'staging':
            return 'https://pass-staging.texasgateway.org'
        elif env == 'production':
            return 'https://pass.texasgateway.org'

        raise AuthException(
            'Invalid Trinity environment was found `{env}`, '
            'valid choices are `production` and `staging`.'.format(
                env=env,
            ))

    def authorization_url(self):
        return '{base_url}/oauth/v2/auth'.format(base_url=self.base_url)

    def access_token_url(self):
        return '{base_url}/oauth/v2/token'.format(base_url=self.base_url)

    def get_user_details(self, response):
        """Return user details from Trinity account"""
        fullname, _first_name, _last_name = self.get_user_names(
            fullname='',
            first_name=response.get('first_name', ''),
            last_name=response.get('last_name', ''),
        )

        return {
            'username': response.get('username'),
            'email': response.get('email') or '',
            'fullname': fullname or '',
            'district': response.get('original_district'),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = '{base_url}/api/v1/user/me?{params}'.format(
            base_url=self.base_url,
            params=urlencode({
                'access_token': access_token,
            })
        )

        return self.get_json(url)

    def get_user_id(self, details, response):
        """Use trinity username as unique id"""
        return details['email']
