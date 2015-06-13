"""Watson's base exception handling."""


class WatsonException(Exception):
    """Base watson exception

    To correctly use this class, inherit from it and define
    a `template` property.

    That `template` will be formated using the keyword arguments
    provided to the constructor.

    Example:
    ::
        class NotFound(WatsonException):
            '''The required object is not available in container.'''

            template = "The %(object)r was not found in %(container)s."


        raise NotFound(object=object_name, container=container)
    """

    template = "An unknown exception occurred."

    def __init__(self, message=None, **kwargs):
        message = message or self.template

        try:
            message = message % kwargs
        except (TypeError, KeyError):
            # Something went wrong during message formatting.
            # Probably kwargs doesn't match a variable in the message.
            message = ("Message: %(template)s. Extra or "
                       "missing info: %(kwargs)s" %
                       {"template": message, "kwargs": kwargs})

        super(WatsonException, self).__init__(message)
