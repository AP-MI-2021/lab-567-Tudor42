import Tests.domain as td
import Tests.CRUD as cr
import Tests.functionalities as fn


def run_tests():
    cr.test_add_obj()
    cr.test_delete_obj()
    cr.test_modify_obj()
    cr.test_get_obj_data_list()
    cr.test_get_obj_IDs()
    td.test_obiect()
    fn.test_mutare()
    fn.test_add_description()
    fn.test_get_max_price_per_location()
    fn.test_sort_invetory_by_price()
