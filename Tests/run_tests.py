import Tests.domain as td
import Tests.CRUD as cr


def run_tests():
    cr.test_add_obj()
    cr.test_delete_obj()
    cr.test_modify_obj()
    cr.test_get_obj_data_list()
    cr.test_get_obj_IDs()
    td.test_obiect()
    cr.test_mutare()
    cr.test_add_description()
