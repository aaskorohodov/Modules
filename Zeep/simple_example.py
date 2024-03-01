"""
This is an example of using Zeep to query weather forcast.
API specification:

    https://graphical.weather.gov/xml/ - describes how to use thi resource
    https://graphical.weather.gov/xml/docs/elementInputNames.php - describes required fields for weather_parameters
    https://graphical.weather.gov/xml/SOAP_server/ndfdXML.htm - wev-SOAP requester for the same service
"""
from datetime import datetime, timedelta
from pprint import pprint
from typing import Optional
from zeep import Client
from xml.etree import ElementTree


class SOARequester:
    """Can make a SOAP request and print its result

    Attributes:
        client: Zeep's client to make SOAP-requests
        latitude: Latitude of the place, to get forcast from
        longitude: Longitude of the place, to get forcast from
        product_type: No idea what this is. Got from WSDL-requirements
        start_time: Forcast from
        end_time: Forcast up to
        unit_type: e for US, m for metrics
        weather_parameters: Parameters to receive in the response
        xml_response: Response as a string"""

    def __init__(self, wsdl_url: str):
        """Init

        Attributes:
            wsdl_url: Url from where to get WSDL"""

        self.client = Client(wsdl_url)

        self.latitude = 40.785                                  # NYC, ~Central park
        self.longitude = -73.965                                # NYC, ~Central park
        self.product_type = "time-series"
        self.start_time, self.end_time = self._get_time_strings()
        self.unit_type = "m"                                    # m for 'Metric' (meters, Celsius...)
        self.weather_parameters = self._make_weather_params()

        self.xml_response: Optional[str] = None

    def _get_time_strings(self):
        """Makes 2 strings representing 2 dates: today and 2 days later

        Returns:
            2 string in this format 2024-03-01T00:00:00"""

        # Get current date and time
        current_date = datetime.now().strftime("%Y-%m-%dT00:00:00")

        # Get date and time for two days from now
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT00:00:00")

        return current_date, future_date

    def _make_weather_params(self) -> dict[str, bool]:
        """Makes parameters for SOAP

        Returns:
            dict with 'parameter_name': True or False (need ot not)"""

        weather_parameters = {
            'maxt': True,
            'mint': True,
            'temp': False,
            'dew': False,
            'appt': False,
            'pop12': False,
            'qpf': False,
            'snow': False,
            'sky': False,
            'rh': False,
            'wspd': False,
            'wdir': False,
            'wx': False,
            'icons': False,
            'waveh': False,
            'incw34': False,
            'incw50': False,
            'incw64': False,
            'cumw34': False,
            'cumw50': False,
            'cumw64': False,
            'wgust': False,
            'critfireo': False,
            'dryfireo': False,
            'conhazo': False,
            'ptornado': False,
            'phail': False,
            'ptstmwinds': False,
            'pxtornado': False,
            'pxhail': False,
            'pxtstmwinds': False,
            'ptotsvrtstm': False,
            'pxtotsvrtstm': False,
            'tmpabv14d': False,
            'tmpblw14d': False,
            'tmpabv30d': False,
            'tmpblw30d': False,
            'tmpabv90d': False,
            'tmpblw90d': False,
            'prcpabv14d': False,
            'prcpblw14d': False,
            'prcpabv30d': False,
            'prcpblw30d': False,
            'prcpabv90d': False,
            'prcpblw90d': False,
            'precipa_r': False,
            'sky_r': False,
            'td_r': False,
            'temp_r': False,
            'wdir_r': False,
            'wspd_r': False,
            'wwa': False,
            'iceaccum': False,
            'maxrh': False,
            'minrh': False
        }

        return weather_parameters

    def make_soap_request(self) -> None:
        """Makes SOAP-request and saves result"""

        response = self.client.service.NDFDgen(
            self.latitude,
            self.longitude,
            self.product_type,
            self.start_time,
            self.end_time,
            self.unit_type,
            self.weather_parameters
        )
        self.xml_response = response

    def _extract_data_from_response(self) -> dict[str, any]:
        """Extracts data from SOAP-response and saves it into dict"""

        result = {}

        root = ElementTree.fromstring(self.xml_response)

        max_temperature = root.find(".//temperature[@type='maximum']/value").text
        result['Max Temperature:'] = max_temperature

        min_temperature = root.find(".//temperature[@type='minimum']/value").text
        result['Min Temperature:'] = min_temperature

        hourly_temperature_values = [value.text for value in root.findall(".//temperature[@type='hourly']/value")]
        result['Hourly Temperature Values:'] = hourly_temperature_values

        precipitation_values = [value.text for value in root.findall(".//precipitation[@type='liquid']/value")]
        result['Precipitation Values:'] = precipitation_values

        wind_speed_values = [value.text for value in root.findall(".//wind-speed[@type='sustained']/value")]
        result['Wind Speed Values:'] = wind_speed_values

        wind_direction_values = [value.text for value in root.findall(".//direction[@type='wind']/value")]
        result['Wind Direction Values:'] = wind_direction_values

        return result

    def print_results(self) -> None:
        """Extracts data and prints results from saved SOAP"""

        data = self._extract_data_from_response()
        for key, value in data.items():
            print(key, value)

    def print_raw_response(self):
        """Prints raw-response"""

        pprint(self.xml_response)


wsdl = "https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl"
soap_requester = SOARequester(wsdl)
soap_requester.make_soap_request()
soap_requester.print_raw_response()
soap_requester.print_results()
