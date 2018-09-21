# coding=utf-8
from lxml import etree
from util.rbQueue import RbQueue
import json,traceback
class Processor(object):

    def process(self,resp,info):
        # print(resp.request.url)
        # print(resp.text)
        html = None
        try:
            html = resp.text
        except:
            html = resp
        try:
            # with open(r'C:\Users\Ramboo\Desktop\2.html',"w",encoding='utf-8') as f:
            #     f.write(html)
            #     f.close()
            rule = json.loads(info['rule'])
            navi_list = rule['navi']
            selectors = etree.HTML(html)
            for navi in navi_list:
                content = selectors.xpath(navi['xpath'])[0].xpath('@href')[0]
                placeurl = navi['placeurl']
                task = {}
                if placeurl:
                    try:
                        task['url'] = eval(r''+placeurl.replace("{url}",content)+r'')
                    except:
                        task['url'] = eval(r'"'+placeurl.replace("{url}",content)+r'"')
                else:
                    task['url'] =  content
                print(task['url'])
                task['rule'] = rule['field']
                RbQueue.rb_queue.put(task)
        except Exception as a:
            print(a)



class FieldProcess(object):
    def process(self,resp,info):
        html = None
        try:
            html = resp.text
        except:
            html = resp
        try:
            # with open(r'C:\Users\Ramboo\Desktop\1.html',"w",encoding='utf-8') as f:
            #     f.write(html)
            #     f.close()
            selectors = etree.HTML(html)
            field_list = info
            result_list = []
            for field in field_list:
                content = selectors.xpath(field['xpath'])[0].xpath('string(.)')
                result = {}
                result['field'] = field['field']
                result['content'] = content
                result_list.append(result)
            print(result_list)
        except Exception as a:
            print(traceback.format_exc())

