# python 기본 라이브러리 urllib
# 
from indeed import get_indeed_jobs
from so import get_so_jobs
from file import make_file


indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
make_file(so_jobs + indeed_jobs)