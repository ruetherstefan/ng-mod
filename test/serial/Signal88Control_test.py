from src.serial.Signal88Control import Signal88Control


def test_decode_bytes_to_boolarray_0():
    assert [False, False, False, False, False, False, False, False]\
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x00'))


def test_decode_bytes_to_boolarray_1():
    assert [False, False, False, False, False, False, False, True]\
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x01'))


def test_decode_bytes_to_boolarray_2():
    assert [False, False, False, False, False, False, True, False]\
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x02'))


def test_decode_bytes_to_boolarray_4():
    assert [False, False, False, False, False, True, False, False]\
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x04'))


def test_decode_bytes_to_boolarray_8():
    assert [False, False, False, False, True, False, False, False] \
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x08'))


def test_decode_bytes_to_boolarray_16():
    assert [False, False, False, True, False, False, False, False] \
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x10'))


def test_decode_bytes_to_boolarray_32():
    assert [False, False, True, False, False, False, False, False] \
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x20'))


def test_decode_bytes_to_boolarray_64():
    assert [False, True, False, False, False, False, False, False] \
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x40'))


def test_decode_bytes_to_boolarray_128():
    assert [True, False, False, False, False, False, False, False] \
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\x80'))


def test_decode_bytes_to_boolarray_255():
    assert [True, True, True, True, True, True, True, True] \
        .__eq__(Signal88Control.decode_bytes_to_boolarray(b'\xFF'))
