import requests
import csv

url = 'https://api.github.com/users/defunkt'

r = requests.get(url)

repo_dic = r.json()

outfile_path = '/Users/Gerella/PycharmProjects/Task1/test1.csv'

writer = csv.writer(open(outfile_path, 'w'))

headers = ['id','name','login','avatar_url', 'url','email', 'location','followers','following','created_at','updated_at']

writer.writerow(headers)


# for row in writer:   (if there is more than one respon
writer.writerow([
        repo_dic['id'], repo_dic['name'], repo_dic['login'], repo_dic['avatar_url'],
        repo_dic['url'],repo_dic['email'],repo_dic['location'],repo_dic['followers'],repo_dic['following'],
        repo_dic['created_at'],repo_dic['updated_at']
    ])


