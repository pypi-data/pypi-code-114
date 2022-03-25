# imports - third party imports
import click

# imports - module imports
from neocli.utils.cli import (
	MultiCommandGroup,
	print_neocli_version,
	use_experimental_feature,
	setup_verbosity,
)


@click.group(cls=MultiCommandGroup)
@click.option(
	"--version",
	is_flag=True,
	is_eager=True,
	callback=print_neocli_version,
	expose_value=False,
)
@click.option(
	"--use-feature", is_eager=True, callback=use_experimental_feature, expose_value=False,
)
@click.option(
	"-v", "--verbose", is_flag=True, callback=setup_verbosity, expose_value=False,
)
def neocli_command(neocli_path="."):
	import neocli

	neocli.set_neo_version(neocli_path=neocli_path)


from neocli.commands.make import (
	drop,
	exclude_app_for_update,
	get_app,
	include_app_for_update,
	init,
	new_app,
	pip,
	remove_app,
)

neocli_command.add_command(init)
neocli_command.add_command(drop)
neocli_command.add_command(get_app)
neocli_command.add_command(new_app)
neocli_command.add_command(remove_app)
neocli_command.add_command(exclude_app_for_update)
neocli_command.add_command(include_app_for_update)
neocli_command.add_command(pip)


from neocli.commands.update import (
	retry_upgrade,
	switch_to_branch,
	switch_to_develop,
	update,
)

neocli_command.add_command(update)
neocli_command.add_command(retry_upgrade)
neocli_command.add_command(switch_to_branch)
neocli_command.add_command(switch_to_develop)


from neocli.commands.utils import (
	backup_all_sites,
	backup_site,
	neocli_src,
	clear_command_cache,
	disable_production,
	download_translations,
	find_neoclies,
	generate_command_cache,
	migrate_env,
	prepare_beta_release,
	release,
	renew_lets_encrypt,
	restart,
	set_mariadb_host,
	set_nginx_port,
	set_redis_cache_host,
	set_redis_queue_host,
	set_redis_socketio_host,
	set_ssl_certificate,
	set_ssl_certificate_key,
	set_url_root,
	start,
)

neocli_command.add_command(start)
neocli_command.add_command(restart)
neocli_command.add_command(set_nginx_port)
neocli_command.add_command(set_ssl_certificate)
neocli_command.add_command(set_ssl_certificate_key)
neocli_command.add_command(set_url_root)
neocli_command.add_command(set_mariadb_host)
neocli_command.add_command(set_redis_cache_host)
neocli_command.add_command(set_redis_queue_host)
neocli_command.add_command(set_redis_socketio_host)
neocli_command.add_command(download_translations)
neocli_command.add_command(backup_site)
neocli_command.add_command(backup_all_sites)
neocli_command.add_command(release)
neocli_command.add_command(renew_lets_encrypt)
neocli_command.add_command(disable_production)
neocli_command.add_command(neocli_src)
neocli_command.add_command(prepare_beta_release)
neocli_command.add_command(find_neoclies)
neocli_command.add_command(migrate_env)
neocli_command.add_command(generate_command_cache)
neocli_command.add_command(clear_command_cache)

from neocli.commands.setup import setup

neocli_command.add_command(setup)


from neocli.commands.config import config

neocli_command.add_command(config)

from neocli.commands.git import remote_reset_url, remote_set_url, remote_urls

neocli_command.add_command(remote_set_url)
neocli_command.add_command(remote_reset_url)
neocli_command.add_command(remote_urls)

from neocli.commands.install import install

neocli_command.add_command(install)
