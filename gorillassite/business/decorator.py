__author__ = 'abreu'


def parameter(klass):
    """
    Decorator responsável por adicionar parametros a action quando decorado.

    Ex:

    @parameter
    class SendMessage:
        def execute():
            ...
            parametro1 = self.parameter['parametro1']
            parametro1 = self.parameter['parametro1']
            ...

    action = SendMessage()

    action.add_parameter(parametro1="1", parametro2="2")
    """

    class ParameterClass(klass):

        def __init__(self, *args, **kargs):
            super(ParameterClass, self).__init__(*args, **kargs)
            self.__parameter = dict()

        @property
        def parameter(self):
            return self.__parameter

        @parameter.setter
        def parameter(self, value):

            self.__parameter = value

        def add_parameter(self, **kwargs):

            self.__parameter.update(kwargs)

        def execute(self):

            if self.parameter is None or not self.parameter:
                raise ValueError('Parameter must be setted.')

            klass.execute(self)

    return ParameterClass


def result(klass):

    """
    Decorator responsável por adicionar resultados de retorno a action quando decorado.

    Ex:

    @result
    class SendMessage:
        def execute():
            ...
            action.add_result(resultado1="A")

    action = SendMessage()

    action.execute()

    resultado1 = action.result['resultado1']

    """

    class ResultClass(klass):

        def __init__(self, *args, **kargs):
            super(ResultClass, self).__init__(*args, **kargs)
            self.__result = dict()

        @property
        def result(self):
            return self.__result

        @result.setter
        def result(self, value):
            self.__result = value


        def add_result(self, **kwargs):
            self.__result.update(kwargs)

        def execute(self):

            klass.execute(self)

            if self.result is None or not self.result:
                raise ValueError('Result must be setted.')

    return ResultClass
