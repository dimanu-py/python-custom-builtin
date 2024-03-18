from look_up import LookUp

class TestLookUp:

    def test_is_empty_when_created_with_no_source(self):
        look_up = LookUp()

        assert len(look_up) == 0

    def test_can_create_from_dictionary(self):
        look_up = LookUp({1: 'one', 2: 'two'})

        assert len(look_up) == 2

    def test_can_create_from_sequence(self):
        look_up = LookUp([(1, 'one'), (2, 'two')])

        assert len(look_up) == 2