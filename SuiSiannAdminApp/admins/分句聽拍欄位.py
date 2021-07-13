from django.utils.html import format_html
from itertools import zip_longest
from django.conf import settings

kuiku = getattr(settings, 'KUI_KU', 3)


class 分句欄位():
    音檔html = '''<div>{}：<audio controls>
                <source src='{}'>
                Your browser does not support the audio element.</audio></div>'''

    def 分句聽拍(self, obj):
        return self.分句組合(
            obj.漢字.split('\n'),
            obj.羅馬字含口語調.split('\n'),
            obj.kaldi切音時間網址(),
        )

    def 分句組合(self, 漢陣列, 羅陣列, 音陣列):
        pan = []
        kiatko = []
        han = []
        lo = []
        im = []
        for 幾, (漢, 羅, 音檔網址) in enumerate(zip_longest(
            漢陣列, 羅陣列, 音陣列,
        ), start=1):
            if 漢 is not None:
                han.append(漢)
            else:
                han.append('')
            if 羅 is not None:
                lo.append(羅)
            else:
                lo.append('')
            if 音檔網址 is not None:
                if 漢 is not None or 羅 is not None:
                    im.append(幾)
                else:
                    im.append('{} 音檔較tsē句，請重切'.format(幾))
                im.append(音檔網址)
            else:
                im.append('{} 音檔較少句，請重切'.format(幾))
                im.append('')

            if len(han) == kuiku:
                pan.append(self.一區html(kuiku))
                kiatko.append('\n'.join(han))
                kiatko.append('\n'.join(lo))
                kiatko.extend(im)
                han = []
                lo = []
                im = []
        if han:
            pan.append(self.一區html(len(han)))
            kiatko.append('\n'.join(han))
            kiatko.append('\n'.join(lo))
            kiatko.extend(im)
        return format_html(''.join(pan), *kiatko)

    def 一區html(self, kui):
        return (
            '''<div>
        <textarea cols=120 rows=3 name='han'>{}</textarea>
        <textarea cols=120 rows=4 name='lo' class='phiaua'>{}</textarea>'''
            + (self.音檔html * kui) +
            '</div>'
        )
