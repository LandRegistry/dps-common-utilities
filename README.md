# Common Utilities

This repository contains modules that can be reused across the service's APIs. 

### Use
To use the modules contained in this repository in other application, add this line to the `requirements.txt` file at the applications's root:
> `git+http://192.168.249.38/dps-beta/common-utilities.git@`<specific>`#egg=common_utilities`

where <specific> is either the branch name, full commit hash or tag of the version of the repository you wish to use. For example:
> `git+http://192.168.249.38/dps-beta/common-utilities.git@v1.0.0#egg=common_utilities`



## `errors.py`

The `errors` module handles the definition of error codes and messages, and is intended to act as a **single source of truth** for all errors used throughout the service's APIs.

The module consists of two parts:

1. The `errors` dictionary
2. The getter functions

### Error Dictionary

The error dictionary is a simple Python dictionary which contains the actual definitions of the error codes and messages. It is structured like so:

```python
errors = {
    "app": {
        "key": ("message", 'code'),
        "another_key": ("message with string formatting slot: {}", 'different code')
    },
    "app2": {
        "key": ("message", 'code')
    }
}
```

for example:

```python
errors = {
    "session": {
        "SESSION_NOT_CREATED": ("Redis session was not created", 'E100'),
        "NO_SESSION": ("Session token not valid", 'E101'),
        "NO_STATE": ("Session state not found", 'E102'),
        "NO_KEY": ("Section corresponding to key not found in session", 'E103'),
        "RESPONSE_BUILD_FAILED": ("{}", 'E104')
    },
    "auth": {
        "LDAP_AMBIGUOUS_SEARCH": ("Ambiguous LDAP search", 'E200'),
        "INVALID_API_KEY": ("The api key provided is not valid", 'E201'),
        "INVALID_CREDENTIALS": ("Invalid credentials provided", 'E202'),
        "FAILED_AUTH_GENERIC": ("Failed to authenticate with error - {}", 'E203'),
        "USER_NOT_FOUND": ("Can not find user with username {}", 'E204'),
        "JWT_EXPIRED": ("JSON Web Token signature expired", 'E205'),
        "JWT_INVALID": ("Invalid JSON Web Token", 'E206'),
        "JWT_GENERIC": ("Error reading JSON Web Token", 'E207'),
        "JWT_GENERATION_FAILED": ("Unable to generate JSON Web Token", 'E208')
    },
    "account": {
        "LDAP_AMBIGUOUS_SEARCH": ("Ambiguous LDAP search", 'E300'),
        "LDAP_UNKNOWN": ("{}", 'E301'),
        "LDAP_DUPLICATE_ENTRY": ("LDAP entry already exists", 'E302'),
        "LDAP_GENERIC": ("{}", 'E303'),
        "USER_NOT_FOUND": ("User {} not found", 'E304'),
        "INVALID_PAYLOAD": ("Update user: Payload failed validation - {}", 'E305'),
        "BAD_PASSWORD": ("Supplied password is unacceptable", 'E306'),
        "RESPONSE_BUILD_FAILED": ("{}", "E07")
    }
}
```

Note the following:

1. `app` must be unique within the first level.
2. `key` must be unique within its application.
3. `code` should be unique within its application.
4. `message` should be as useful as possible, and may contain one slot for runtime string formatting (`{}`)
5. Each application has 100 possible error codes (thus all `code`s within an application should begin with the same digit), to ease confusion during debugging.
6. Similar errors should be repeated in multiple applications, instead of entering the application once and then referencing from a different application. Corresponding error codes have been used so far but this is purely for aesthetic purposes.

New error codes can be added to the dictionary very simply, but the reference your application's `requirements.txt` may need updating and the application will need to be rebuilt for the changes to take effect.



### The Getter Functions

The tuples that make up the error definitions have been structured with the `ApplicationError` class's constructor in mind. The modules basic `get` function simply returns the specified error definition/code pair in the order that the `ApplicationError` constructor accepts. It has the signature:

> **`get`**(_app_, _key_, _filler=None_)

The `filler` argument may be used when getting errors that have a string formatting slot (`{}`). The module will perform `string.format()` on the error's message, using the`filler` that you provide.

An example of how to use this method is:

> `raise ApplicationError(*errors.get("session", "SESSION_NOT_CREATED"))`

or, if you wish to use string formatting to form a more precise error message:

> `raise ApplicationError(*errors.get("account", "RESPONSE_BUILD_FAILED", filler=str(ex)))`

The `*` expands the tuple into seperate arguments for consumption by the `ApplicationError`'s constructor.

#### Querying

For cases where you don't need both the error's message _and_ code, such as unit testing and error handling, the `get_message` and `get_code` functions are available. These functions have the following signatures:

> **`get_message`**(_app_, _key_, _filler=None_)
>
> **`get_code`**(_app_, _key_)

Their operation is self-evident, where the `filler` argument works in the same way as it does in the basic `get` method.