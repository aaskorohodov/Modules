from zeep import Client


wsdl = 'http://dneonline.com/calculator.asmx?wsdl'
client = Client(wsdl=wsdl)
client.service.Add(1, 2)
