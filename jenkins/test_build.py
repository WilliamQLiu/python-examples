from jenkinsapi.jenkins import Jenkins


jenkins = Jenkins('http://localhost:8078', username='admin', password='admin')
job_name = 'django_unit_tests'
job = jenkins[job_name]

queue_item = job.invoke()
print('Building ... ')

queue_item.block_until_complete()

build = job.get_last_completed_build()

print('Last build number was: ', build.get_number())
print('Last build result was: ', build.get_status())
#print('Last build based on branch: ', build.get_revision_branch())

