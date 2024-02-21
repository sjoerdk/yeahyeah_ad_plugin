"""Code and classes for saving things longer than runtime

"""
import keyring

from yeahyeah_ad_plugin.exceptions import YeahYeahADError


class KeyRingStorage:
    """Store AD credentials in keyring. Only works if OS is supported by keyring
    see https://pypi.org/project/keyring/
    """
    service_name = "yeahyeah_ad_plugin"
    password_key = "AD_password"

    def save_password(self, value):
        keyring.set_password(self.service_name, self.password_key, value)

    def load_password(self):
        value = keyring.get_password(self.service_name, self.password_key)
        if value is None:
            raise YeahYeahADError(
                f"Could not find key '{self.password_key}' for service " 
                f"'{self.service_name}"
            )
        return value

    def delete_password(self):
        return keyring.delete_password(self.service_name, self.password_key)

