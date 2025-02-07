from app.utils import download_csv, load_data

def test_download_csv(mocker):
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, content=b"id,latitude,longitude\n1,40.7128,-74.0060"))
    download_csv()
    assert True  # If no exception is raised, the test passes

def test_load_data(mocker):
    mocker.patch("pandas.read_csv", return_value=[
        {"id": 1, "latitude": 40.7128, "longitude": -74.0060}
    ])
    data = load_data()
    assert len(data) > 0