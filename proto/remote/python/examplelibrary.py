class RemoteTestLibrary:

    # Basic communication (and documenting keywords)

    def passing(self):
        """This keyword passes.

        See `Failing`, `Logging`, and `Returning` for other basic keywords.
        """
        pass
  
    def failing(self, message):
        """This keyword fails with provided `message`"""
        raise AssertionError(message)

    def logging(self, message, level='INFO'):
        """This keywords logs given `message` with given `level`

        Example:
        | Logging | Hello, world! |      |
        | Logging | Warning!!!    | WARN |
        """
        print '*%s* %s' % (level, message)

    def returning(self):
        """This keyword returns a string 'returned string'."""
        return 'returned string'

    # Arguments counts

    def no_arguments(self):
        return 'no arguments'

    def one_argument(self, arg):
        return arg

    def two_arguments(self, arg1, arg2):
        return '%s %s' % (arg1, arg2)

    def seven_arguments(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        return ' '.join((arg1, arg2, arg3, arg4, arg5, arg6, arg7))

    def arguments_with_default_values(self, arg1, arg2='2', arg3=3):
        return '%s %s %s' % (arg1, arg2, arg3)

    def variable_number_of_arguments(self, *args):
        return ' '.join(args)

    def required_defaults_and_varargs(self, req, default='world', *varargs):
        return ' '.join((req, default) + varargs)

    # Argument types

    def string_as_argument(self, arg):
        self._should_be_equal(arg, self.return_string())

    def unicode_string_as_argument(self, arg):
        self._should_be_equal(arg, self.return_unicode_string())

    def empty_string_as_argument(self, arg):
        self._should_be_equal(arg, '')

    def integer_as_argument(self, arg):
        self._should_be_equal(arg, self.return_integer())

    def negative_integer_as_argument(self, arg):
        self._should_be_equal(arg, self.return_negative_integer())

    def float_as_argument(self, arg):
        self._should_be_equal(arg, self.return_float())

    def negative_float_as_argument(self, arg):
        self._should_be_equal(arg, self.return_negative_float())

    def zero_as_argument(self, arg):
        self._should_be_equal(arg, 0)

    def boolean_true_as_argument(self, arg):
        self._should_be_equal(arg, True)

    def boolean_false_as_argument(self, arg):
        self._should_be_equal(arg, False)

    def none_as_argument(self, arg):
        self._should_be_equal(arg, '')

    def object_as_argument(self, arg):
        self._should_be_equal(arg, '<MyObject>')

    def list_as_argument(self, arg):
        self._should_be_equal(arg, self.return_list())

    def empty_list_as_argument(self, arg):
        self._should_be_equal(arg, [])

    def list_containing_none_as_argument(self, arg):
        self._should_be_equal(arg, [''])

    def list_containing_objects_as_argument(self, arg):
        self._should_be_equal(arg, ['<MyObject1>', '<MyObject2>'])

    def nested_list_as_argument(self, arg):
        exp = [ [True, False], [[1, '', '<MyObject>', {}]] ]
        self._should_be_equal(arg, exp)

    def dictionary_as_argument(self, arg):
        self._should_be_equal(arg, self.return_dictionary())

    def empty_dictionary_as_argument(self, arg):
        self._should_be_equal(arg, {})

    def dictionary_with_non_string_keys_as_argument(self, arg):
        self._should_be_equal(arg, {'1': 2, 'False': True})

    def dictionary_containing_none_as_argument(self, arg):
        self._should_be_equal(arg, {'As value': '', '': 'As key'})

    def dictionary_containing_objects_as_argument(self, arg):
        self._should_be_equal(arg, {'As value': '<MyObject1>', '<MyObject2>': 'As key'})

    def nested_dictionary_as_argument(self, arg):
        exp = { '1': {'True': False},
                '2': {'A': {'1': ''}, 'B': {'<MyObject>': {}}} }
        self._should_be_equal(arg, exp)

    def _should_be_equal(self, arg, exp):
        if arg != exp:
            raise AssertionError('%r != %r' % (arg, exp))

    # Return values

    def return_string(self):
        return 'Hello, world!'

    def return_unicode_string(self):
        return u'Hyv\xE4\xE4 \xFC\xF6t\xE4!'

    def return_empty_string(self):
        return ''

    def return_integer(self):
        return 42

    def return_negative_integer(self):
        return -1
  
    def return_float(self):
        return 3.14
  
    def return_negative_float(self):
        return -0.5

    def return_zero(self):
        return 0
  
    def return_boolean_true(self):
        return True

    def return_boolean_false(self):
        return False

    def return_nothing(self):
        pass

    def return_object(self):
        return MyObject()

    def return_list(self):
        return ['One', -2, False]

    def return_empty_list(self):
        return []

    def return_list_containing_none(self):
        return [None]

    def return_list_containing_objects(self):
        return [MyObject(1), MyObject(2)]

    def return_nested_list(self):
        return [ [True, False], [[1, None, MyObject(), {}]] ]

    def return_tuple(self):
        return (1, 'two', True)

    def return_empty_tuple(self):
        return ()

    def return_nested_tuple(self):
        return ( (True, False), [(1, None, MyObject(), {})] )

    def return_dictionary(self):
        return {'one': 1, 'true': True}

    def return_empty_dictionary(self):
        return {}

    def return_dictionary_with_non_string_keys(self):
        return {1: 2, False: True}

    def return_dictionary_containing_none(self):
        return {'As value': None, None: 'As key'}

    def return_dictionary_containing_objects(self):
        return {'As value': MyObject(1), MyObject(2): 'As key'}

    def return_nested_dictionary(self):
        return { 1: {True: False},
                 2: {'A': {1: None}, 'B': {MyObject(): {}}} }

    # Not keywords

    def _private_method(self):
        pass

    def __private_method(self):
        pass

    attribute = 'Not a keyword'


class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index


if __name__ == '__main__':
    import sys
    from robotremoteserver import RobotRemoteServer

    RobotRemoteServer(RemoteTestLibrary(), *sys.argv[1:])
