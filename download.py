import urllib.request

# URLs for the zip files
links = [
    'https://nihcc.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz',
    'https://nihcc.box.com/shared/static/i28rlmbvmfjbl8p2n3ril0pptcmcu9d1.gz',
    'https://nihcc.box.com/shared/static/f1t00wrtdk94satdfb9olcolqx20z2jp.gz',
    'https://nihcc.box.com/shared/static/0aowwzs5lhjrceb3qp67ahp0rd1l1etg.gz',
    'https://nihcc.box.com/shared/static/v5e3goj22zr6h8tzualxfsqlqaygfbsn.gz',
    'https://nihcc.box.com/shared/static/asi7ikud9jwnkrnkj99jnpfkjdes7l6l.gz',
    'https://nihcc.box.com/shared/static/jn1b4mw4n6lnh74ovmcjb8y48h8xj07n.gz',
    'https://nihcc.box.com/shared/static/tvpxmn7qyrgl0w8wfh9kqfjskv6nmm1j.gz',
    'https://nihcc.box.com/shared/static/upyy3ml7qdumlgk2rfcvlb9k6gvqq2pj.gz',
    'https://nihcc.box.com/shared/static/l6nilvfa9cg3s28tqv1qc1olm3gnz54p.gz',
    'https://nihcc.box.com/shared/static/hhq8fkdgvcari67vfhs7ppg2w6ni4jze.gz',
    'https://nihcc.box.com/shared/static/ioqwiy20ihqwyr8pf4c24eazhh281pbu.gz'
]

dict_complete = {'pass':[], 'fail':links}
terminate = False
while(True):
    for idx, link in enumerate(links):

        link_pass = ""
        for idx_f, link_fail in enumerate(dict_complete['fail']):
            if(link in link_fail):
                fn = 'images_%02d.tar.gz' % (idx+1)
                try: urllib.request.urlretrieve(link, fn)
                except: break
                else: link_pass = link_fail

        if(len(link_pass) > 0):
            print('Fail   : images_%02d.tar.gz' % (idx+1))
            continue
        else:
            try: dict_complete['fail'].remove(link_pass)
            except: terminate = True
            dict_complete['pass'].append(link_pass)
            print('Sucess : images_%02d.tar.gz' % (idx+1))

    if(len(dict_complete['pass']) == len(links) or terminate): break

print("Download complete. Please check the checksums")
