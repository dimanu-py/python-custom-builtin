from look_up import LookUp

class TestLookUp:

    def test_is_empty_when_created_with_no_source(self):
        look_up = LookUp()

        assert len(look_up) == 0

