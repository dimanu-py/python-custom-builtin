import pytest

from look_up import LookUp


class TestLookUp:

    def test_is_empty_when_created_with_no_source(self):
        look_up = LookUp()

        assert len(look_up) == 0

    @pytest.mark.parametrize("source", [{1: "one", 2: "two"}, [(1, 'one'), (2, 'two')]])
    def test_can_create_from_mapping(self, source):
        look_up = LookUp(source)

        expected_size = len(source)

        assert len(look_up) == expected_size

    def test_can_be_accessed_by_key(self):
        look_up = LookUp([(1, "one"), (2, "two")])

        assert look_up[1] == "one"
        assert look_up[2] == "two"

    def test_new_items_can_not_be_added(self):
        look_up = LookUp([(1, "one"), (2, "two")])

        with pytest.raises(TypeError):
            look_up[3] = "three"

    def test_can_verify_if_key_is_present(self):
        look_up = LookUp([(1, "one"), (2, "two")])

        assert 1 in look_up
        assert 2 in look_up
        assert 3 not in look_up
