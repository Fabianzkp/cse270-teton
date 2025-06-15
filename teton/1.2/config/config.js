const LAT = "43.8866";
const LON = "-111.6777";
const APIKEY = "791967606da3a7ba920b6566d902c6ec";

const WEATHER_URL_STUB = "./data/weather.json";
const WEATHER_URL_PROD = `https://api.openweathermap.org/data/2.5/weather?q=Teton,Idaho,US&appid=791967606da3a7ba920b6566d902c6ec&units=imperial`;

const apiURL = WEATHER_URL_PROD;

const DIRECTORY_DATA_URL_PROD = "<PRODUCTION_URL_HERE>";
const DIRECTORY_DATA_URL_STUB = "./data/business.json";
const DIRECTORY_DATA_URL_TEST = "http://127.0.0.1:8000/data/all";

const businessDataUrl = DIRECTORY_DATA_URL_TEST;
