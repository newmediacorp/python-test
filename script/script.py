import yaml
import lxml.html
import re

def value_list(x):
    if isinstance(x, dict):
        return set(x.values())
    elif isinstance(x, basestring):
        return [x]
    else:
        return None


stream = open("conf.yaml", 'r')
data = yaml.load(stream)

##print data['pages'].keys()
for page in data['pages'].keys():
    page_title = data['pages'][page]['title']
    page_description = data['pages'][page]['description']
    
    sections = data['pages'][page]['sections']
    sections_list = []
    print page
    #section portion
   
    for section in sections.keys(): 
        print section     
        tags = data['pages'][page]['sections'][section]
        print tags
        # Check if collection of html tags in section
        
        if isinstance(tags, list):            
            for tag in tags:
                print tag.keys()
                print tag.values()
                ui_element_content = tag.values()[0]
                print ui_element_content

        else: #if no html collection in sections portion
            print tags.keys()
            section_list_html = []
            for tag in tags.keys():                
                ui_element_content = data['pages'][page]['sections'][section][tag]
                print ui_element_content
                
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
                        # print section_html
                        # section_list_html.append(section_html)
                    section_list_html.append(section_html)
            print section_list_html

    with open('schemas/page.tpl','r') as pf:
        html = pf.read()
        html = re.sub('%%PAGE-TITLE%%',page_title,str(html))
        html = re.sub('%%PAGE-DESCRIPTION%%',page_description,str(html))
        html = re.sub('%%SECTIONS%%',''.join(section_list_html),str(html))
        print html

    with open(str(page)+'.html','w') as pf:
        pf.write(html)

        # print section_list_html

            # with open('schemas/page.tpl','r') as pf:5
            #     html = pf.read()
            #     html = re.sub('%%PAGE-TITLE%%',page_title,str(html))
            #     html = re.sub('%%PAGE-DESCRIPTION%%',page_description,str(html))
            #     html = re.sub('%%SECTIONS%%',section_html,str(html))
            #     print html



##                    print tag_html


 ##       """For Getting sections with relevant tags"""

        
##        print tags
##        for tag in tags.keys():
##            print tag
##            ui_element_content = data['pages'][page]['sections'][section][tag]
##            with open('schemas/'+str(tag)+'.tpl','r') as tf:
##                tag_html = tf.read()
##                if tag.lower() == 'p' or tag.lower() == 'h1':
##                    tag_html = re.sub('%%UI-ELEMENT-CONTENT%%',ui_element_content,str(tag_html))
####                    print tag_html
##                    """Replacing section Content """
##                    section_html = re.sub('%%SECTION-CONTENT%%',tag_html,str(section_html))
##                    
##                if tag.lower() == 'button':
##                    button_type = ui_element_content['type']
##                    button_css = ui_element_content['css']
##                    button_type = ui_element_content['name']
##                    tag_html = re.sub('%%BUTTON-TYPE%%',button_type,str(tag_html))
##                    tag_html = re.sub('%%BUTTON-CSS%%',button_type,str(tag_html))
##                    tag_html = re.sub('%%BUTTON-NAME%%',button_type,str(tag_html))
####                    print tag_html
##                    """Replacing section Content """
##                    section_html = re.sub('%%SECTION-CONTENT%%',tag_html,str(section_html))
##
##            sections_list.append(section_html)
####            print ui_element_content
##            
##
##        with open('schemas/page.tpl','r') as pf:
##            html = pf.read()
##            html = re.sub('%%PAGE-TITLE%%',page_title,str(html))
##            html = re.sub('%%PAGE-DESCRIPTION%%',page_description,str(html))
##            html = re.sub('%%SECTIONS%%',section_html,str(html))
##            print html
##
##            
##            with open('schemas/'+str(tag)+'.tpl','r') as tf:
##                tag_html = tf.read() 
##                tag_html = re.sub('%%UI-ELEMENT-CONTENT%%',ui_element_content,str(tag_html))
##                print tag_html
