import unittest
import renamer


renamer.DEBUG = True


class RuleCase(unittest.TestCase):
    def base_assert(self, kwargs):
        for expect_value, in_value in kwargs.items():
            self.assertEqual(
                renamer.format_file_name(in_value),
                expect_value)

    def test_0(self):
        in_and_expect = {
            "HZGD-139": "hzgd-139.mp4",
            "ABP-992": "abp-992-c.mp4",
            "VRTM-089": "VRTM-089.HD.mp4",
            "LOVE-362": "[bai.du]love-362.mp4", }
        self.base_assert(in_and_expect)

    def test_1(self):
        in_and_expect = {
            "CARIB-1080": "baidu2048.com@062620-001-carib-1080p.mp4",
            "SSIS-334": "baidu800.com@SSIS-334.mp4",
            "PPPD-851": "PPPD-851(1080P)@18P2P.mp4",
            "ATID-403": "BAIDU2048.COM@ATID-403.mp4",
            "IPX-837": "baidu20s8.com@IPX-837.mp4",
            "SW-259": "SW-259@THMS.mkv", }
        self.base_assert(in_and_expect)

    def test_2(self):
        in_and_expect = {
            "GETS-100": "GETS-100_HD_CH.mp4", }
        self.base_assert(in_and_expect)

    def test_3(self):
        in_and_expect = {
            "BAD-268": "1hbad00268hhb.wmv",
            "STARS-145": "stars00145.mp4",
                         "STARS-174": "STARS174C.mp4", }
        self.base_assert(in_and_expect)

    def test_4(self):
        in_and_expect = {
            "FSDSS-077": "FSDSS-077.1080p.mp4",
                         "STARS-256": "STARS-256~baidu2p.com.mp4",
                         "MIAE-327": "MIAE-327~baidu224.com.mp4", }
        self.base_assert(in_and_expect)

    def test_5(self):
        in_and_expect = {
            "NDS-004": "574NDS-004 (填充填充-填充) (Uncensored Leaked) 填充填充 填充填充",
            "SNIS-850": "SNIS-850 Padding Padding 填充填充 [FHD][HEVC]", 
            "SDMF-002": "[JAVWE.com]SDMF002C.HD.1080P.ZhuixinYou.COM字幕"}
        self.base_assert(in_and_expect)


if __name__ == "__main__":
    unittest.main()
