from src.manager import Manager
from src.models import Parameters


def test_financial_integrity_of_settlements():
    parameters = Parameters()
    manager = Manager(parameters)
    year = 2025
    month = 1

    for apartment_key in manager.apartments.keys():

        apartment_settlement = manager.get_settlement(apartment_key, year, month)
        if apartment_settlement is None or apartment_settlement.total_due_pln == 0:
            continue

        tenant_settlements = manager.create_tenants_settlements(apartment_settlement)
        if not tenant_settlements:
            continue

        total_tenants_due = sum(settlement.total_due_pln for settlement in tenant_settlements)
        assert total_tenants_due == apartment_settlement.total_due_pln


def test_missing_bills_alarm():
    from src.manager import Manager
    from src.models import Parameters
    
    manager = Manager(parameters=Parameters())
    year = 2099 
    month = 1
    apartment_key = 'A1'
    is_missing = manager.find_apartments_without_bills(apartment_key, year, month)

    assert is_missing is True