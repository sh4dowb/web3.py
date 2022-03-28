import pytest


def test_resolve(ens):
    acct = ens.w3.eth.accounts[2]
    ens.setup_address('tester.eth', acct)

    assert ens.resolve('tester.eth') == acct

    # clean up
    ens.setup_address('tester.eth', None)


@pytest.mark.parametrize('subdomain', ('sub1', 'sub2', 'rändöm', '🌈rainbow', 'faß'))
def test_wildcard_resolution_with_extended_resolver_for_subdomains(ens, subdomain):
    # validate subdomains of `extended-resolver.eth` by asserting it returns the specified
    # hard-coded address from `tests/test_contracts/ExtendedResolver.sol` which requires
    # certain conditions to be met that are specific to subdomains only
    resolved_child_address = ens.resolve(f'{subdomain}.extended-resolver.eth')
    assert resolved_child_address == '0x000000000000000000000000000000000000dEaD'


def test_wildcard_resolution_with_extended_resolver_for_parent_ens_domain(ens):
    # validate `extended-resolver.eth` by asserting it returns the specified hard-coded address from
    # `tests/test_contracts/ExtendedResolver.sol` which requires a specific condition to be
    # met for the parent domain `extended-resolver.eth`
    resolved_parent_address = ens.resolve('extended-resolver.eth')
    assert resolved_parent_address == '0x000000000000000000000000000000000000bEEF'