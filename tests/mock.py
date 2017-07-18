from unittest.mock import Mock


__author__ = 'abreu'


def generic_action():

    return Mock()


def generic_action_boom():

    action = Mock()

    action.execute = Mock(side_effect=Exception('Boom!'))

    return action
