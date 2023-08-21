import ftplib
from datetime import datetime, timedelta

def create_floder(session,path):
    try:
        session.cwd(path)
        print("found a floder")
    except:
        session.mkd(path)
        session.cwd(path)
        print("create a floder")
    return

def ftp_upload(project_path,file):

        hostname = '10.128.16.210'
        user = 'admin'
        pwd = '1234'

        now = datetime.now()
        date_file_name = f'{str(now.date())}_{str(now.time()).split(".")[0].replace(":","_")}'
        year,month,date = mfg_date()

        upload_path = f"/{project_path}/{year}/{month}/{date}/TYLASURF_{date_file_name}.csv"

        session = ftplib.FTP(hostname,user,pwd)
        create_floder(session,project_path)
        create_floder(session,str(year))
        create_floder(session,str(month))
        create_floder(session,str(date))

        try:
            session.storbinary(f'STOR {upload_path}', file)
        except Exception as e:
            print(f'info store-->{e}')
            return {"result":"ng",'code':e}
        file.close()
        session.quit()
        return {"result":"ok",'code':'-'}

def mfg_date():
    mfg_date = datetime.now() - timedelta(hours=7)
    year = mfg_date.year
    month = mfg_date.month
    date = mfg_date.day

    if len(str(year)) == 1:
        year = '0'+str(year)
    if len(str(month)) == 1:
        month = '0'+str(month)
    if len(str(date)) == 1:
        date = '0'+str(date)
    return year,month,date
