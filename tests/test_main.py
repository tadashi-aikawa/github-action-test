from src.main import owl_sum


class TestSum:
    def test_normal(self):
        assert 5 == owl_sum(2, 3)
