#!/usr/bin/env python

# import pyseabreeze library
import seabreeze
seabreeze.use("pyseabreeze")
import seabreeze.spectrometers as sb

import rospy
from datetime import datetime

from ocean_optics_driver.srv import *

def calibration_scan_callback(req):
	time_now = datetime.now()

	filename = time_now.strftime("./ocean_optics_output_data/calibration_data/calibration_data_%m-%d_%H:%M:%S.txt")

	devices = sb.list_devices()

	if (len(devices) == 0):
		print "No Ocean Optics devices found!"
		return False

	with open(filename, 'w') as f:
		for i in range(len(devices)):
			spec = sb.Spectrometer(devices[i])
			spec.integration_time_micros(12000)
			wavelengths = spec.wavelengths()
			intensities = spec.intensities()
			for j in range(len(wavelengths)):
				f.write("%f, %f\n" % wavelenths[j], intensities[j])

	return True

def reflectance_scan_callback(req):
	time_now = datetime.now()

	filename = time_now.strftime("./ocean_optics_output_data/sample_data/sample_data_%m-%d_%H:%M:%S.txt")

	devices = sb.list_devices()

	if (len(devices) == 0):
		print "No Ocean Optics devices found!"
		return False

	with open(filename, 'w') as f:
		for i in range(len(devices)):
			spec = sb.Spectrometer(devices[i])
			spec.integration_time_micros(12000)
			wavelengths = spec.wavelengths()
			intensities = spec.intensities()
			for j in range(len(wavelengths)):
				f.write("%f, %f\n" % wavelenths[j], intensities[j])

	return True

def ocean_optics_specs_server():

    rospy.init_node('ocean_optics_specs_server')

    calibration_service = rospy.Service('ocean_optics_spec_calibration_scan', OceanOptics, calibration_scan_callback)
    reflectance_service = rospy.Service('ocean_optics_spec_reflectance_scan', OceanOptics, reflectance_scan_callback)

    print "ocean_optics_specs_server ready to perform scans..."
    print "\tIt is recommended to first run a calibration scan.\n"
    
    # show detected devices
    print "Detected devices: "
    print sb.list_devices()

    rospy.spin()

if __name__ == "__main__":
    ocean_optics_specs_server()