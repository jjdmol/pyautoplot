import unittest
from pyautoplot.angle import *


class AngleTest(unittest.TestCase):

    def test_init_adjust(self):
        self.assertAlmostEquals(Angle(-0.2, 1.0, 3.0).value, 1.8)
        self.assertAlmostEquals(Angle(0.3, -2.0, 5.0).value, 0.3)
        self.assertAlmostEquals(Angle(5.2, -2.0, 5.0).value, -1.8)
        self.assertAlmostEquals(Angle(3.0, 1.0, 3.0).value, 1.0)
        self.assertAlmostEquals(Angle(3.0, 1.0, 3.0,True).value, 3.0)
        self.assertAlmostEquals(Angle(1.0,1.0, 3.0).value, 1.0)
        pass
    
    def test_set_rad(self):
        alpha = Angle(0.0,1.0,3.0)
        self.assertAlmostEquals(alpha.value, 2.0)
        self.assertAlmostEquals(alpha.set_rad(-0.2), 1.8)
        pass

    def test_set_hms(self):
        self.assertEquals(Angle((10, 20, 30.5),type='hms').as_hms(2), '10:20:30.50')
        pass

    def test_set_sdms(self):
        self.assertEquals(Angle(('+', 10, 20, 30.5),type='sdms').as_sdms(2), '+010:20:30.50')
        self.assertEquals(Angle(('-', 10, 20, 30.5),-pi/2,pi/2,type='sdms').as_sdms(2), '-10:20:30.50')
        pass

    def test_as_hms(self):
        self.assertEquals(Angle(-4*pi/36.0).as_hms(), '22:40:00')
        self.assertEquals(Angle(-4*pi/36.0,-pi,pi).as_hms(), '-01:20:00')
        self.assertEquals(Angle(-pi/12.0 -pi/12.0/3600.0 +0.9999996/3600.0/12.0*pi).as_hms(3), '23:00:00.000') 
        self.assertEquals(Angle(-pi/12.0 -pi/12.0/3600.0 +0.9999996/3600.0/12.0*pi).as_hms(7), '22:59:59.9999996') 
        self.assertEquals(Angle(-pi/4/45.0/360000.0).as_hms(1), '00:00:00.0')
        pass


    def test_adjust(self):
        self.assertAlmostEquals(Angle(2.0, 1.0, 3.0).adjust(-0.2), 1.8)
        self.assertAlmostEquals(Angle(0.0, -2.0, 5.0).adjust(0.3), 0.3)
        self.assertAlmostEquals(Angle(4.8, -2.0, 5.0).adjust(5.2), -1.8)
        pass

    def test_as_sdms(self):
        self.assertEquals(Angle(pi/40.0,-pi/2,pi/2).as_sdms(),'+04:30:00')
        self.assertEquals(Angle(pi/40.0).as_sdms(), '+004:30:00')
        self.assertEquals(Angle(-pi/4.0).as_sdms(2), '+315:00:00.00')
        self.assertEquals(Angle(-pi/4/45.0/360000.0).as_sdms(1), '+000:00:00.0')
        self.assertEquals(Angle(-pi/4/3600000,-pi/2,pi/2).as_sdms(2), '-00:00:00.05')
        pass



class RighAscensionTest(unittest.TestCase):
    def test_right_ascension(self):
        ra=RightAscension(3*pi/2.0)
        self.assertAlmostEquals(ra.lower_bound, 0.0)
        self.assertAlmostEquals(ra.upper_bound, 2*pi)
        self.assertAlmostEquals(ra.include_upper_bound, False)
        self.assertAlmostEquals(ra.cyclical, True)
        self.assertEquals(ra.as_hms(), '18:00:00')
        pass

    pass

class DeclinationTest(unittest.TestCase):
    def test_declination(self):
        dec=Declination(3*pi/2.0)
        self.assertAlmostEquals(dec.lower_bound, -pi/2.0)
        self.assertAlmostEquals(dec.upper_bound, +pi/2.0)
        self.assertAlmostEquals(dec.include_upper_bound, True)
        self.assertAlmostEquals(dec.cyclical, False)
        self.assertEquals(dec.as_sdms(), '+90:00:00')
        pass
    pass

class HourAngleTest(unittest.TestCase):
    def test_hour_angle(self):
        ha=HourAngle(3*pi/2.0)
        self.assertAlmostEquals(ha.lower_bound, -pi)
        self.assertAlmostEquals(ha.upper_bound, +pi)
        self.assertAlmostEquals(ha.include_upper_bound, False)
        self.assertAlmostEquals(ha.cyclical, True)
        self.assertEquals(ha.as_hms(), '-06:00:00')
        pass
    pass

class EquatorialDirectionTest(unittest.TestCase):
    
    def test__str__(self):
        self.assertEquals(str(EquatorialDirection(RightAscension(6.12348768),
                                                  Declination(1.024))), 'J2000 RA: 23:23:24, DEC: +58:40:15')
        self.assertEquals(str(EquatorialDirection(RightAscension(6.12348768+pi),
                                                  Declination(1.024),
                                                  'B1950')), 'B1950 RA: 11:23:24, DEC: +58:40:15')
        pass
    
    pass



#
#  M A I N 
#

if __name__ == '__main__':
    unittest.main()

#
#  E O F
#
