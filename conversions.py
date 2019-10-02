#!user/bin/env python
# -*- coding: utf-8 -*-
#Temperature conversions module"""

#function converts from Celsius to Kelvin.
def convertCelsiusToKelvin(degrees):
    
    kelvin = degrees + 273.15
    return kelvin

#This function converts from Celsius to Fahrenheit.
def convertCelsiusToFahrenheit(degrees):
    
    Fahrenheit = (degrees * 1.8) + 32
    return Fahrenheit

#This function converts from Fahrenheit to Celsius.
def convertFahrenheitToCelsius(degrees):
    
    Celsius = (degrees - 32.0) * 5./9
    return Celsius

#This function converts from Fahrenheit to Kelvin.
def convertFahrenheitToKelvin(degrees):
    
    Kelvin = ((degrees + 459.67) * 5 / 9)
    return Kelvin

#This function converts from Kelvin to Celsius.
def convertKelvinToCelsius(degrees):
    
    Celsius = degrees - 273.15
    return Celsius

#This function converts from Kelvin to Fahrenheit.
def convertKelvinToFahrenheit(degrees):
    
    Fahrenheit_A = convertKelvinToCelsius(degrees)
    Fahrenheit = convertCelsiusToFahrenheit(Fahrenheit_A)
    return Fahrenheit

