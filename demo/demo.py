from pex.loading.loader import LoaderCsvPandas


loader = LoaderCsvPandas('tests/test_loader/test.csv')
print(loader.data)
