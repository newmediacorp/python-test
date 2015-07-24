import yaml
import lxml.html
import re
import os

def value_list(x):
    if isinstance(x, dict):
        return set(x.values())
    elif isinstance(x, basestring):
        return [x]
    else:
        return None


stream = open("conf.yaml", 'r')
data = yaml.load(stream)

for page, v in data['pages'].items():
    page_title = data['pages'][page]['title']
    page_description = data['pages'][page]['description']
    
    sections = data['pages'][page]['sections']
    sections_list = []

    #section portion
    for section, v in sections.items():    
        tags = data['pages'][page]['sections'][section]
        
        # Check if collection of html tags in section        
        if isinstance(tags, list):            
            for tag in tags:
                ui_element_content = tag.values()[0]                

        else: #if no html collection in sections portion
            section_list_html = []
            for tag, v in tags.items():                
                ui_element_content = data['pages'][page]['sections'][section][tag]
                
                #opening sections portion
                with open('schemas/section.tpl','r') as sf:
                    section_html = sf.read()
                    section_html = re.sub('%%SECTION-NAME%%',section,str(section_html))

                #opening relevant .tpl file
                with open('schemas/'+str(tag)+'.tpl','r') as tf:
                    tag_html = tf.read()
                    if tag.lower() == 'p' or tag.lower() == 'h1':
                        tag_html = re.sub('%%UI-ELEMENT-CONTENT%%',ui_element_content,str(tag_html))

                        #"""Replacing section Content """
                        section_html = re.sub('%%SECTION-CONTENT%%',tag_html,str(section_html))
                        # print section_html                        
                        
                    if tag.lower() == 'button':
                        button_type = ui_element_content['type']
                        button_css = ui_element_content['css']
                        button_type = ui_element_content['name']
                        tag_html = re.sub('%%BUTTON-TYPE%%',button_type,str(tag_html))
                        tag_html = re.sub('%%BUTTON-CSS%%',button_type,str(tag_html))
                        tag_html = re.sub('%%BUTTON-NAME%%',button_type,str(tag_html))
                        #"""Replacing section Content """
                        section_html = re.sub('%%SECTION-CONTENT%%',tag_html,str(section_html))
                        
                        
                    section_list_html.append(section_html)
            #print section_list_html

    with open('schemas/page.tpl','r') as pf:
        html = pf.read()
        html = re.sub('%%PAGE-TITLE%%',page_title,str(html))
        html = re.sub('%%PAGE-DESCRIPTION%%',page_description,str(html))
        html = re.sub('%%SECTIONS%%',''.join(section_list_html),str(html))
        print html

    directory = 'html'
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, str(page)+'.html'),'w') as pf:
        pf.write(html)


