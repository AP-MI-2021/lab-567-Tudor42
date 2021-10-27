import Tests.domain as td
import Tests.logic as tl
import Tests.CRUD as cr


def run_tests():
    cr.test_inventory()
    td.test_obiect()
    tl.test_mutare()
