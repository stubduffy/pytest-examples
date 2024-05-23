import pytest
import requests
import datetime


def test_get_all_carts(fakestore_client):
    result = fakestore_client.get_all_carts()
    carts = result.json()
    assert len(carts) > 0
    assert result.status_code == requests.codes.ok


def test_get_specific_cart(fakestore_client):
    result = fakestore_client.get_cart(3)
    cart = result.json()
    assert cart["id"] == 3
    assert result.status_code == requests.codes.ok


def test_get_carts_with_limit(fakestore_client):
    result = fakestore_client.get_all_carts(params={"limit": 2})
    carts = result.json()
    assert len(carts) == 2
    assert result.status_code == requests.codes.ok


def test_get_carts_with_sort(fakestore_client):
    result = fakestore_client.get_all_carts(params={"sort": "desc"})
    carts = result.json()
    last_id = 100
    for cart in carts:
        this_id = cart["id"]
        assert this_id < last_id
        last_id = this_id
    assert result.status_code == requests.codes.ok


def test_get_carts_with_limit_and_sort(fakestore_client):
    result = fakestore_client.get_all_carts(params={"limit": 4, "sort": "desc"})
    carts = result.json()
    last_id = 100
    for cart in carts:
        this_id = cart["id"]
        assert this_id < last_id
        last_id = this_id
    assert len(carts) == 4
    assert result.status_code == requests.codes.ok


def test_get_carts_within_time_range(fakestore_client):
    start_date_str = "2020-03-01"
    end_date_str = "2020-03-31"
    result = fakestore_client.get_all_carts(
        params={"startdate": start_date_str, "enddate": end_date_str}
    )
    carts = result.json()
    start_date = datetime.date.fromisoformat(start_date_str)
    end_date = datetime.date.fromisoformat(end_date_str)
    for cart in carts:
        cart_date = datetime.date.fromisoformat(cart["date"][:10])
        assert cart_date >= start_date and cart_date < end_date
    assert result.status_code == requests.codes.ok


def test_get_carts_from_start_date(fakestore_client):
    start_date_str = "2020-03-01"
    result = fakestore_client.get_all_carts(params={"startdate": start_date_str})
    carts = result.json()
    start_date = datetime.date.fromisoformat(start_date_str)
    for cart in carts:
        cart_date = datetime.date.fromisoformat(cart["date"][:10])
        assert cart_date >= start_date
    assert result.status_code == requests.codes.ok


def test_get_carts_to_end_date(fakestore_client):
    end_date_str = "2020-03-31"
    result = fakestore_client.get_all_carts(params={"enddate": end_date_str})
    carts = result.json()
    end_date = datetime.date.fromisoformat(end_date_str)
    for cart in carts:
        cart_date = datetime.date.fromisoformat(cart["date"][:10])
        assert cart_date < end_date
    assert result.status_code == requests.codes.ok


def test_get_all_carts_for_a_user(fakestore_client):
    user_id = 1
    result = fakestore_client.get_user_carts(user_id=user_id)
    carts = result.json()
    for cart in carts:
        assert cart["userId"] == user_id
    assert result.status_code == requests.codes.ok


def test_add_cart(fakestore_client):
    payload = {
        "userId": 5,
        "date": "2020-02-03",
        "products": [{"productId": 5, "quantity": 1}, {"productId": 1, "quantity": 5}],
    }
    result = fakestore_client.add_cart(payload)
    cart = result.json()
    assert (
        result.status_code == requests.codes.ok
    )  # would expect this to be requests.codes.created in reality


def test_update_cart(fakestore_client):
    payload = {
        "userId": 100,
        "date": "2020-02-03",
        "products": [{"productId": 5, "quantity": 1}, {"productId": 1, "quantity": 5}],
    }
    result = fakestore_client.update_cart(3, payload)
    cart = result.json()
    assert result.status_code == requests.codes.ok


def test_delete_cart(fakestore_client):
    result = fakestore_client.delete_cart(3)
    cart = result.json()
    assert result.status_code == requests.codes.ok


@pytest.mark.xfail(reason="known issue; requesting a non-existent cart should fail")
def test_get_non_existing_cart(fakestore_client):
    result = fakestore_client.get_cart(10000)
    assert result.status_code == requests.codes.not_found


@pytest.mark.xfail(
    reason="known issue; an invalid sort should probably not go unnoticed"
)
def test_get_carts_with_invalid_sort(fakestore_client):
    result = fakestore_client.get_all_carts(params={"sort": "neither_asc_nor_desc"})
    assert result.status_code == requests.codes.bad_request


def test_get_carts_with_impossible_time_range(fakestore_client):
    result = fakestore_client.get_all_carts(
        params={"startdate": "2020-12-10", "enddate": "2019-10-10"}
    )
    assert len(result.json()) == 0
    assert result.status_code == requests.codes.ok


@pytest.mark.xfail(
    reason="known issue; an invalid limit should probably not go unnoticed"
)
def test_get_carts_with_invalid_limit(fakestore_client):
    result = fakestore_client.get_all_carts(params={"limit": "not_an_int"})
    assert result.status_code == requests.codes.bad_request


def test_get_carts_with_invalid_time_range(fakestore_client):
    result = fakestore_client.get_all_carts(params={"startdate": "not_a_date"})
    assert result.status_code == requests.codes.bad_request

@pytest.mark.xfail(
    reason="known issue; an invalid payload should probably not go unnoticed"
)
def test_add_cart_invalid_payload(fakestore_client):
    payload = {'unknown': 'field'}
    result = fakestore_client.add_cart(payload)
    cart = result.json()
    print(cart)
    assert (
        result.status_code == requests.codes.bad_request
    )  
