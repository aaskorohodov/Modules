from Zeep.calculator.calculator_with_soap import SoapCalculator
from Zeep.calculator.gui import CalculatorApp


wsdl = 'http://dneonline.com/calculator.asmx?wsdl'
calculator_logic = SoapCalculator(wsdl)
application = CalculatorApp(calculator_logic)
