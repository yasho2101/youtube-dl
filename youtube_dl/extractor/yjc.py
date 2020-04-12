from __future__ import unicode_literals

from .common import InfoExtractor


class yjcIE(InfoExtractor):
    _VALID_URL = r'(?:https?://)?(?:www\.)?yjc\.ir/fa/news/(?P<id>\w+)/*'

    _TESTS = [{
        'url': 'https://www.yjc.ir/fa/news/7297994/دانلود قسمت نهم سریال کامیون/ پخش شده از شبکه دوم سیما در تاریخ ۹ فروردین ۹۹',
        'info_dict': {
            'id': '7297994',
            'ext': 'mp4',
            'title': 'دانلود قسمت نهم سریال کامیون/ پخش شده از شبکه دوم سیما در تاریخ ۹ فروردین ۹۹',
        }

    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(
            url, video_id
        )

        title = self._html_search_regex(r'<title>(.+?)</title>', webpage, 'title')

        download_url = self._html_search_regex(

            r'((https:\/\/)cdn\.yjc\.ir/files/fa/news/[0-9]*/[0-9]*/[0-9]*/[0-9_]*\.mp4)',

            webpage, "download_url"
        )
        return {
            'id': video_id,
            'url': download_url,
            'title': title
        }
