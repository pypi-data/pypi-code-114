# imports - standard imports
import os
import sys

# imports - third party imports
import click


@click.command('start', help="Start Neo development processes")
@click.option('--no-dev', is_flag=True, default=False)
@click.option('--no-prefix', is_flag=True, default=False, help="Hide process name from neocli start log")
@click.option('--concurrency', '-c', type=str)
@click.option('--procfile', '-p', type=str)
@click.option('--man', '-m', help="Process Manager of your choice ;)")
def start(no_dev, concurrency, procfile, no_prefix, man):
	from neocli.utils.system import start
	start(no_dev=no_dev, concurrency=concurrency, procfile=procfile, no_prefix=no_prefix, procman=man)


@click.command('restart', help="Restart supervisor processes or systemd units")
@click.option('--web', is_flag=True, default=False)
@click.option('--supervisor', is_flag=True, default=False)
@click.option('--systemd', is_flag=True, default=False)
def restart(web, supervisor, systemd):
	from neocli.neocli import NeoCLI
	NeoCLI(".").reload(web, supervisor, systemd)


@click.command('set-nginx-port', help="Set NGINX port for site")
@click.argument('site')
@click.argument('port', type=int)
def set_nginx_port(site, port):
	from neocli.config.site_config import set_nginx_port
	set_nginx_port(site, port)


@click.command('set-ssl-certificate', help="Set SSL certificate path for site")
@click.argument('site')
@click.argument('ssl-certificate-path')
def set_ssl_certificate(site, ssl_certificate_path):
	from neocli.config.site_config import set_ssl_certificate
	set_ssl_certificate(site, ssl_certificate_path)


@click.command('set-ssl-key', help="Set SSL certificate private key path for site")
@click.argument('site')
@click.argument('ssl-certificate-key-path')
def set_ssl_certificate_key(site, ssl_certificate_key_path):
	from neocli.config.site_config import set_ssl_certificate_key
	set_ssl_certificate_key(site, ssl_certificate_key_path)


@click.command('set-url-root', help="Set URL root for site")
@click.argument('site')
@click.argument('url-root')
def set_url_root(site, url_root):
	from neocli.config.site_config import set_url_root
	set_url_root(site, url_root)


@click.command('set-mariadb-host', help="Set MariaDB host for neocli")
@click.argument('host')
def set_mariadb_host(host):
	from neocli.utils.neocli import set_mariadb_host
	set_mariadb_host(host)


@click.command('set-redis-cache-host', help="Set Redis cache host for neocli")
@click.argument('host')
def set_redis_cache_host(host):
	"""
	Usage: neocli set-redis-cache-host localhost:6379/1
	"""
	from neocli.utils.neocli import set_redis_cache_host
	set_redis_cache_host(host)


@click.command('set-redis-queue-host', help="Set Redis queue host for neocli")
@click.argument('host')
def set_redis_queue_host(host):
	"""
	Usage: neocli set-redis-queue-host localhost:6379/2
	"""
	from neocli.utils.neocli import set_redis_queue_host
	set_redis_queue_host(host)


@click.command('set-redis-socketio-host', help="Set Redis socketio host for neocli")
@click.argument('host')
def set_redis_socketio_host(host):
	"""
	Usage: neocli set-redis-socketio-host localhost:6379/3
	"""
	from neocli.utils.neocli import set_redis_socketio_host
	set_redis_socketio_host(host)



@click.command('download-translations', help="Download latest translations")
def download_translations():
	from neocli.utils.translation import download_translations_p
	download_translations_p()


@click.command('renew-lets-encrypt', help="Sets Up latest cron and Renew Let's Encrypt certificate")
def renew_lets_encrypt():
	from neocli.config.lets_encrypt import renew_certs
	renew_certs()


@click.command('backup', help="Backup single site")
@click.argument('site')
def backup_site(site):
	from neocli.neocli import NeoCLI
	from neocli.utils.system import backup_site
	if site not in NeoCLI(".").sites:
		print(f'Site `{site}` not found')
		sys.exit(1)
	backup_site(site, neocli_path='.')


@click.command('backup-all-sites', help="Backup all sites in current neocli")
def backup_all_sites():
	from neocli.utils.system import backup_all_sites
	backup_all_sites(neocli_path='.')


@click.command('release', help="Release a Neo app (internal to the Neo team)")
@click.argument('app')
@click.argument('bump-type', type=click.Choice(['major', 'minor', 'patch', 'stable', 'prerelease']))
@click.option('--from-branch', default='develop')
@click.option('--to-branch', default='master')
@click.option('--remote', default='upstream')
@click.option('--owner', default='neo')
@click.option('--repo-name')
@click.option('--dont-frontport', is_flag=True, default=False, help='Front port fixes to new branches, example merging hotfix(v10) into staging-fixes(v11)')
def release(app, bump_type, from_branch, to_branch, owner, repo_name, remote, dont_frontport):
	from neocli.release import release
	frontport = not dont_frontport
	release(neocli_path='.', app=app, bump_type=bump_type, from_branch=from_branch, to_branch=to_branch, remote=remote, owner=owner, repo_name=repo_name, frontport=frontport)


@click.command('prepare-beta-release', help="Prepare major beta release from develop branch")
@click.argument('app')
@click.option('--owner', default='neo')
def prepare_beta_release(app, owner):
	from neocli.prepare_beta_release import prepare_beta_release
	prepare_beta_release(neocli_path='.', app=app, owner=owner)


@click.command('disable-production', help="Disables production environment for the neocli.")
def disable_production():
	from neocli.config.production_setup import disable_production
	disable_production(neocli_path='.')


@click.command('src', help="Prints neocli source folder path, which can be used as: cd `neocli src`")
def neocli_src():
	from neocli.cli import src
	print(os.path.dirname(src))


@click.command('find', help="Finds neoclies recursively from location")
@click.argument('location', default='')
def find_neoclies(location):
	from neocli.utils import find_neoclies
	find_neoclies(directory=location)


@click.command('migrate-env', help="Migrate Virtual Environment to desired Python Version")
@click.argument('python', type=str)
@click.option('--no-backup', 'backup', is_flag=True, default=True)
def migrate_env(python, backup=True):
	from neocli.utils.neocli import migrate_env
	migrate_env(python=python, backup=backup)


@click.command('generate-command-cache', help="Caches Neo Framework commands")
def generate_command_cache(neocli_path='.'):
	from neocli.utils import generate_command_cache
	return generate_command_cache(neocli_path=neocli_path)


@click.command('clear-command-cache', help="Clears Neo Framework cached commands")
def clear_command_cache(neocli_path='.'):
	from neocli.utils import clear_command_cache
	return clear_command_cache(neocli_path=neocli_path)
