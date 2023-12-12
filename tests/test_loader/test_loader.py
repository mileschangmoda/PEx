class TestClass:
    def test_csv_loader(self):
        print('Test 1: test csv loader')
        from pex.loading.loader import LoaderCsvPandas
        loader = LoaderCsvPandas('tests/test_loader/test.csv')
        assert int(loader.data['col1'].iloc[0]) == 1