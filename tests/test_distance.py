from distance import *

def test_construction() -> None:
    d = Distance(5.0, KM)
    assert d.value == 5.0
    assert d.unit == KM

def test_repr() -> None:
    assert repr(Distance(5.0, KM)) == "Distance(5.0, km)"

def test_str() -> None:
    assert str(Distance(5.0, MM)) == "5.0 mm"

def test_value_as() -> None:
    d1 = Distance(5.0, MM)
    assert d1.value_as(MM) == 5.0
    assert d1.value_as(M) == 0.005
    assert d1.value_as(KM) == 0.000005

    d2 = Distance(3.0, KM)
    assert d2.value_as(MM) == 3000000.0
    assert d2.value_as(M) == 3000.0
    assert d2.value_as(KM) == 3.0

def test_value_m() -> None:
    assert Distance(5.0, MM).value_m == 0.005
    assert Distance(4.0, M).value_m == 4.0
    assert Distance(3.0, KM).value_m == 3000.0

def test_eq() -> None:
    assert Distance(5.0, M) == Distance(5.0, M)
    assert Distance(5.0, M) == Distance(5000.0, MM)
    assert Distance(5.0, M) == Distance(0.005, KM)

    assert Distance(5.0, M) != Distance(4.0, M)
    assert Distance(5.0, M) != Distance(5.0, MM)

def test_inequalities() -> None:
    # some distances in a non-decreasing order
    ordered_distances = [
        Distance(5.0, MM),
        Distance(0.005, M),
        Distance(10.0, MM),
        Distance(0.00001, KM),
        Distance(900.0, MM),
        Distance(1.0, M),
        Distance(50000, MM),
        Distance(0.1, KM),
        Distance(1000, M),
    ]
    for i in range(len(ordered_distances)):
        for j in range(len(ordered_distances)):
            l = ordered_distances[i]
            r = ordered_distances[j]
            if i == j:
                assert l == r
                assert not l < r
                assert l <= r
                assert not l > r
                assert l >= r
            elif i < j:
                assert l <= r
                assert not l > r
                assert (l < r) == (l != r)
                assert (l >= r) == (l == r)
            else:
                assert l >= r
                assert not l < r
                assert (l > r) == (l != r)
                assert (l <= r) == (l == r)

def test_additive_ops() -> None:
    assert Distance(5.0, M) + Distance(3.0, M) == Distance(8.0, M)
    assert Distance(5.0, MM) - Distance(3.0, MM) == Distance(2.0, MM)
    assert -Distance(5.0, KM) == Distance(-5.0, KM)
    assert +Distance(5.0, M) == Distance(5.0, M)

    # with mixed units, the one on the left wins
    assert Distance(5.0, M) + Distance(3.0, MM) == Distance(5.003, M)
    assert Distance(5.0, MM) - Distance(3.0, M) == Distance(-2995.0, MM)

def test_multiplicate_ops() -> None:
    assert Distance(5.0, MM) * 2 == Distance(10.0, MM)
    assert 3 * Distance(15.0, M) == Distance(45.0, M)
    assert Distance(3.0, KM) / 2 == Distance(1.5, KM)
