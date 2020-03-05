errors = {
    'session': {
        'SESSION_NOT_CREATED': ('Redis session was not created', 'E100'),
        'NO_SESSION': ('Session token not valid', 'E101'),
        'NO_STATE': ('Session state not found', 'E102'),
        'NO_KEY': ('Section corresponding to key not found in session', 'E103'),
        'RESPONSE_BUILD_FAILED': ('{}', 'E104')
    },
    'auth': {
        'LDAP_AMBIGUOUS_SEARCH': ('Ambiguous LDAP search', 'E200'),
        'INVALID_API_KEY': ('The api key provided is not valid', 'E201'),
        'INVALID_CREDENTIALS': ('Invalid credentials provided', 'E202'),
        'FAILED_AUTH_GENERIC': ('Failed to authenticate with error - {}', 'E203'),
        'USER_NOT_FOUND': ('Can not find user with username {}', 'E204'),
        'JWT_EXPIRED': ('JSON Web Token signature expired', 'E205'),
        'JWT_INVALID': ('Invalid JSON Web Token', 'E206'),
        'JWT_GENERIC': ('Error reading JSON Web Token', 'E207'),
        'JWT_GENERATION_FAILED': ('Unable to generate JSON Web Token', 'E208'),
    },
    'account': {
        'LDAP_AMBIGUOUS_SEARCH': ('Ambiguous LDAP search', 'E300'),
        'LDAP_UNKNOWN': ('{}', 'E301'),
        'LDAP_DUPLICATE_ENTRY': ('LDAP entry already exists', 'E302'),
        'LDAP_GENERIC': ('{}', 'E303'),
        'USER_NOT_FOUND': ('User "{}" not found', 'E304'),
        'INVALID_PAYLOAD': ('Update user: Payload failed validation - {}', 'E305'),
        'BAD_PASSWORD': ('Supplied password is unacceptable', 'E306'),
        'ULAPD_USER_DELETE_FAIL': ('Ulapd-API failed to delete user details - {}', 'E307'),
        'NOTIFY_FAIL': ('Notify has failed to send the email', 'E308'),
        'AUTH_TOKEN_ERROR': ('Authentication API failed to return a password creation token', 'E309'),
        'VERIFICATION_FAIL': ('Verification-api has failed to process the request', 'E310'),
        'ULAPD_DATASET_FAIL': ('Ulapd-API failed to get dataset details', 'E311')
    },
    'verification_ui': {
        'API_HTTP_ERROR': ('Received the following response from verification_api: {}', 'E401'),
        'API_CONN_ERROR': ('Encountered an error connecting to verification_api: {}', 'E402'),
        'API_TIMEOUT': ('Connection to verification_api timed out: {}', 'E403'),
        'ADFS_ROLE_LOGGED_IN_ERROR': ('User is logged in but does not have role {}', 'E404'),
        'ADFS_ROLE_LOGGED_OUT_ERROR': ('User is not logged in so cannot have role {}', 'E405')

    },
    'verification_api': {
        'ACCOUNT_API_HTTP_ERROR': ('Received the following response from account_api: {}', 'E501'),
        'ACCOUNT_API_CONN_ERROR': ('Encountered an error connecting to account_api: {}', 'E502'),
        'ACCOUNT_API_TIMEOUT': ('Connection to account_api timed out: {}', 'E503'),
        'AUDIT_API_HTTP_ERROR': ('Received the following response from audit_api: {}', 'E504'),
        'AUDIT_API_CONN_ERROR': ('Encountered an error connecting to audit_api: {}', 'E505'),
        'AUDIT_API_TIMEOUT': ('Connection to audit_api timed out: {}', 'E506'),
        'VERIFICATION_ERROR': ('Error in verification-api: {}', 'E507'),
        'SQLALCHEMY_ERROR': ('SQLAlchemy error: {}', 'E508'),
        'AKUMA_API_HTTP_ERROR': ('Received the following response from akuma_api: {}', 'E509'),
        'AKUMA_API_CONN_ERROR': ('Encountered an error connecting to akuma_api: {}', 'E510'),
        'AKUMA_API_TIMEOUT': ('Connection to akuma_api timed out: {}', 'E511'),
        'LOCKING_ERROR': ('Locking error: {}', 'E512'),
        'CASE_NOT_FOUND': ('User "{}" not found', 'E513'),
        'METRIC_API_HTTP_ERROR': ('Received the following response from dps_metric_api: {}', 'E514'),
        'METRIC_API_CONN_ERROR': ('Encountered an error connecting to dps_metric_api: {}', 'E515'),
        'METRIC_API_TIMEOUT': ('Connection to dps_metric_api timed out: {}', 'E516'),
        'ULAPD_API_HTTP_ERROR': ('Received the following response from ulapd_api: {}', 'E517'),
        'ULAPD_API_CONN_ERROR': ('Encountered an error connecting to ulapd_api: {}', 'E518'),
        'ULAPD_API_TIMEOUT': ('Connection to ulapd_api timed out: {}', 'E519')
    },
    'dps_metric_api': {
        'SQLALCHEMY_ERROR': ('SQLAlchemy error: {}', 'E601'),
        'CASE_NOT_FOUND': ('User "{}" not found', 'E602')
    },
    'ulapd_api': {
        'SQLALCHEMY_ERROR': ('SQLAlchemy error: {}', 'E701'),
        'USER_NOT_FOUND': ('User "{}" not found', 'E702'),
        'LICENCE_AGREE_ERROR': ('Failed to add new licence agreement: {}', 'E703'),
        'CREATE_USER_ERROR': ('Failed to create user: {}', 'E704'),
        'DELETE_USER_ERROR': ('Failed to delete user: {}', 'E705'),
        'RESET_API_KEY_ERROR': ('Failed to reset API key: {}', 'E706'),
        'DATASET_NOT_FOUND': ('Dataset: {} not found', 'E707'),
        'USER_TYPE_NOT_FOUND': ('User type: {} not found', 'E708'),
        'ACCOUNT_API_HTTP_ERROR': ('Received the following response from account_api: {}', 'E709'),
        'ACCOUNT_API_CONN_ERROR': ('Encountered an error connecting to account_api: {}', 'E710'),
        'ACCOUNT_API_TIMEOUT': ('Connection to account_api timed out: {}', 'E711'),
        'VERIFICATION_API_HTTP_ERROR': ('Received the following response from verification_api: {}', 'E712'),
        'VERIFICATION_API_CONN_ERROR': ('Encountered an error connecting to verification_api: {}', 'E713'),
        'VERIFICATION_API_TIMEOUT': ('Connection to verification_api timed out: {}', 'E714')
    },
    'ulapd_ui': {
        'API_HTTP_ERROR': ('Received the following response from ulapd_api: {}', 'E801'),
        'API_CONN_ERROR': ('Encountered an error connecting to ulapd_api: {}', 'E802'),
        'API_TIMEOUT': ('Connection to ulapd_api timed out: {}', 'E803'),
        'NO_DATASETS_FOUND': ('No datasets found', 'E804'),
        'DATASET_NOT_FOUND': ('Dataset {} not found', 'E805'),
        'API_KEY_ERROR': ('Provided API key: {} is incorrect or does not exist', 'E806'),
        'FILE_DOES_NOT_EXIST': ('The file name: {} provided does not exist', 'E807'),
        'NO_LICENCE_SIGNED': ('You have not yet signed the licence for this dataset: {}', 'E808'),
        'DATASET_NOT_PAID': ('You have not paid for access to this dataset: {}', 'E809'),
        'NO_DATASET_ACCESS': ('You do not have access to this dataset: {}', 'E810'),
        'RESOURCE_NOT_FOUND': ('Resource: {} not found', 'E811')
    }
}


def get(app, key, filler=None):
    if filler is None:
        return errors[app][key]

    template = errors[app][key][0]
    message = template.format(filler)
    code = errors[app][key][1]
    return message, code


def get_message(app, key, filler=None):
    return get(app, key, filler)[0]


def get_code(app, key):
    return get(app, key)[1]
