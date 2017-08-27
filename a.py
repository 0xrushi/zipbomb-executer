from zipfile import ZipFile
import os
import threading

def unpack_zip(zipfile='', local_path=''):
        print ('dsds')
        fp = local_path+zipfile
        extract_path = fp.strip('.zip')+'/'
        print ('fp is :'+fp+'\nextract_path is :'+extract_path)
        parent_archive = ZipFile(fp)
        parent_archive.extractall(extract_path)
        nl = parent_archive.namelist()
        print('namelist is'+str(nl))
        parent_archive.close()
        for name in nl:
                try:
                        if name[-4:] == '.zip':
                                unpack_zip(zipfile=name, local_path=extract_path)
                                os.remove(extract_path+name)
                except:
                        print 'failed on', name
                        pass
        return 
    
path = unpack_zip('out.zip')
input('sd')
