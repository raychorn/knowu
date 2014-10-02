import os, sys

import argparse

from utils import *

if (__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL template in the form of: %s" % (__url__), type=str, nargs='?', default=__url__)
    args = parser.parse_args()
    
    if (args.url):
        __url__ = args.url

    fpath = os.path.abspath(os.sep.join(['.','data']))
    if (os.path.exists(fpath)):
        files = os.listdir(fpath)
        for f in files:
            fn = os.sep.join([fpath,f])
            if (os.path.exists(fn)):
                os.remove(fn)
        os.removedirs(fpath)
    if (not os.path.exists(fpath)):
        os.mkdir(fpath)
    
    def __main__():
        for state in states:
            __data__ = fetch_data_for(state)
            __json__ = json.dumps(__data__, indent=4)
            fname = os.sep.join([fpath,'%s.json' % (state)])
            print >> sys.stdout, 'Saving data in "%s".' % (fname)
            fOut = open(fname,'w')
            try:
                print >>fOut, __json__
            except:
                pass
            fOut.flush()
            fOut.close()
            print >> sys.stdout, '\n'
    
    __main__()
    