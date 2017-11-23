#coding=utf-8
class Html_Outputer():
    def __init__(self):
        self.data=[]
    def collect_data(self,data):
        if data is None:
            return
        self.data.append(data)
    def output_html(self):
        fout=open('output.html','w')
        fout.write('<html><meta charset="utf-8">')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.data:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])


        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')