from fabric.operations import local
result = local('ls', capture=True)
print "Content:/n%s" % (result, )
