from pyinfra import host
from pyinfra.operations import apt, server
from pyinfra.facts.server import LinuxDistribution

linux_distribution = host.get_fact(LinuxDistribution)
linux_name = linux_distribution['release_meta']['ID']
linux_codename = linux_distribution['release_meta']['CODENAME']

# Adding tailscale for raspberry pi
apt.key(
  name='Add tailscale key',
  src='https://pkgs.tailscale.com/stable/{}/{}.gpg'.format(linux_name, linux_codename),
)

apt.repo(
  name='Add tailscale repo',
  src='deb https://pkgs.tailscale.com/stable/{} {} main'.format(linux_name, linux_codename),
  filename='tailscale',
)

apt.packages(
  name='Install tailscale',
  packages=['apt-transport-https', 'tailscale'],
  update=True,
  latest=True,
)

server.shell(
  name='Start tailscale',
  commands=['tailscale up --authkey {}'.format(host.data.tailscale_preauth_key)]
)
