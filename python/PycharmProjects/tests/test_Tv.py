from unittest import TestCase
from television.tv import Tv


class TestTurnOnTv(TestCase):
    def test_that_tv_is_on(self):
        tv = Tv()
        tv.turn_on()
        self.assertTrue(tv.is_On)

    def test_that_tv_is_off(self):
        tv = Tv()
        tv.turn_off()
        self.assertFalse(tv.is_On)

    def test_to_get_chanel(self):
        tv1 = Tv()
        self.assertEqual(tv1.get_chanel(), 0)

    def test_to_set_chanel(self):
        tv1 = Tv()
        tv1.set_chanel(3)
        self.assertEqual(tv1.get_chanel(), 3)

    def test_to_get_volume(self):
        tv1 = Tv()
        self.assertEqual(tv1.get_volume(), 0)

    def test_to_set_volume(self):
        tv1 = Tv()
        self.assertEqual(tv1.get_volume(), 0)
    def test_to_increase_volume(self):
        tv1 =Tv()
        tv1.set_volume(19)
        self.assertEqual(tv1.get_volume(), 19)
        tv1.increase_volume()
        self.assertEqual(tv1.get_volume(), 20)

    def test_to_decrease_volume(self):
        tv1 = Tv()
        tv1.set_volume(19)
        self.assertEqual(tv1.get_volume(), 19)
        tv1.decrease_volume()
        self.assertEqual(tv1.get_volume(), 18)

    def test_to_set_mute(self):
        tv1 = Tv()
        tv1.set_volume(15)
        self.assertEqual(tv1.get_volume(), 15)

        tv1.get_mute()
        self.assertTrue(tv1.is_muted)
        self.assertEqual(tv1.get_volume(),0)

        tv1.get_mute()
        self.assertFalse(tv1.is_muted)
        self.assertEqual(tv1.get_volume(),15)

    def test_channel_up(self):
        tv1 = Tv()
        tv1.set_chanel(0)
        self.assertEqual(tv1.get_chanel(), 0)

        tv1.chanel_up()
        self.assertEqual(tv1.get_chanel(), 1)

    def test_channel_down(self):
        tv1 = Tv()
        tv1.set_chanel(2)
        self.assertEqual(tv1.get_chanel(), 2)

        tv1.chanel_down()
        self.assertEqual(tv1.get_chanel(), 1)











