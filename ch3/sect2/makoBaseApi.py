# coding=utf-8

from mako.template import Template

if __name__ == '__main__':
    template = Template('Hello ${name}!')
    str = template.render(name='Xiao Ming')
    print str

    templateHtml = Template(filename='./hello.mako').render(name='Li Shi')
    print templateHtml

    templateCache = Template(filename='./hello.mako', module_directory='/tmp/mako_cache').render(name='Zhang San')
    print templateCache
