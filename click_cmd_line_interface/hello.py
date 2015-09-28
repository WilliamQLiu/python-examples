import click


@click.command()  # allows you to just run 'hello' as a command on cli
@click.option('--string', default='World')  # pass in parameters
def cli():
    print 'Hello %s!' % string
    #print 'Hello World'