class TestClass:
    def test_csv_loader(self):
        from pex.loading.loader import Loader, LoaderCsvPandas

        print('Test 1: test csv loader')
        from pex.loading.loader import Loader, LoaderCsvPandas
        loader: Loader = LoaderCsvPandas('tests/test_loader/test.csv')
        assert int(loader.data['col1'].iloc[0]) == 1


if __name__ == '__main__':
    x = TestClass()
    x.test_csv_loader()
