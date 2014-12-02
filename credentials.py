class Windows:
    category = "Host"
    name = "Windows"

    def __init__(self, username, password, domain="", auth_method="Password"):
        self.username = username
        self.password = password
        self.domain = domain
        self.auth_method = auth_method

class SSH:
    category = "Host"
    name = "SSH"

    def __init__(self, username, password, auth_method="password", elevate_privileges_with="Nothing", escalation_account="", escalation_password=""):
        if auth_method not in ("password", "certificate", "Kerberos", "public key"):
            raise ValueError('auth_method not valid')

        self.username = username
        self.password = password
        self.auth_method = auth_method
        if elevate_privileges_with == "Cisco 'enable'":
            self.escalation_password = escalation_password
        if elevate_privileges_with == "sudo":
            self.escalation_account = escalation_account
            self.escalation_password = escalation_password
        self.elevate_privileges_with = elevate_privileges_with

class Salesforce:
    category = "Cloud Services"
    name = "Salesforce.com"

    def __init__(self, username, password):
        self.username = username
        self.password = password

class PaloAltoPANOS:
    category = "Miscellaneous"
    name = "Palo Alto Networks PAN-OS"

    def __init__(self, username, password, port="443", verify_ssl=True):
        self.username = username
        self.password = password
        self.port = port
        self.verify_ssl = verify_ssl
