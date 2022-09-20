import random


def define_id(pre_id: str = '',
              widget_type: str = '',
              extra: str = '',
              number_of_digits: int = 6) -> str:
    """
    Create a unique id for the widgets
    :param pre_id:
    :param extra:
    :param widget_type:
    :param number_of_digits:
    :return:
    """
    max_number = int('1' + '0' * number_of_digits)

    random_number = str(int(random.random() * max_number)).zfill(number_of_digits)

    return '{}{}{}{}'.format(pre_id, extra, widget_type, random_number)


def short_id(id_widget: str = '', number_of_digits: int = 6):
    return id_widget[:-number_of_digits]


def get_id_from_form_name(
        keys: list, form_name: str,
        widget_name: str,
        widget_type: str,
        property_: str):
    name = '{}{}{}'.format(form_name,
                           widget_name,
                           widget_type)
    id_item = ''
    for _k in keys:
        if name in _k:
            if _k.endswith('.{}'.format(property_)):
                id_item = _k

    return id_item
