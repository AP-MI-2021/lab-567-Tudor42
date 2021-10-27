import Tests.domain as td
import Tests.logic as tl
import Tests.CRUD as cr


def run_tests():
    cr.test_add_obj()
    cr.test_delete_obj()
    cr.test_modify_obj()
    td.test_obiect()
    tl.test_mutare()
